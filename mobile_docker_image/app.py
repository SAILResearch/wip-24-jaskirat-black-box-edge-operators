from flask import Flask, request
from fcn_inference import *
from resnet_inference import *
from resnext_inference import *
from duc_inference import *
import requests
import json
import base64
app = Flask(__name__)



@app.route('/run_mobile_cloud_earlyexit_single_inference_duc_int8_sptq', methods=['GET', 'POST'])
def run_mobile_cloud_earlyexit_single_inference_duc_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = duc_int8_sptq_earlyexit_first_half_single_inference(
                request.json[0])
            result = requests.post('http://edge_inference_container:5001/run_mobile_cloud_earlyexit_single_inference_duc_int8_sptq',
                                   json=result, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_mobile_edge_earlyexit_single_inference_duc_int8_sptq', methods=['GET', 'POST'])
def run_mobile_edge_earlyexit_single_inference_duc_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = duc_int8_sptq_earlyexit_first_half_single_inference(
                request.json[0])
            result = requests.post('http://edge_inference_container:5001/run_mobile_edge_earlyexit_single_inference_duc_int8_sptq',
                                   json=result, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)
        

@app.route('/run_mobile_single_inference_duc', methods=['GET', 'POST'])
def run_mobile_single_inference_duc():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = duc_single_inference(request.json[0])
            return json.dumps(result)


@app.route('/run_mobile_single_inference_duc_int8_sptq', methods=['GET', 'POST'])
def run_mobile_single_inference_duc_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = duc_int8_sptq_single_inference(request.json[0])
            return json.dumps(result)


@app.route('/run_mobile_earlyexit_single_inference_duc', methods=['GET', 'POST'])
def run_mobile_earlyexit_single_inference_duc():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = duc_earlyexit_single_inference(
                request.json[0])
            return json.dumps(result)


@app.route('/run_mobile_earlyexit_single_inference_duc_int8_sptq', methods=['GET', 'POST'])
def run_mobile_earlyexit_single_inference_duc_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = duc_int8_sptq_earlyexit_single_inference(
                request.json[0])
            return json.dumps(result)


@app.route('/run_edge_single_inference_duc', methods=['GET', 'POST'])
def run_edge_single_inference_duc():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_single_inference_duc',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_single_inference_duc_int8_sptq', methods=['GET', 'POST'])
def run_edge_single_inference_duc_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_single_inference_duc_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_cloud_single_inference_duc', methods=['GET', 'POST'])
def run_cloud_single_inference_duc():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_single_inference_duc',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_cloud_single_inference_duc_int8_sptq', methods=['GET', 'POST'])
def run_cloud_single_inference_duc_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_single_inference_duc_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_earlyexit_single_inference_duc', methods=['GET', 'POST'])
def run_edge_earlyexit_single_inference_duc():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_earlyexit_single_inference_duc',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_earlyexit_single_inference_duc_int8_sptq', methods=['GET', 'POST'])
def run_edge_earlyexit_single_inference_duc_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_earlyexit_single_inference_duc_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_cloud_earlyexit_single_inference_duc', methods=['GET', 'POST'])
def run_cloud_earlyexit_single_inference_duc():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_earlyexit_single_inference_duc',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_cloud_earlyexit_single_inference_duc_int8_sptq', methods=['GET', 'POST'])
def run_cloud_earlyexit_single_inference_duc_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_earlyexit_single_inference_duc_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_cloud_earlyexit_single_inference_duc_int8_sptq', methods=['GET', 'POST'])
def run_edge_cloud_earlyexit_single_inference_duc_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_cloud_earlyexit_single_inference_duc_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_cloud_split_single_inference_duc', methods=['GET', 'POST'])
def run_edge_cloud_split_single_inference_duc():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_cloud_split_single_inference_duc',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_mobile_edge_split_single_inference_duc', methods=['GET', 'POST'])
def run_mobile_edge_split_single_inference_duc():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = duc_split_first_half_single_inference(
                request.json[0])
            result = requests.post('http://edge_inference_container:5001/run_mobile_edge_split_single_inference_duc',
                                   json=result, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_mobile_cloud_split_single_inference_duc', methods=['GET', 'POST'])
def run_mobile_cloud_split_single_inference_duc():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = duc_split_first_half_single_inference(
                request.json[0])
            result = requests.post('http://edge_inference_container:5001/run_mobile_cloud_split_single_inference_duc',
                                   json=result, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_single_inference_fcn', methods=['GET', 'POST'])
def run_edge_single_inference_fcn():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_single_inference_fcn',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_single_inference_resnet', methods=['GET', 'POST'])
def run_edge_single_inference_resnet():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_single_inference_resnet',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_edge_single_inference_resnet_pruned', methods=['GET', 'POST'])
def run_edge_single_inference_resnet_pruned():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_single_inference_resnet_pruned',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_single_inference_resnet_distilled', methods=['GET', 'POST'])
def run_edge_single_inference_resnet_distilled():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_single_inference_resnet_distilled',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_edge_single_inference_resnet_distilled_int8_sptq', methods=['GET', 'POST'])
def run_edge_single_inference_resnet_distilled_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_single_inference_resnet_distilled_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_edge_single_inference_resnet_distilled_int8_qat', methods=['GET', 'POST'])
def run_edge_single_inference_resnet_distilled_int8_qat():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_single_inference_resnet_distilled_int8_qat',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_edge_single_inference_resnext', methods=['GET', 'POST'])
def run_edge_single_inference_resnext():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_single_inference_resnext',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_edge_single_inference_resnext_pruned', methods=['GET', 'POST'])
def run_edge_single_inference_resnext_pruned():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_single_inference_resnext_pruned',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_edge_single_inference_resnext_distilled', methods=['GET', 'POST'])
def run_edge_single_inference_resnext_distilled():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_single_inference_resnext_distilled',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_edge_single_inference_resnext_distilled_int8_sptq', methods=['GET', 'POST'])
def run_edge_single_inference_resnext_distilled_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_single_inference_resnext_distilled_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_edge_single_inference_resnext_distilled_int8_qat', methods=['GET', 'POST'])
def run_edge_single_inference_resnext_distilled_int8_qat():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_single_inference_resnext_distilled_int8_qat',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_earlyexit_single_inference_fcn', methods=['GET', 'POST'])
def run_edge_earlyexit_single_inference_fcn():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_earlyexit_single_inference_fcn',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_earlyexit_single_inference_resnet', methods=['GET', 'POST'])
def run_edge_earlyexit_single_inference_resnet():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_earlyexit_single_inference_resnet',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_earlyexit_single_inference_resnext', methods=['GET', 'POST'])
def run_edge_earlyexit_single_inference_resnext():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_earlyexit_single_inference_resnext',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_earlyexit_single_inference_fcn_int8_sptq', methods=['GET', 'POST'])
def run_edge_earlyexit_single_inference_fcn_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_earlyexit_single_inference_fcn_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_earlyexit_single_inference_resnet_int8_sptq', methods=['GET', 'POST'])
def run_edge_earlyexit_single_inference_resnet_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_earlyexit_single_inference_resnet_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_earlyexit_single_inference_resnext_int8_sptq', methods=['GET', 'POST'])
def run_edge_earlyexit_single_inference_resnext_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_earlyexit_single_inference_resnext_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_cloud_earlyexit_single_inference_fcn_int8_sptq', methods=['GET', 'POST'])
def run_edge_cloud_earlyexit_single_inference_fcn_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_cloud_earlyexit_single_inference_fcn_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_cloud_earlyexit_single_inference_resnet_int8_sptq', methods=['GET', 'POST'])
def run_edge_cloud_earlyexit_single_inference_resnet_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_cloud_earlyexit_single_inference_resnet_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_cloud_earlyexit_single_inference_resnext_int8_sptq', methods=['GET', 'POST'])
def run_edge_cloud_earlyexit_single_inference_resnext_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_cloud_earlyexit_single_inference_resnext_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_cloud_split_single_inference_fcn', methods=['GET', 'POST'])
def run_edge_cloud_split_single_inference_fcn():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_cloud_split_single_inference_fcn',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_cloud_split_single_inference_resnet', methods=['GET', 'POST'])
def run_edge_cloud_split_single_inference_resnet():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_cloud_split_single_inference_resnet',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_cloud_split_single_inference_resnext', methods=['GET', 'POST'])
def run_edge_cloud_split_single_inference_resnext():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_cloud_split_single_inference_resnext',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_mobile_edge_earlyexit_single_inference_fcn_int8_sptq', methods=['GET', 'POST'])
def run_mobile_edge_earlyexit_single_inference_fcn_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = fcn_int8_sptq_earlyexit_first_half_single_inference(
                request.json[0])
            result = [base64.b64encode(data[0]).decode(
                'utf-8'), base64.b64encode(data[1]).decode('utf-8'), data[1].shape]
            result = requests.post('http://edge_inference_container:5001/run_mobile_edge_earlyexit_single_inference_fcn_int8_sptq',
                                   json=result, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_mobile_edge_earlyexit_single_inference_resnet_int8_sptq', methods=['GET', 'POST'])
def run_mobile_edge_earlyexit_single_inference_resnet_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = resnet_int8_sptq_earlyexit_first_half_single_inference(
                request.json[0])
            data = [base64.b64encode(i).decode('utf-8') for i in data]
            result = requests.post('http://edge_inference_container:5001/run_mobile_edge_earlyexit_single_inference_resnet_int8_sptq',
                                   json=data, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_mobile_edge_earlyexit_single_inference_resnext_int8_sptq', methods=['GET', 'POST'])
def run_mobile_edge_earlyexit_single_inference_resnext_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = resnext_int8_sptq_earlyexit_first_half_single_inference(
                request.json[0])
            data = [base64.b64encode(i).decode('utf-8') for i in data]
            result = requests.post('http://edge_inference_container:5001/run_mobile_edge_earlyexit_single_inference_resnext_int8_sptq',
                                   json=data, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_mobile_edge_split_single_inference_fcn', methods=['GET', 'POST'])
def run_mobile_edge_split_single_inference_fcn():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = fcn_split_first_half_single_inference(
                request.json[0])
            result = [base64.b64encode(i).decode('utf-8') for i in data]
            result.append(data[1].shape)
            result = requests.post('http://edge_inference_container:5001/run_mobile_edge_split_single_inference_fcn',
                                   json=result, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_mobile_edge_split_single_inference_resnet', methods=['GET', 'POST'])
def run_mobile_edge_split_single_inference_resnet():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = resnet_split_first_half_single_inference(
                request.json[0])
            data = [base64.b64encode(i).decode('utf-8') for i in data]
            result = requests.post('http://edge_inference_container:5001/run_mobile_edge_split_single_inference_resnet',
                                   json=data, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_mobile_edge_split_single_inference_resnext', methods=['GET', 'POST'])
def run_mobile_edge_split_single_inference_resnext():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = resnext_split_first_half_single_inference(
                request.json[0])
            data = [base64.b64encode(i).decode('utf-8') for i in data]
            result = requests.post('http://edge_inference_container:5001/run_mobile_edge_split_single_inference_resnext',
                                   json=data, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_mobile_cloud_earlyexit_single_inference_fcn_int8_sptq', methods=['GET', 'POST'])
def run_mobile_cloud_earlyexit_single_inference_fcn_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = fcn_int8_sptq_earlyexit_first_half_single_inference(
                request.json[0])
            result = [base64.b64encode(data[0]).decode(
                'utf-8'), base64.b64encode(data[1]).decode('utf-8'), data[1].shape]
            result = requests.post('http://edge_inference_container:5001/run_mobile_cloud_earlyexit_single_inference_fcn_int8_sptq',
                                   json=result, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_mobile_cloud_earlyexit_single_inference_resnet_int8_sptq', methods=['GET', 'POST'])
def run_mobile_cloud_earlyexit_single_inference_resnet_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = resnet_int8_sptq_earlyexit_first_half_single_inference(
                request.json[0])
            data = [base64.b64encode(i).decode('utf-8') for i in data]
            result = requests.post('http://edge_inference_container:5001/run_mobile_cloud_earlyexit_single_inference_resnet_int8_sptq',
                                   json=data, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_mobile_cloud_earlyexit_single_inference_resnext_int8_sptq', methods=['GET', 'POST'])
def run_mobile_cloud_earlyexit_single_inference_resnext_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = resnext_int8_sptq_earlyexit_first_half_single_inference(
                request.json[0])
            data = [base64.b64encode(i).decode('utf-8') for i in data]
            result = requests.post('http://edge_inference_container:5001/run_mobile_cloud_earlyexit_single_inference_resnext_int8_sptq',
                                   json=data, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_mobile_cloud_split_single_inference_fcn', methods=['GET', 'POST'])
def run_mobile_cloud_split_single_inference_fcn():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = fcn_split_first_half_single_inference(
                request.json[0])
            result = [base64.b64encode(i).decode('utf-8') for i in data]
            result.append(data[1].shape)
            result = requests.post('http://edge_inference_container:5001/run_mobile_cloud_split_single_inference_fcn',
                                   json=result, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_mobile_cloud_split_single_inference_resnet', methods=['GET', 'POST'])
def run_mobile_cloud_split_single_inference_resnet():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = resnet_split_first_half_single_inference(
                request.json[0])
            data = [base64.b64encode(i).decode('utf-8') for i in data]
            result = requests.post('http://edge_inference_container:5001/run_mobile_cloud_split_single_inference_resnet',
                                   json=data, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_mobile_cloud_split_single_inference_resnext', methods=['GET', 'POST'])
def run_mobile_cloud_split_single_inference_resnext():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = resnext_split_first_half_single_inference(
                request.json[0])
            data = [base64.b64encode(i).decode('utf-8') for i in data]
            result = requests.post('http://edge_inference_container:5001/run_mobile_cloud_split_single_inference_resnext',
                                   json=data, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_single_inference_fcn_int8_sptq', methods=['GET', 'POST'])
def run_edge_single_inference_fcn_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_single_inference_fcn_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_single_inference_resnet_int8_sptq', methods=['GET', 'POST'])
def run_edge_single_inference_resnet_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_single_inference_resnet_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_edge_single_inference_resnet_int8_qat', methods=['GET', 'POST'])
def run_edge_single_inference_resnet_int8_qat():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_single_inference_resnet_int8_qat',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)



@app.route('/run_edge_single_inference_resnext_int8_sptq', methods=['GET', 'POST'])
def run_edge_single_inference_resnext_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_single_inference_resnext_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_edge_single_inference_resnext_int8_qat', methods=['GET', 'POST'])
def run_edge_single_inference_resnext_int8_qat():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_edge_single_inference_resnext_int8_qat',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_cloud_single_inference_fcn', methods=['GET', 'POST'])
def run_cloud_single_inference_fcn():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_single_inference_fcn',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_cloud_single_inference_resnet', methods=['GET', 'POST'])
def run_cloud_single_inference_resnet():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_single_inference_resnet',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_cloud_single_inference_resnet_pruned', methods=['GET', 'POST'])
def run_cloud_single_inference_resnet_pruned():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_single_inference_resnet_pruned',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_cloud_single_inference_resnet_distilled', methods=['GET', 'POST'])
def run_cloud_single_inference_resnet_distilled():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_single_inference_resnet_distilled',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_cloud_single_inference_resnet_distilled_int8_sptq', methods=['GET', 'POST'])
def run_cloud_single_inference_resnet_distilled_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_single_inference_resnet_distilled_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_cloud_single_inference_resnet_distilled_int8_qat', methods=['GET', 'POST'])
def run_cloud_single_inference_resnet_distilled_int8_qat():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_single_inference_resnet_distilled_int8_qat',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_cloud_single_inference_resnext', methods=['GET', 'POST'])
def run_cloud_single_inference_resnext():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_single_inference_resnext',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_cloud_single_inference_resnext_pruned', methods=['GET', 'POST'])
def run_cloud_single_inference_resnext_pruned():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_single_inference_resnext_pruned',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_cloud_single_inference_resnext_distilled', methods=['GET', 'POST'])
def run_cloud_single_inference_resnext_distilled():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_single_inference_resnext_distilled',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_cloud_single_inference_resnext_distilled_int8_sptq', methods=['GET', 'POST'])
def run_cloud_single_inference_resnext_distilled_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_single_inference_resnext_distilled_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_cloud_single_inference_resnext_distilled_int8_qat', methods=['GET', 'POST'])
def run_cloud_single_inference_resnext_distilled_int8_qat():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_single_inference_resnext_distilled_int8_qat',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_cloud_earlyexit_single_inference_fcn', methods=['GET', 'POST'])
def run_cloud_earlyexit_single_inference_fcn():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_earlyexit_single_inference_fcn',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_cloud_earlyexit_single_inference_resnet', methods=['GET', 'POST'])
def run_cloud_earlyexit_single_inference_resnet():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_earlyexit_single_inference_resnet',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_cloud_earlyexit_single_inference_resnext', methods=['GET', 'POST'])
def run_cloud_earlyexit_single_inference_resnext():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_earlyexit_single_inference_resnext',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_cloud_earlyexit_single_inference_fcn_int8_sptq', methods=['GET', 'POST'])
def run_cloud_earlyexit_single_inference_fcn_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_earlyexit_single_inference_fcn_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_cloud_earlyexit_single_inference_resnet_int8_sptq', methods=['GET', 'POST'])
def run_cloud_earlyexit_single_inference_resnet_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_earlyexit_single_inference_resnet_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_cloud_earlyexit_single_inference_resnext_int8_sptq', methods=['GET', 'POST'])
def run_cloud_earlyexit_single_inference_resnext_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_earlyexit_single_inference_resnext_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)



