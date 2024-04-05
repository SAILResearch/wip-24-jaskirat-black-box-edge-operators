import onnx
input_path="wide-resnet101_int8_sptq.onnx"
output_path="wide-resnet101_int8_sptq_earlyexit_sub_graph.onnx"
input_names=['input']
output_names=['/layer4/layer4.0/Add_output_0']
onnx.utils.extract_model(input_path, output_path, input_names, output_names)

output_path="wide-resnet101_int8_sptq_decision_sub_graph.onnx"
input_names=['/layer4/layer4.2/Add_output_0']
output_names=['output']
onnx.utils.extract_model(input_path, output_path, input_names, output_names)

model1=onnx.load('wide-resnet101_int8_sptq_earlyexit_sub_graph.onnx')
model2=onnx.load('wide-resnet101_int8_sptq_decision_sub_graph.onnx')
earlyexit_model=onnx.compose.merge_models(model1, model2,io_map=[("/layer4/layer4.0/Add_output_0","/layer4/layer4.2/Add_output_0")])
onnx.save(earlyexit_model, "wide-resnet101_int8_sptq_earlyexit.onnx")