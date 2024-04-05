import onnx
input_path="resnext101.onnx"
output_path="resnext101_earlyexit_sub_graph.onnx"
input_names=['input']
output_names=['/layer4/layer4.0/Add_output_0']
onnx.utils.extract_model(input_path, output_path, input_names, output_names)

output_path="resnext101_decision_sub_graph.onnx"
input_names=['/layer4/layer4.2/Add_output_0']
output_names=['output']
onnx.utils.extract_model(input_path, output_path, input_names, output_names)

model1=onnx.load('resnext101_earlyexit_sub_graph.onnx')
model2=onnx.load('resnext101_decision_sub_graph.onnx')
earlyexit_model=onnx.compose.merge_models(model1, model2,io_map=[("/layer4/layer4.0/Add_output_0","/layer4/layer4.2/Add_output_0")])
onnx.save(earlyexit_model, "resnext101_earlyexit.onnx")
