input_path = "ResNet101-DUC-12.onnx"
output_path = "ResNet101-DUC-12_split_part1.onnx"
input_names = ['data']
output_names = ['conv5_1_1x1_proj/bn','conv5_1_3x3/relu']
onnx.utils.extract_model(input_path, output_path, input_names, output_names)

output_path = "ResNet101-DUC-12_split_part2.onnx"
input_names=['conv5_1_1x1_proj/bn','conv5_1_3x3/relu']
output_names = ['seg_loss']
onnx.utils.extract_model(input_path, output_path, input_names, output_names)