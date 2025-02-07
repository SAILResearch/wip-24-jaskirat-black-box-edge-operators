from flask import Flask, request
import numpy as np
from fcn_inference import *
from resnet_inference import *
from resnext_inference import *
from duc_inference import *
import json
import base64
app = Flask(__name__)


@app.route('/run_mobile_cloud_earlyexit_single_inference_duc', methods=['GET', 'POST'])
def run_mobile_cloud_earlyexit_single_inference_duc():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = duc_earlyexit_second_half_single_inference(
                request.json)
            return json.dumps(result)


@app.route('/run_mobile_cloud_earlyexit_single_inference_duc_int8_sptq', methods=['GET', 'POST'])
def run_mobile_cloud_earlyexit_single_inference_duc_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = duc_int8_sptq_earlyexit_second_half_single_inference(
                request.json)
            return json.dumps(result)


@app.route('/run_edge_cloud_earlyexit_single_inference_duc_int8_sptq', methods=['GET', 'POST'])
def run_edge_cloud_earlyexit_single_inference_duc_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = duc_int8_sptq_earlyexit_second_half_single_inference(
                request.json)
            return json.dumps(result)


@app.route('/run_edge_cloud_split_single_inference_duc', methods=['GET', 'POST'])
def run_edge_cloud_split_single_inference_duc():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = duc_split_second_half_single_inference(
                request.json)
            return json.dumps(result)


@app.route('/run_mobile_cloud_split_single_inference_duc', methods=['GET', 'POST'])
def run_mobile_cloud_split_single_inference_duc():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = duc_split_second_half_single_inference(
                request.json)
            return json.dumps(result)


@app.route('/run_cloud_single_inference_duc', methods=['GET', 'POST'])
def run_cloud_single_inference_duc():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = duc_single_inference(request.json[0])
            return json.dumps(result)


@app.route('/run_cloud_single_inference_duc_int8_sptq', methods=['GET', 'POST'])
def run_cloud_single_inference_duc_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = duc_int8_sptq_single_inference(request.json[0])
            return json.dumps(result)


@app.route('/run_cloud_earlyexit_single_inference_duc', methods=['GET', 'POST'])
def run_cloud_earlyexit_single_inference_duc():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = duc_earlyexit_single_inference(
                request.json[0])
            return json.dumps(result)


@app.route('/run_cloud_earlyexit_single_inference_duc_int8_sptq', methods=['GET', 'POST'])
def run_cloud_earlyexit_single_inference_duc_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = duc_int8_sptq_earlyexit_single_inference(
                request.json[0])
            return json.dumps(result)


@app.route('/run_mobile_cloud_earlyexit_single_inference_fcn_int8_sptq', methods=['GET', 'POST'])
def run_mobile_cloud_earlyexit_single_inference_fcn_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = request.json
            result = [np.frombuffer(base64.b64decode(result[0]), 'int64').reshape(
                2,), np.frombuffer(base64.b64decode(result[1]), 'float32').reshape(result[2])]
            result = fcn_int8_sptq_earlyexit_second_half_single_inference(
                result)
            return json.dumps(result)


@app.route('/run_mobile_cloud_earlyexit_single_inference_resnet_int8_sptq', methods=['GET', 'POST'])
def run_mobile_cloud_earlyexit_single_inference_resnet_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = request.json
            result = [np.frombuffer(base64.b64decode(i), 'float32').reshape(
                1, 1024, 14, 14) for i in result]
            result = resnet_int8_sptq_earlyexit_second_half_single_inference(
                result)
            return json.dumps(result)


@app.route('/run_mobile_cloud_earlyexit_single_inference_resnext_int8_sptq', methods=['GET', 'POST'])
def run_mobile_cloud_earlyexit_single_inference_resnext_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = request.json
            result = [np.frombuffer(base64.b64decode(i), 'float32').reshape(
                1, 1024, 14, 14) for i in result]
            result = resnext_int8_sptq_earlyexit_second_half_single_inference(
                result)
            return json.dumps(result)


@app.route('/run_edge_cloud_earlyexit_single_inference_fcn_int8_sptq', methods=['GET', 'POST'])
def run_edge_cloud_earlyexit_single_inference_fcn_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = request.json
            result = [np.frombuffer(base64.b64decode(result[0]), 'int64').reshape(
                2,), np.frombuffer(base64.b64decode(result[1]), 'float32').reshape(result[2])]
            result = fcn_int8_sptq_earlyexit_second_half_single_inference(
                result)
            return json.dumps(result)


@app.route('/run_edge_cloud_earlyexit_single_inference_resnext_int8_sptq', methods=['GET', 'POST'])
def run_edge_cloud_earlyexit_single_inference_resnext_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = request.json
            result = [np.frombuffer(base64.b64decode(i), 'float32').reshape(
                1, 1024, 14, 14) for i in result]
            result = resnext_int8_sptq_earlyexit_second_half_single_inference(
                result)
            return json.dumps(result)


@app.route('/run_edge_cloud_earlyexit_single_inference_resnet_int8_sptq', methods=['GET', 'POST'])
def run_edge_cloud_earlyexit_single_inference_resnet_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = request.json
            result = [np.frombuffer(base64.b64decode(i), 'float32').reshape(
                1, 1024, 14, 14) for i in result]
            result = resnet_int8_sptq_earlyexit_second_half_single_inference(
                result)
            return json.dumps(result)


