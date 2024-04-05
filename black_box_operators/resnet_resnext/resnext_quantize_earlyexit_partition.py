input_path = "resnext101_int8_sptq_earlyexit.onnx"
output_path = "resnext101_int8_sptq_earlyexit_part1.onnx"
input_names = ['input']
output_names = ['/layer3/layer3.16/Add_output_0']
onnx.utils.extract_model(input_path, output_path, input_names, output_names)

output_path = "resnext101_int8_sptq_earlyexit_part2.onnx"
input_names=['/layer3/layer3.16/Add_output_0']
output_names = ['output']
onnx.utils.extract_model(input_path, output_path, input_names, output_names)