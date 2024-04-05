import torch
import numpy as np    # we're going to use numpy to process input and output data
import onnxruntime as ort   # to inference ONNX models, we use the ONNX Runtime
import json
from PIL import Image
import base64
from io import BytesIO
from torchvision import transforms as T
resnext_preprocess_image = T.Compose([T.Resize(232), T.CenterCrop(224), T.ToTensor(
), T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])


class Resnext():
    def __init__(self):
        self.labels = self.load_labels(
            'resnext_models/imagenet-simple-labels.json')

    def load_labels(self, path):
        with open(path) as f:
            data = json.load(f)
        return data

    def preprocess(self, input):
        input_data = resnext_preprocess_image(input)
        input_data = np.expand_dims(input_data, 0)
        return input_data

    def postprocess(self, result):
        result = self.labels[np.argmax(result)]
        return {"Prediction: ": result}


resnext_model = Resnext()
providers = [("CUDAExecutionProvider", {"cudnn_conv_algo_search": "DEFAULT"})]


def resnext_single_inference(img):
    # Run the model on the backend
    image = Image.open(BytesIO(base64.b64decode(
        img.encode('utf-8')))).convert('RGB')
    # get the name of the first input of the model
    input_data = resnext_model.preprocess(image)
    session = ort.InferenceSession(
        'resnext_models/resnext101.onnx', providers=providers)
    result = session.run(
        [session.get_outputs()[0].name], {session.get_inputs()[0].name: input_data})
    result = resnext_model.postprocess(result)
    return result


def resnext_earlyexit_single_inference(img):
    # Run the model on the backend
    image = Image.open(BytesIO(base64.b64decode(
        img.encode('utf-8')))).convert('RGB')
    # get the name of the first input of the model
    input_data = resnext_model.preprocess(image)
    session = ort.InferenceSession(
        'resnext_models/resnext101_earlyexit.onnx', providers=providers)
    result = session.run(
        [session.get_outputs()[0].name], {session.get_inputs()[0].name: input_data})
    result = resnext_model.postprocess(result)
    return result


def resnext_int8_sptq_earlyexit_single_inference(img):
    # Run the model on the backend
    image = Image.open(BytesIO(base64.b64decode(
        img.encode('utf-8')))).convert('RGB')
    # get the name of the first input of the model
    input_data = resnext_model.preprocess(image)
    session = ort.InferenceSession(
        'resnext_models/resnext101_int8_sptq_earlyexit.onnx', providers=providers)
    result = session.run(
        [session.get_outputs()[0].name], {session.get_inputs()[0].name: input_data})
    result = resnext_model.postprocess(result)
    return result

def resnext_split_first_half_single_inference(img):
    # Run the model on the backend
    image = Image.open(BytesIO(base64.b64decode(
        img.encode('utf-8')))).convert('RGB')
    # get the name of the first input of the model
    input_data = resnext_model.preprocess(image)
    session = ort.InferenceSession(
        'resnext_models/resnext101_split_part1.onnx', providers=providers)
    result = session.run([session.get_outputs()[0].name], {
        session.get_inputs()[0].name: input_data})
    return result


def resnext_split_second_half_single_inference(img):
    # Run the model on the backend
    # get the name of the first input of the model
    session = ort.InferenceSession(
        'resnext_models/resnext101_split_part2.onnx', providers=providers)
    result = session.run([session.get_outputs()[0].name], {
        session.get_inputs()[0].name: img[0]})
    result = resnext_model.postprocess(result)
    return result


def resnext_int8_sptq_earlyexit_first_half_single_inference(img):
    # Run the model on the backend
    image = Image.open(BytesIO(base64.b64decode(
        img.encode('utf-8')))).convert('RGB')
    # get the name of the first input of the model
    input_data = resnext_model.preprocess(image)
    session = ort.InferenceSession(
        'resnext_models/resnext101_int8_sptq_earlyexit_part1.onnx', providers=providers)
    result = session.run([session.get_outputs()[0].name], {
        session.get_inputs()[0].name: input_data})
    return result


def resnext_int8_sptq_earlyexit_second_half_single_inference(img):
    # Run the model on the backend
    # get the name of the first input of the model
    session = ort.InferenceSession(
        'resnext_models/resnext101_int8_sptq_earlyexit_part2.onnx', providers=providers)
    result = session.run([session.get_outputs()[0].name], {
        session.get_inputs()[0].name: img[0]})
    result = resnext_model.postprocess(result)
    return result


def resnext_int8_sptq_single_inference(img):
    # Run the model on the backend
    image = Image.open(BytesIO(base64.b64decode(
        img.encode('utf-8')))).convert('RGB')
    # get the name of the first input of the model
    input_data = resnext_model.preprocess(image)
    session = ort.InferenceSession(
        'resnext_models/resnext101_int8_sptq.onnx', providers=providers)
    result = session.run(
        [session.get_outputs()[0].name], {session.get_inputs()[0].name: input_data})
    result = resnext_model.postprocess(result)
    return result
