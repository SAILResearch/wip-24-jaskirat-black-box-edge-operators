import onnx
input_path="ResNet101-DUC-12_int8_sptq_earlyexit.onnx"
output_path = "ResNet101-DUC-12_int8_sptq_earlyexit_part1.onnx"
input_names=['data']
output_names = ['conv4_23']
onnx.utils.extract_model(input_path, output_path, input_names, output_names)

output_path="ResNet101-DUC-12_int8_sptq_earlyexit_part2.onnx"
input_names = ['conv4_23']
output_names = ['seg_loss']
onnx.utils.extract_model(input_path, output_path, input_names, output_names)
