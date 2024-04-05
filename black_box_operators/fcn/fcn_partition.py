import onnx
input_path = "fcn-resnet101-11.onnx"
output_path = "fcn-resnet101-11_split_part1.onnx"
input_names = ['input']
output_names = ['995','945']
onnx.utils.extract_model(input_path, output_path, input_names, output_names)
output_path = "fcn-resnet101-11_split_part2.onnx"
input_names = ['995','945']
output_names= ['out']
onnx.utils.extract_model(input_path, output_path, input_names, output_names)
