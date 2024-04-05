import onnx
input_path = "fcn-resnet101-11-original.onnx"
output_path = "fcn-resnet101-11.onnx"
input_names = ['input']
output_names = ['out']
onnx.utils.extract_model(input_path, output_path, input_names, output_names)
