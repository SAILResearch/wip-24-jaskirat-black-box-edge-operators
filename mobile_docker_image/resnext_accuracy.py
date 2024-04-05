import torch
from torchvision import transforms as T
from PIL import Image
import os
import numpy as np
import os
import onnxruntime as rt
from timeit import default_timer as timer
# Pre-processing function for ImageNet models
preprocess = T.Compose([
    T.Resize(232),
    T.CenterCrop(224),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
sess = rt.InferenceSession("resnext_models/resnext101.onnx",providers=['CPUExecutionProvider'])
input_name=sess.get_inputs()[0].name
output_name=sess.get_outputs()[0].name
predicted_labels=[]
batch_size=1
num_batches = int(50000/batch_size)
# read the image
start = timer()
for i,file in enumerate(os.listdir('imagenet')):
  img = Image.open('imagenet/'+file).convert('RGB')
  # pre-process the image like mobilenet and resize it to 224x224
  img = preprocess(img)
  # create a batch of 1 (that batch size is buned into the saved_model)
  img_batch = np.expand_dims(img, axis=0)
  result = sess.run([output_name], {input_name:img_batch})
  result=np.argsort(-np.squeeze(result))[:5].tolist()
  predicted_labels.append(result)
  if (i+1)%50==0:
        print('[%d / %d] batches done'%(i+1,num_batches))
inference_time = timer() - start
print("Inference Time(s): ",inference_time)
validation_labels={}
with open('validation_labels.txt') as f:
   lines=f.readlines()
   for line in lines:
     line=line.split("\n")[0].split(" ")
     validation_labels[line[0]]=int(line[1])

actual_labels=[]
for file in os.listdir('imagenet'):
  actual_labels.append(validation_labels[file])

def top1_accuracy(predictions, labels):
    top1 = 0
    top5 =0
    num_of_samples = len(labels)

    for i in range(num_of_samples):
        if predictions[i][0] == labels[i]:
            top1 += 1
        if np.isin(np.array([labels[i]]), predictions[i]):
          top5 += 1

    return top1/num_of_samples,top5/num_of_samples

top1,top5=top1_accuracy(predicted_labels,actual_labels)
print("Top-1 accuracy: {}, Top-5 accuracy: {}".format(top1, top5))
