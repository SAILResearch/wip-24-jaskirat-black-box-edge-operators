import torch
import numpy as np    # we're going to use numpy to process input and output data
import onnxruntime as ort   # to inference ONNX models, we use the ONNX Runtime
from PIL import Image
import base64
from io import BytesIO
from duc_models import cityscapes_labels
import math
import cv2 as cv


class DUC():
    def __init__(self):
        # get train id to color mappings from file
        trainId2colors = {
            label.trainId: label.color for label in cityscapes_labels.labels}
        # prepare and return palette
        self.palette = [0] * 256 * 3
        for trainId in trainId2colors:
            colors = trainId2colors[trainId]
            if trainId == 255:
                colors = (0, 0, 0)
            for i in range(3):
                self.palette[trainId * 3 + i] = colors[i]
        self.ds_rate = 8
        self.label_num = 19
        self.cell_width = 2
        self.img_height, self.img_width = (800, 800)

    def preprocess(self, im, rgb_mean):
        # Convert to float32
        test_img = im.astype(np.float32)
        # Extrapolate image with a small border in order obtain an accurate reshaped image after DUC layer
        test_shape = [im.shape[0], im.shape[1]]
        cell_shapes = [math.ceil(l / 8)*8 for l in test_shape]
        test_img = cv.copyMakeBorder(test_img, 0, max(0, int(cell_shapes[0]) - im.shape[0]), 0, max(
            0, int(cell_shapes[1]) - im.shape[1]), cv.BORDER_CONSTANT, value=rgb_mean)
        test_img = np.transpose(test_img, (2, 0, 1))
        # subtract rbg mean
        for i in range(3):
            test_img[i] -= rgb_mean[i]
        test_img = np.expand_dims(test_img, axis=0)
        return test_img

    def colorize(self, labels):
        # generate colorized image from output labels and color palette
        result_img = Image.fromarray(labels).convert(
            'P')
        result_img.putpalette(self.palette)
        return np.array(result_img.convert('RGB'))

    def postprocess(self, labels, result_shape):
        result_height, result_width = result_shape
        # re-arrange output
        test_width = int((int(self.img_width) / self.ds_rate) * self.ds_rate)
        test_height = int((int(self.img_height) / self.ds_rate) * self.ds_rate)
        feat_width = int(test_width / self.ds_rate)
        feat_height = int(test_height / self.ds_rate)
        labels = labels.reshape(
            (self.label_num, 4, 4, feat_height, feat_width))
        labels = np.transpose(labels, (0, 3, 1, 4, 2))
        labels = labels.reshape(
            (self.label_num, int(test_height / self.cell_width), int(test_width / self.cell_width)))

        labels = labels[:, :int(self.img_height / self.cell_width),
                        :int(self.img_width / self.cell_width)]
        labels = np.transpose(labels, [1, 2, 0])
        labels = cv.resize(labels, (result_width, result_height),
                           interpolation=cv.INTER_LINEAR)
        labels = np.transpose(labels, [2, 0, 1])
        # get classification labels
        raw_labels = np.argmax(labels, axis=0).astype(np.uint8)
        # generate segmented image
        result = Image.fromarray(self.colorize(
            raw_labels)).resize(result_shape[::-1])
        result = base64.b64encode(
            self.get_image_buffer(result)).decode("utf8")
        result = {"base64_segmented_image": result}
        return result

    def get_image_buffer(self, image):
        img_buffer = BytesIO()
        image.save(img_buffer, 'PNG')
        img_buffer.seek(0)
        return img_buffer.read()


duc_model = DUC()
providers = [("CUDAExecutionProvider", {"cudnn_conv_algo_search": "DEFAULT"})]


def duc_single_inference(img):
    # Run the model on the backend
    image = np.array(Image.open(BytesIO(base64.b64decode(
        img.encode('utf-8')))).convert('RGB'))
    result_shape = [image.shape[0], image.shape[1]]
    image = cv.resize(image, (800, 800))
    rgb_mean = cv.mean(image)
    # get the name of the first input of the model
    input_data = duc_model.preprocess(image, rgb_mean)
    session = ort.InferenceSession(
        'duc_models/ResNet101-DUC-12.onnx', providers=providers)
    result = session.run(
        [session.get_outputs()[0].name], {session.get_inputs()[0].name: input_data})
    result = duc_model.postprocess(result[0][0], result_shape)
    return result


def duc_earlyexit_single_inference(img):
    # Run the model on the backend
    image = np.array(Image.open(BytesIO(base64.b64decode(
        img.encode('utf-8')))).convert('RGB'))
    # get the name of the first input of the model
    result_shape = [image.shape[0], image.shape[1]]
    image = cv.resize(image, (800, 800))
    rgb_mean = cv.mean(image)
    # get the name of the first input of the model
    input_data = duc_model.preprocess(image, rgb_mean)
    session = ort.InferenceSession(
        'duc_models/ResNet101-DUC-12_earlyexit.onnx', providers=providers)
    result = session.run(
        [session.get_outputs()[0].name], {session.get_inputs()[0].name: input_data})
    result = duc_model.postprocess(result[0][0], result_shape)
    return result


