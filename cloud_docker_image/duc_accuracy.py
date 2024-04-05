from __future__ import print_function
import numpy as np
from timeit import default_timer as timer
import glob
import os
from cityscapes_loader import CityLoader
import torch
import onnxruntime as rt
import mxnet as mx
if len(mx.test_utils.list_gpus())==0:
    ctx = mx.cpu()
else:
    ctx = mx.gpu(0)
providers = [("CUDAExecutionProvider", {"cudnn_conv_algo_search": "DEFAULT"})]
sess = rt.InferenceSession("duc_models/ResNet101-DUC-12.onnx",providers=providers)
input_name=sess.get_inputs()[0].name
output_name=[i.name for i in sess.get_outputs()]
# Path to validation data
data_dir = '/leftImg8bit/val'
# Path to validation labels
label_dir = '/gtFine/val'
# Set batch size
batch_size = 1

def check_label_shapes(labels, preds, shape=0):
    if shape == 0:
        label_shape, pred_shape = len(labels), len(preds)
    else:
        label_shape, pred_shape = labels.shape, preds.shape

    if label_shape != pred_shape:
        raise ValueError("Shape of labels {} does not match shape of "
                         "predictions {}".format(label_shape, pred_shape))

class IoUMetric(mx.metric.EvalMetric):
    def __init__(self, ignore_label, label_num, name='IoU'):
        self._ignore_label = ignore_label
        self._label_num = label_num
        super(IoUMetric, self).__init__(name=name)

    def reset(self):
        self._tp = [0.0] * self._label_num
        self._denom = [0.0] * self._label_num

    def update(self, labels, preds):
        check_label_shapes(labels, preds)
        for i in range(len(labels)):
            pred_label = mx.ndarray.argmax_channel(preds[i]).asnumpy().astype('int32')
            label = labels[i].asnumpy().astype('int32')

            check_label_shapes(label, pred_label)

            iou = 0
            eps = 1e-6
            for j in range(self._label_num):
                pred_cur = (pred_label.flat == j)
                gt_cur = (label.flat == j)
                tp = np.logical_and(pred_cur, gt_cur).sum()
                denom = np.logical_or(pred_cur, gt_cur).sum() - np.logical_and(pred_cur, label.flat == self._ignore_label).sum()
                assert tp <= denom
                self._tp[j] += tp
                self._denom[j] += denom
                iou += self._tp[j] / (self._denom[j] + eps)
            iou /= self._label_num
            self.sum_metric = iou
            self.num_inst = 1

# Create evaluation metric
met = IoUMetric(ignore_label=255, label_num=19, name="IoU")
metric = mx.metric.create(met)
loader = CityLoader
val_args = {
    'data_path'             : data_dir,
    'label_path'            : label_dir,
    'rgb_mean'              : (122.675, 116.669, 104.008),
    'batch_size'            : batch_size,
    'scale_factors'         : [1],
    'data_name'             : 'data',
    'label_name'            : 'seg_loss_label',
    'data_shape'            : [tuple(list([batch_size, 3, 800, 800]))],
    'label_shape'           : [tuple([batch_size, (160000)])],
    'use_random_crop'       : False,
    'use_mirror'            : False,
    'ds_rate'               : 8,
    'convert_label'         : True,
    'multi_thread'          : False,
    'cell_width'            : 2,
    'random_bound'          : [120,120],
}
val_dataloader = loader('val.lst', val_args)
# reset data loader
val_dataloader.reset()
# reset evaluation metric
metric.reset()
# loop over batches
from timeit import default_timer as timer
start = timer()
for nbatch, eval_batch in enumerate(val_dataloader):
    # get output
    # update evaluation metric
    outputs = sess.run(output_name, {input_name: eval_batch.data[0].asnumpy()})[0]
    outputs=[mx.nd.array(outputs,ctx)]
    metric.update(eval_batch.label,outputs)
    # print progress
    if nbatch%50==0:
        print('{} / {} batches done'.format(nbatch,int(3500/batch_size)))
inference_time = timer() - start
print("Inference Time(s): ",inference_time)
print("mean Intersection Over Union (mIOU): {}".format(metric.get()[1]))