@app.route('/run_edge_cloud_split_single_inference_fcn', methods=['GET', 'POST'])
def run_edge_cloud_split_single_inference_fcn():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = request.json
            result = [np.frombuffer(base64.b64decode(result[0]), 'int64').reshape(2,), np.frombuffer(base64.b64decode(result[1]), 'float32').reshape(result[2])]
            result = fcn_split_second_half_single_inference(result)
            return json.dumps(result)


@app.route('/run_edge_cloud_split_single_inference_resnet', methods=['GET', 'POST'])
def run_edge_cloud_split_single_inference_resnet():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = request.json
            result = [np.frombuffer(base64.b64decode(i), 'float32').reshape(
                1, 1024, 14, 14) for i in result]
            result = resnet_split_second_half_single_inference(result)
            return json.dumps(result)


@app.route('/run_edge_cloud_split_single_inference_resnext', methods=['GET', 'POST'])
def run_edge_cloud_split_single_inference_resnext():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = request.json
            result = [np.frombuffer(base64.b64decode(i), 'float32').reshape(
                1, 1024, 14, 14) for i in result]
            result = resnext_split_second_half_single_inference(
                result)
            return json.dumps(result)

@app.route('/run_mobile_cloud_split_single_inference_fcn', methods=['GET', 'POST'])
def run_mobile_cloud_split_single_inference_fcn():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = request.json
            result = [np.frombuffer(base64.b64decode(result[0]), 'int64').reshape(2,), np.frombuffer(base64.b64decode(result[1]), 'float32').reshape(result[2])]
            result = fcn_split_second_half_single_inference(result)
            return json.dumps(result)

@app.route('/run_mobile_cloud_split_single_inference_resnet', methods=['GET', 'POST'])
def run_mobile_cloud_split_single_inference_resnet():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = request.json
            result = [np.frombuffer(base64.b64decode(i), 'float32').reshape(
                1, 1024, 14, 14) for i in result]
            result = resnet_split_second_half_single_inference(result)
            return json.dumps(result)


@app.route('/run_mobile_cloud_split_single_inference_resnext', methods=['GET', 'POST'])
def run_mobile_cloud_split_single_inference_resnext():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = request.json
            result = [np.frombuffer(base64.b64decode(i), 'float32').reshape(
                1, 1024, 14, 14) for i in result]
            result = resnext_split_second_half_single_inference(
                result)
            return json.dumps(result)


@app.route('/run_cloud_single_inference_fcn', methods=['GET', 'POST'])
def run_cloud_single_inference_fcn():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = fcn_single_inference(request.json[0])
            return json.dumps(result)


@app.route('/run_cloud_single_inference_fcn_int8_sptq', methods=['GET', 'POST'])
def run_cloud_single_inference_fcn_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = fcn_int8_sptq_single_inference(request.json[0])
            return json.dumps(result)


@app.route('/run_cloud_earlyexit_single_inference_fcn', methods=['GET', 'POST'])
def run_cloud_earlyexit_single_inference_fcn():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = fcn_earlyexit_single_inference(
                request.json[0])
            return json.dumps(result)


@app.route('/run_cloud_earlyexit_single_inference_fcn_int8_sptq', methods=['GET', 'POST'])
def run_cloud_earlyexit_single_inference_fcn_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = fcn_int8_sptq_earlyexit_single_inference(
                request.json[0])
            return json.dumps(result)


@app.route('/run_cloud_single_inference_resnet', methods=['GET', 'POST'])
def run_cloud_single_inference_resnet():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnet_single_inference(request.json[0])
            return json.dumps(result)


@app.route('/run_cloud_single_inference_resnet_int8_sptq', methods=['GET', 'POST'])
def run_cloud_single_inference_resnet_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnet_int8_sptq_single_inference(request.json[0])
            return json.dumps(result)

@app.route('/run_cloud_earlyexit_single_inference_resnet_int8_sptq', methods=['GET', 'POST'])
def run_cloud_earlyexit_single_inference_resnet_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnet_int8_sptq_earlyexit_single_inference(
                request.json[0])
            return json.dumps(result)


@app.route('/run_cloud_earlyexit_single_inference_resnet', methods=['GET', 'POST'])
def run_cloud_earlyexit_single_inference_resnet():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnet_earlyexit_single_inference(request.json[0])
            return json.dumps(result)


@app.route('/run_cloud_single_inference_resnext', methods=['GET', 'POST'])
def run_cloud_single_inference_resnext():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnext_single_inference(request.json[0])
            return json.dumps(result)

@app.route('/run_cloud_single_inference_resnext_int8_sptq', methods=['GET', 'POST'])
def run_cloud_single_inference_resnext_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnext_int8_sptq_single_inference(request.json[0])
            return json.dumps(result)


@app.route('/run_cloud_earlyexit_single_inference_resnext_int8_sptq', methods=['GET', 'POST'])
def run_cloud_earlyexit_single_inference_resnext_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnext_int8_sptq_earlyexit_single_inference(
                request.json[0])
            return json.dumps(result)


@app.route('/run_cloud_earlyexit_single_inference_resnext', methods=['GET', 'POST'])
def run_cloud_earlyexit_single_inference_resnext():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnext_earlyexit_single_inference(
                request.json[0])
            return json.dumps(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True, threaded=True)
