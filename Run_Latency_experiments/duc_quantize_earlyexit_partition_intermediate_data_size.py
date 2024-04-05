import onnx
import onnxruntime as ort
import numpy as np
import csv
import sys
from PIL import Image
import os
import cv2 as cv
import math

dataset = os.listdir('cityscapes_100_images')

def preprocess(im, rgb_mean):
        # Convert to float32
        test_img = im.astype(np.float32)
        # Extrapolate image with a small border in order obtain an accurate reshaped image after DUC layer
        test_shape = [im.shape[0], im.shape[1]]
        cell_shapes = [math.ceil(l / 8)*8 for l in test_shape]
        test_img = cv.copyMakeBorder(test_img, 0, max(0, int(cell_shapes[0]) - im.shape[0]), 0, max(
            0, int(cell_shapes[1]) - im.shape[1]), cv.BORDER_CONSTANT, value=rgb_mean)
        test_img = np.transpose(test_img, (2, 0, 1))
        # subtract rbg mean
        for i in range(3):
            test_img[i] -= rgb_mean[i]
        test_img = np.expand_dims(test_img, axis=0)
        return test_img


def get_size_in_megabits(data):
    # Get the size in bits
    size_in_bits = data.nbytes * 8
    # Convert to megabits
    size_in_megabits = size_in_bits / (1024 * 1024)
    return size_in_megabits

# Load the ONNX model
model = onnx.load('ResNet101-DUC-12_int8_sptq_earlyexit.onnx')

# Create an ONNX runtime session
ort_session = ort.InferenceSession(model.SerializeToString())
input_name = ort_session.get_inputs()[0].name

# Get the original outputs
org_outputs = [x.name for x in ort_session.get_outputs()]

# Add all intermediate outputs to the ONNX graph
for node in model.graph.node:
    for output in node.output:
        if output not in org_outputs:
            model.graph.output.extend([onnx.ValueInfoProto(name=output)])

# Create a new ONNX runtime session with the updated model
ort_session = ort.InferenceSession(model.SerializeToString())

# Create a dummy input tensor
image_tensors=[]
for img in dataset:
    image = np.array(Image.open(os.path.join('cityscapes_100_images', img)).convert('RGB'))
    image = cv.resize(image, (800, 800))
    rgb_mean = cv.mean(image)
    image = preprocess(image, rgb_mean)
    image_tensors.append(image)

# Prepare data for CSV
csv_data = [("Node Name", "Output Tensor Name", "Output Tensor Dimention","Output Tensor Size (Mb)")]

# Iterate through each node in the ONNX graph
for node in model.graph.node:
    # Get the names of the outputs produced by the current node
    if node.name=='conv4_23':
        node_outputs = node.output
        # Run the ONNX model for the current node's outputs
        for image_tensor in image_tensors:
            ort_outs = ort_session.run(node_outputs, {input_name: image_tensor})
            # Append node names, output names, and sizes in megabits to the CSV data
            for output_name, output_data in zip(node_outputs, ort_outs):
                size_in_megabits = get_size_in_megabits(output_data)
                csv_data.append((node.name, output_name, output_data.shape, size_in_megabits))

# Write data to CSV file
csv_file_path = "duc_quantize_earlyexit_partition_intermediate_data_size.csv"
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

print(f"CSV file saved at: {csv_file_path}")
