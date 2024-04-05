from __future__ import print_function
import mxnet as mx
import numpy as np
import glob
import os
from mxnet.contrib.onnx import import_model
from cityscapes_loader import CityLoader

if len(mx.test_utils.list_gpus())==0:
    ctx = mx.cpu()
else:
    ctx = mx.gpu(0)
# Path to validation data
data_dir = '/leftImg8bit/val'
# Path to validation labels
label_dir = '/gtFine/val'
# Set batch size
batch_size = 1
index = 0
val_lst = []
# images
all_images = glob.glob(os.path.join(data_dir, '*/*.png'))
all_images.sort()
for p in all_images:
    l = p.replace(data_dir, label_dir).replace('leftImg8bit', 'gtFine_labelIds')
    if os.path.isfile(l):
        index += 1
        for i in range(1, 8):
            val_lst.append([str(index), p, l, "512", str(256 * i)])


val_out = open('val.lst', "w")
for line in val_lst:
    print('\t'.join(line),file=val_out)
