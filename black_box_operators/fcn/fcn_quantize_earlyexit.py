input_path = "fcn-resnet101-11_int8_sptq.onnx"
output_path = "fcn-resnet101-11_int8_sptq_earlyexit_sub_graph.onnx"
input_names = ['input']
output_names = ['995','967']
onnx.utils.extract_model(input_path, output_path, input_names, output_names)

output_path = "fcn-resnet101-11_int8_sptq_decision_sub_graph.onnx"
input_names = ['995','987']
output_names = ['out']
onnx.utils.extract_model(input_path, output_path, input_names, output_names)

model1=onnx.load("fcn-resnet101-11_int8_sptq_earlyexit_sub_graph.onnx")
model2=onnx.load("fcn-resnet101-11_int8_sptq_decision_sub_graph.onnx")
model2 = onnx.compose.add_prefix(model2, prefix="m1/")
earlyexit_model=onnx.compose.merge_models(model1, model2,io_map=[("995","m1/995"),("967","m1/987")])
onnx.save(earlyexit_model, "fcn-resnet101-11_int8_sptq_earlyexit.onnx")