@app.route('/run_cloud_single_inference_fcn_int8_sptq', methods=['GET', 'POST'])
def run_cloud_single_inference_fcn_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_single_inference_fcn_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_cloud_single_inference_resnet_int8_sptq', methods=['GET', 'POST'])
def run_cloud_single_inference_resnet_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_single_inference_resnet_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_cloud_single_inference_resnet_int8_qat', methods=['GET', 'POST'])
def run_cloud_single_inference_resnet_int8_qat():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_single_inference_resnet_int8_qat',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_cloud_single_inference_resnext_int8_sptq', methods=['GET', 'POST'])
def run_cloud_single_inference_resnext_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_single_inference_resnext_int8_sptq',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)


@app.route('/run_cloud_single_inference_resnext_int8_qat', methods=['GET', 'POST'])
def run_cloud_single_inference_resnext_int8_qat():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = requests.post('http://edge_inference_container:5001/run_cloud_single_inference_resnext_int8_qat',
                                   json=request.json, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
            return json.dumps(result)

@app.route('/run_mobile_single_inference_fcn', methods=['GET', 'POST'])
def run_mobile_single_inference_fcn():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = fcn_single_inference(request.json[0])
            return json.dumps(result)


@app.route('/run_mobile_single_inference_resnet', methods=['GET', 'POST'])
def run_mobile_single_inference_resnet():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnet_single_inference(request.json[0])
            return json.dumps(result)

@app.route('/run_mobile_single_inference_resnet_int8_sptq', methods=['GET', 'POST'])
def run_mobile_single_inference_resnet_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnet_int8_sptq_single_inference(request.json[0])
            return json.dumps(result)


@app.route('/run_mobile_single_inference_resnet_int8_qat', methods=['GET', 'POST'])
def run_mobile_single_inference_resnet_int8_qat():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnet_int8_qat_single_inference(request.json[0])
            return json.dumps(result)

@app.route('/run_mobile_single_inference_resnet_pruned', methods=['GET', 'POST'])
def run_mobile_single_inference_resnet_pruned():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnet_pruned_single_inference(request.json[0])
            return json.dumps(result)

@app.route('/run_mobile_single_inference_resnet_distilled', methods=['GET', 'POST'])
def run_mobile_single_inference_resnet_distilled():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnet_distilled_single_inference(request.json[0])
            return json.dumps(result)

@app.route('/run_mobile_single_inference_resnet_distilled_int8_sptq', methods=['GET', 'POST'])
def run_mobile_single_inference_resnet_distilled_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnet_distilled_int8_sptq_single_inference(request.json[0])
            return json.dumps(result)

@app.route('/run_mobile_single_inference_resnet_distilled_int8_qat', methods=['GET', 'POST'])
def run_mobile_single_inference_resnet_distilled_int8_qat():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnet_distilled_int8_qat_single_inference(request.json[0])
            return json.dumps(result)

@app.route('/run_mobile_single_inference_resnext', methods=['GET', 'POST'])
def run_mobile_single_inference_resnext():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnext_single_inference(request.json[0])
            return json.dumps(result)

@app.route('/run_mobile_single_inference_resnext_int8_sptq', methods=['GET', 'POST'])
def run_mobile_single_inference_resnext_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnext_int8_sptq_single_inference(request.json[0])
            return json.dumps(result)

@app.route('/run_mobile_single_inference_resnext_int8_qat', methods=['GET', 'POST'])
def run_mobile_single_inference_resnext_int8_qat():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnext_int8_qat_single_inference(request.json[0])
            return json.dumps(result)

@app.route('/run_mobile_single_inference_resnext_pruned', methods=['GET', 'POST'])
def run_mobile_single_inference_resnext_pruned():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnext_pruned_single_inference(request.json[0])
            return json.dumps(result)

@app.route('/run_mobile_single_inference_resnext_distilled', methods=['GET', 'POST'])
def run_mobile_single_inference_resnext_distilled():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnext_distilled_single_inference(request.json[0])
            return json.dumps(result)

@app.route('/run_mobile_single_inference_resnext_distilled_int8_sptq', methods=['GET', 'POST'])
def run_mobile_single_inference_resnext_distilled_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnext_distilled_int8_sptq_single_inference(request.json[0])
            return json.dumps(result)


@app.route('/run_mobile_single_inference_resnext_distilled_int8_qat', methods=['GET', 'POST'])
def run_mobile_single_inference_resnext_distilled_int8_qat():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnext_distilled_int8_qat_single_inference(request.json[0])
            return json.dumps(result)


@app.route('/run_mobile_earlyexit_single_inference_fcn_int8_sptq', methods=['GET', 'POST'])
def run_mobile_earlyexit_single_inference_fcn_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = fcn_int8_sptq_earlyexit_single_inference(
                request.json[0])
            return json.dumps(result)


@app.route('/run_mobile_earlyexit_single_inference_resnet_int8_sptq', methods=['GET', 'POST'])
def run_mobile_earlyexit_single_inference_resnet_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnet_int8_sptq_earlyexit_single_inference(
                request.json[0])
            return json.dumps(result)


@app.route('/run_mobile_earlyexit_single_inference_resnext_int8_sptq', methods=['GET', 'POST'])
def run_mobile_earlyexit_single_inference_resnext_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnext_int8_sptq_earlyexit_single_inference(
                request.json[0])
            return json.dumps(result)


@app.route('/run_mobile_earlyexit_single_inference_fcn', methods=['GET', 'POST'])
def run_mobile_earlyexit_single_inference_fcn():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = fcn_earlyexit_single_inference(request.json[0])
            return json.dumps(result)


@app.route('/run_mobile_earlyexit_single_inference_resnet', methods=['GET', 'POST'])
def run_mobile_earlyexit_single_inference_resnet():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnet_earlyexit_single_inference(request.json[0])
            return json.dumps(result)


@app.route('/run_mobile_earlyexit_single_inference_resnext', methods=['GET', 'POST'])
def run_mobile_earlyexit_single_inference_resnext():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = resnext_earlyexit_single_inference(
                request.json[0])
            return json.dumps(result)



@app.route('/run_mobile_single_inference_fcn_int8_sptq', methods=['GET', 'POST'])
def run_mobile_single_inference_fcn_int8_sptq():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            result = fcn_int8_sptq_single_inference(request.json[0])
            return json.dumps(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
