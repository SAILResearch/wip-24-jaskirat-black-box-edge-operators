import onnx
import onnxruntime as ort
import numpy as np
import csv
import sys
from PIL import Image
import os
from torchvision import transforms as T
resnet_preprocess_image = T.Compose([T.Resize(232), T.CenterCrop(224), T.ToTensor(
), T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

dataset = os.listdir('imagenet_100_images')

def get_size_in_megabits(data):
    # Get the size in bits
    size_in_bits = data.nbytes * 8
    # Convert to megabits
    size_in_megabits = size_in_bits / (1024 * 1024)
    return size_in_megabits

# Load the ONNX model
model = onnx.load('wide-resnet101.onnx')

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
    image = Image.open(os.path.join('imagenet_100_images', img)).convert('RGB')
    image=resnet_preprocess_image(image)
    image = np.expand_dims(image, 0)
    image_tensors.append(image)

# Prepare data for CSV
csv_data = [("Node Name", "Output Tensor Name", "Output Tensor Dimention","Output Tensor Size (Mb)")]

# Iterate through each node in the ONNX graph
for node in model.graph.node:
    # Get the names of the outputs produced by the current node
    if node.name=='/layer3/layer3.16/Add':
        node_outputs = node.output
        # Run the ONNX model for the current node's outputs
        for image_tensor in image_tensors:
            ort_outs = ort_session.run(node_outputs, {input_name: image_tensor})
            # Append node names, output names, and sizes in megabits to the CSV data
            for output_name, output_data in zip(node_outputs, ort_outs):
                size_in_megabits = get_size_in_megabits(output_data)
                csv_data.append((node.name, output_name, output_data.shape, size_in_megabits))

# Write data to CSV file
csv_file_path = "resnet_partition_intermediate_data_size.csv"
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

print(f"CSV file saved at: {csv_file_path}")