import torch
import numpy as np    # we're going to use numpy to process input and output data
import onnxruntime as ort   # to inference ONNX models, we use the ONNX Runtime
from PIL import Image
import base64
from io import BytesIO
from torchvision import transforms as T
from matplotlib.colors import hsv_to_rgb
fcn_resnet_preprocess_image = T.Compose([T.ToTensor(),
                                         T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])


class FCN():
    def __init__(self):
        self.num_classes = len([line.rstrip('\n')
                                for line in open('fcn_models/voc_classes.txt')])

    def preprocess(self, input):
        input_data = fcn_resnet_preprocess_image(input)
        input_data = np.expand_dims(input_data, 0)
        return input_data

    def get_palette(self):
        # prepare and return palette
        palette = [0] * self.num_classes * 3

        for hue in range(self.num_classes):
            if hue == 0:  # Background color
                colors = (0, 0, 0)
            else:
                colors = hsv_to_rgb((hue / self.num_classes, 0.75, 0.75))

            for i in range(3):
                palette[hue * 3 + i] = int(colors[i] * 255)

        return palette

    def colorize(self, labels):
        # generate colorized image from output labels and color palette
        result_img = Image.fromarray(labels).convert(
            'P', colors=self.num_classes)
        result_img.putpalette(self.get_palette())
        return np.array(result_img.convert('RGB'))

    def visualize_output(self, output):
        # assert(image.shape[0] == output.shape[1] and
        #        image.shape[1] == output.shape[2])  # Same height and width
        # assert(output.shape[0] == self.num_classes)

        # get classification labels
        raw_labels = np.argmax(output, axis=0).astype(np.uint8)

        # generate segmented image
        result_img = self.colorize(raw_labels)

        result_img = Image.fromarray(result_img)

        return result_img

    def get_image_buffer(self, image):
        img_buffer = BytesIO()
        image.save(img_buffer, 'PNG')
        img_buffer.seek(0)
        return img_buffer.read()

    def postprocess(self, output):
        result_img = self.visualize_output(output)
        segmented_image = base64.b64encode(
            self.get_image_buffer(result_img)).decode("utf8")
        result = {"base64_segmented_image": segmented_image}
        return result


fcn_model = FCN()


def fcn_single_inference(img):
    # Run the model on the backend
    image = Image.open(BytesIO(base64.b64decode(
        img.encode('utf-8')))).convert('RGB')
    # get the name of the first input of the model
    input_data = fcn_model.preprocess(image)
    session = ort.InferenceSession(
        'fcn_models/fcn-resnet101-11.onnx', providers=['CPUExecutionProvider'])
    result = session.run(
        [session.get_outputs()[0].name], {session.get_inputs()[0].name: input_data})
    result = fcn_model.postprocess(result[0][0])
    return result


def fcn_earlyexit_single_inference(img):
    # Run the model on the backend
    image = Image.open(BytesIO(base64.b64decode(
        img.encode('utf-8')))).convert('RGB')
    # get the name of the first input of the model
    input_data = fcn_model.preprocess(image)
    session = ort.InferenceSession(
        'fcn_models/fcn-resnet101-11_earlyexit.onnx', providers=['CPUExecutionProvider'])
    result = session.run(
        [session.get_outputs()[0].name], {session.get_inputs()[0].name: input_data})
    result = fcn_model.postprocess(result[0][0])
    return result


def fcn_int8_sptq_earlyexit_single_inference(img):
    # Run the model on the backend
    image = Image.open(BytesIO(base64.b64decode(
        img.encode('utf-8')))).convert('RGB')
    # get the name of the first input of the model
    input_data = fcn_model.preprocess(image)
    session = ort.InferenceSession(
        'fcn_models/fcn-resnet101-11_int8_sptq_earlyexit.onnx', providers=['CPUExecutionProvider'])
    result = session.run(
        [session.get_outputs()[0].name], {session.get_inputs()[0].name: input_data})
    result = fcn_model.postprocess(result[0][0])
    return result


def fcn_split_first_half_single_inference(img):
    # Run the model on the backend
    image = Image.open(BytesIO(base64.b64decode(
        img.encode('utf-8')))).convert('RGB')
    # get the name of the first input of the model
    input_data = fcn_model.preprocess(image)
    session = ort.InferenceSession(
        'fcn_models/fcn-resnet101-11_split_part1.onnx', providers=['CPUExecutionProvider'])
    result = session.run([session.get_outputs()[0].name, session.get_outputs()[
        1].name], {session.get_inputs()[0].name: input_data})
    return result


def fcn_split_second_half_single_inference(img):
    # Run the model on the backend
    # get the name of the first input of the model
    session = ort.InferenceSession(
        'fcn_models/fcn-resnet101-11_split_part2.onnx', providers=['CPUExecutionProvider'])
    result = session.run([session.get_outputs()[0].name], {session.get_inputs(
    )[0].name: img[0], session.get_inputs()[1].name: img[1]})
    result = fcn_model.postprocess(result[0][0])
    return result


def fcn_int8_sptq_earlyexit_first_half_single_inference(img):
    # Run the model on the backend
    image = Image.open(BytesIO(base64.b64decode(
        img.encode('utf-8')))).convert('RGB')
    # get the name of the first input of the model
    input_data = fcn_model.preprocess(image)
    session = ort.InferenceSession(
        'fcn_models/fcn-resnet101-11_int8_sptq_earlyexit_part1.onnx', providers=['CPUExecutionProvider'])
    result = session.run([session.get_outputs()[0].name, session.get_outputs(
    )[1].name], {session.get_inputs()[0].name: input_data})
    return result


def fcn_int8_sptq_earlyexit_second_half_single_inference(img):
    # Run the model on the backend
    # get the name of the first input of the model
    session = ort.InferenceSession(
        'fcn_models/fcn-resnet101-11_int8_sptq_earlyexit_part2.onnx', providers=['CPUExecutionProvider'])
    result = session.run([session.get_outputs()[0].name], {session.get_inputs(
    )[0].name: img[0], session.get_inputs()[1].name: img[1]})
    result = fcn_model.postprocess(result[0][0])
    return result


def fcn_int8_sptq_single_inference(img):
    # Run the model on the backend
    image = Image.open(BytesIO(base64.b64decode(
        img.encode('utf-8')))).convert('RGB')
    # get the name of the first input of the model
    input_data = fcn_model.preprocess(image)
    session = ort.InferenceSession(
        'fcn_models/fcn-resnet101-11_int8_sptq.onnx', providers=['CPUExecutionProvider'])
    result = session.run(
        [session.get_outputs()[0].name], {session.get_inputs()[0].name: input_data})
    result = fcn_model.postprocess(result[0][0])
    return result
