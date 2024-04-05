import onnx
input_path="fcn-resnet101-11_int8_sptq_earlyexit.onnx"
output_path = "fcn-resnet101-11_int8_sptq_earlyexit_part1.onnx"
input_names = ['input']
output_names = ['995','905']
onnx.utils.extract_model(input_path, output_path, input_names, output_names)

output_path="fcn-resnet101-11_int8_sptq_earlyexit_part2.onnx"
input_names = ['995','905']
output_names = ['m1/out']
onnx.utils.extract_model(input_path, output_path, input_names, output_names)