def duc_int8_sptq_earlyexit_single_inference(img):
    # Run the model on the backend
    image = np.array(Image.open(BytesIO(base64.b64decode(
        img.encode('utf-8')))).convert('RGB'))
    # get the name of the first input of the model
    result_shape = [image.shape[0], image.shape[1]]
    image = cv.resize(image, (800, 800))
    rgb_mean = cv.mean(image)
    # get the name of the first input of the model
    input_data = duc_model.preprocess(image, rgb_mean)
    session = ort.InferenceSession(
        'duc_models/ResNet101-DUC-12_int8_sptq_earlyexit.onnx', providers=providers)
    result = session.run(
        [session.get_outputs()[0].name], {session.get_inputs()[0].name: input_data})
    result = duc_model.postprocess(result[0][0], result_shape)
    return result


def duc_split_first_half_single_inference(img):
    # Run the model on the backend
    image = np.array(Image.open(BytesIO(base64.b64decode(
        img.encode('utf-8')))).convert('RGB'))
    # get the name of the first input of the model
    result_shape = [image.shape[0], image.shape[1]]
    image = cv.resize(image, (800, 800))
    rgb_mean = cv.mean(image)
    # get the name of the first input of the model
    input_data = duc_model.preprocess(image, rgb_mean)
    session = ort.InferenceSession(
        'duc_models/ResNet101-DUC-12_split_part1.onnx', providers=providers)
    result = session.run([session.get_outputs()[0].name, session.get_outputs()[1].name], {
        session.get_inputs()[0].name: input_data})
    result = [base64.b64encode(result[0]).decode(
        'utf-8'), base64.b64encode(result[1]).decode('utf-8'), result_shape]
    return result


def duc_split_second_half_single_inference(img):
    # Run the model on the backend
    # get the name of the first input of the model
    intermediate_result = [np.frombuffer(base64.b64decode(img[0]), 'float32').reshape(
        1, 2048, 100, 100), np.frombuffer(base64.b64decode(img[1]), 'float32').reshape(1, 512, 100, 100)]
    session = ort.InferenceSession(
        'duc_models/ResNet101-DUC-12_split_part2.onnx', providers=providers)
    result = session.run([session.get_outputs()[0].name], {session.get_inputs(
    )[0].name: intermediate_result[0], session.get_inputs(
    )[1].name: intermediate_result[1]})
    result = duc_model.postprocess(result[0][0], img[2])
    return result


def duc_int8_sptq_earlyexit_first_half_single_inference(img):
    # Run the model on the backend
    image = np.array(Image.open(BytesIO(base64.b64decode(
        img.encode('utf-8')))).convert('RGB'))
    # get the name of the first input of the model
    result_shape = [image.shape[0], image.shape[1]]
    image = cv.resize(image, (800, 800))
    rgb_mean = cv.mean(image)
    # get the name of the first input of the model
    input_data = duc_model.preprocess(image, rgb_mean)
    session = ort.InferenceSession(
        'duc_models/ResNet101-DUC-12_int8_sptq_earlyexit_part1.onnx', providers=providers)
    result = session.run([session.get_outputs()[0].name], {
        session.get_inputs()[0].name: input_data})
    result = [base64.b64encode(result[0]).decode('utf-8'), result_shape]
    return result


def duc_int8_sptq_earlyexit_second_half_single_inference(img):
    # Run the model on the backend
    # get the name of the first input of the model
    intermediate_result = [np.frombuffer(base64.b64decode(
        img[0]), 'float32').reshape(1, 1024, 100, 100)]
    session = ort.InferenceSession(
        'duc_models/ResNet101-DUC-12_int8_sptq_earlyexit_part2.onnx', providers=providers)
    result = session.run([session.get_outputs()[0].name], {session.get_inputs(
    )[0].name: intermediate_result[0]})
    result = duc_model.postprocess(result[0][0], img[1])
    return result


def duc_int8_sptq_single_inference(img):
    # Run the model on the backend
    image = np.array(Image.open(BytesIO(base64.b64decode(
        img.encode('utf-8')))).convert('RGB'))
    # get the name of the first input of the model
    result_shape = [image.shape[0], image.shape[1]]
    image = cv.resize(image, (800, 800))
    rgb_mean = cv.mean(image)
    # get the name of the first input of the model
    input_data = duc_model.preprocess(image, rgb_mean)
    session = ort.InferenceSession(
        'duc_models/ResNet101-DUC-12_int8_sptq.onnx', providers=providers)
    result = session.run(
        [session.get_outputs()[0].name], {session.get_inputs()[0].name: input_data})
    result = duc_model.postprocess(result[0][0], result_shape)
    return result
