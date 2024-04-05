import onnx
input_path="ResNet101-DUC-12.onnx"
output_path="ResNet101-DUC-12_earlyexit_sub_graph.onnx"
input_names=['data']
output_names=['conv5_1']
onnx.utils.extract_model(input_path, output_path, input_names, output_names)
output_path="ResNet101-DUC-12_decision_sub_graph.onnx"
input_names=['conv5_3']
output_names=['seg_loss']
onnx.utils.extract_model(input_path, output_path, input_names, output_names)

model1=onnx.load('ResNet101-DUC-12_earlyexit_sub_graph.onnx')
model2=onnx.load('ResNet101-DUC-12_decision_sub_graph.onnx')
earlyexit_model=onnx.compose.merge_models(model1, model2,io_map=[("conv5_1","conv5_3")])
onnx.save(earlyexit_model, "ResNet101-DUC-12_earlyexit.onnx")