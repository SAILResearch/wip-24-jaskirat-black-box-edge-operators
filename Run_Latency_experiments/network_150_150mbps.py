import base64
from io import BytesIO
import os
import json
import requests
from timeit import default_timer as timer
from subprocess import Popen, PIPE
import time

imagenet_dataset = ['ILSVRC2012_val_00033687.JPEG']
coco_dataset= ['000000163682.jpg']
cityscapes_dataset= ['frankfurt_000001_065850_leftImg8bit.png']

def restart_mobile_container(container_name):
    curl_command='docker restart {}'.format(container_name)
    process = Popen(curl_command, shell=True, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    if error:
        print("Error: {}".format(error.decode('utf-8')))
    else:
        curl_command = 'docker exec -d {} bash -c "chmod +x ./network_150mbps.sh;./network_150mbps.sh"'.format(container_name)
        process = Popen(curl_command, shell=True, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if error:
            print("Error: {}".format(error.decode('utf-8')))
        else:
            print("Container {} restarted successfully and Network script successfully executed.".format(container_name))

def restart_edge_container(container_name):
    curl_command='docker restart {}'.format(container_name)
    process = Popen(curl_command, shell=True, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    if error:
        print("Error: {}".format(error.decode('utf-8')))
    else:
        curl_command = 'docker exec -d {} bash -c "chmod +x ./network_150mbps.sh;./network_150mbps.sh"'.format(container_name)
        process = Popen(curl_command, shell=True, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if error:
            print("Error: {}".format(error.decode('utf-8')))
        else:
            print("Container {} restarted successfully and Network script successfully executed.".format(container_name))

def stop_mobile_edge_container(container_name):
    curl_command='docker stop {}'.format(container_name)
    process = Popen(curl_command, shell=True, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    if error:
        print("Error: {}".format(error.decode('utf-8')))
    else:
        print("Container {} stopped successfully.".format(container_name))

def restart_cloud_container(container_name):
    # require ssh tunneling for connecting to external server using following command: ssh -o ServerAliveInterval=60 -f -N -L :8000:localhost:8000 username@servername
    curl_command = 'curl -X POST -d "container_name={}" http://localhost:8000/restart_container_150mbps'.format(container_name)
    process = Popen(curl_command, shell=True, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    print(output)
    
def stop_cloud_container(container_name):
    curl_command = 'curl -X POST -d "container_name={}" http://localhost:8000/stop_container'.format(container_name)
    process = Popen(curl_command, shell=True, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    print(output)

def construct_url_for_identity(tier,subject):
    base_url = 'http://0.0.0.0:5000/run_{}_single_inference_{}'
    results_file= '{}_{}_150mbps_150mbps_results.txt'
    return base_url.format(tier,subject), results_file.format(tier, subject)

def construct_url_for_partition(tier,subject):
    base_url = 'http://0.0.0.0:5000/run_{}_split_single_inference_{}'
    results_file= '{}_{}_150mbps_150mbps_results.txt'
    return base_url.format(tier,subject), results_file.format(tier, subject)

def construct_url_for_earlyexit(tier,subject):
    base_url = 'http://0.0.0.0:5000/run_{}_earlyexit_single_inference_{}'
    results_file= '{}_{}_earlyexit_150mbps_150mbps_results.txt'
    return base_url.format(tier,subject), results_file.format(tier, subject)

def construct_url_for_sptq(tier,subject):
    base_url = 'http://0.0.0.0:5000/run_{}_single_inference_{}_int8_sptq'
    results_file= '{}_{}_int8_sptq_150mbps_150mbps_results.txt'
    return base_url.format(tier,subject), results_file.format(tier, subject)

def construct_url_for_sptq_earlyexit(tier,subject):
    base_url = 'http://0.0.0.0:5000/run_{}_earlyexit_single_inference_{}_int8_sptq'
    results_file= '{}_{}_earlyexit_int8_sptq_150mbps_150mbps_results.txt'
    return base_url.format(tier,subject), results_file.format(tier, subject)

subjects=['resnet','resnext','fcn','duc']
single_tiers=['cloud']
multi_tiers=['mobile_cloud','edge_cloud']
operators=['identity','sptq','earlyexit','sptq earlyexit']

def initial_restart_of_containers():
    restart_mobile_container('mobile_inference_container')
    restart_edge_container('edge_inference_container')
    restart_cloud_container('cloud_inference_container')
    time.sleep(20)

def restart_containers(tier):
    if tier=='mobile':
        restart_mobile_container('mobile_inference_container')
    if tier=='edge':
        restart_mobile_container('mobile_inference_container')
        restart_edge_container('edge_inference_container')
    if tier=='cloud':
        restart_mobile_container('mobile_inference_container')
        restart_edge_container('edge_inference_container')
        restart_cloud_container('cloud_inference_container') 
    if tier=='mobile_edge':
        restart_mobile_container('mobile_inference_container')
        restart_edge_container('edge_inference_container')
    if tier=='edge_cloud':
        restart_mobile_container('mobile_inference_container')
        restart_edge_container('edge_inference_container')
        restart_cloud_container('cloud_inference_container')
    if tier=='mobile_cloud':
        restart_mobile_container('mobile_inference_container')
        restart_edge_container('edge_inference_container')
        restart_cloud_container('cloud_inference_container')
    time.sleep(20)

def shutdown_all_containers():
    stop_mobile_edge_container('mobile_inference_container')
    stop_mobile_edge_container('edge_inference_container')
    stop_cloud_container('cloud_inference_container')

initial_restart_of_containers()
for subject in subjects:
    if subject == "resnet" or subject == "resnext":
        for operator in operators:
            if operator =="identity":
                for single_tier in single_tiers:
                    url, result_file=construct_url_for_identity(single_tier, subject)
                    with open(result_file,'w') as fd:
                        fd.write('Experiment Results\n')
                    for i in range(6):
                        print("Experiment:",i+1)
                        for img in imagenet_dataset:
                            with open(os.path.join('imagenet_100_images', img), "rb") as image_file:
                                im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                            start = timer()
                            result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                            inference_time = timer() - start
                            print(result," Inference Time(s): ",inference_time)
                            with open(result_file,'a') as fd:
                                fd.write(str(inference_time)+'\n')
                    restart_containers(single_tier)
                for multi_tier in multi_tiers:
                    url, result_file=construct_url_for_partition(multi_tier, subject)
                    with open(result_file,'w') as fd:
                        fd.write('Experiment Results\n')
                    for i in range(6):
                        print("Experiment:",i+1)
                        for img in imagenet_dataset:
                            with open(os.path.join('imagenet_100_images', img), "rb") as image_file:
                                im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                            start = timer()
                            result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                            inference_time = timer() - start
                            print(result," Inference Time(s): ",inference_time)
                            with open(result_file,'a') as fd:
                                fd.write(str(inference_time)+'\n')
                    restart_containers(multi_tier)
            if operator =="sptq":
                for single_tier in single_tiers:
                    url, result_file=construct_url_for_sptq(single_tier, subject)
                    with open(result_file,'w') as fd:
                        fd.write('Experiment Results\n')
                    for i in range(6):
                        print("Experiment:",i+1)
                        for img in imagenet_dataset:
                            with open(os.path.join('imagenet_100_images', img), "rb") as image_file:
                                im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                            start = timer()
                            result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                            inference_time = timer() - start
                            print(result," Inference Time(s): ",inference_time)
                            with open(result_file,'a') as fd:
                                fd.write(str(inference_time)+'\n')
                    restart_containers(single_tier)
            if operator =="earlyexit":
                for single_tier in single_tiers:
                    url, result_file=construct_url_for_earlyexit(single_tier, subject)
                    with open(result_file,'w') as fd:
                        fd.write('Experiment Results\n')
                    for i in range(6):
                        print("Experiment:",i+1)
                        for img in imagenet_dataset:
                            with open(os.path.join('imagenet_100_images', img), "rb") as image_file:
                                im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                            start = timer()
                            result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                            inference_time = timer() - start
                            print(result," Inference Time(s): ",inference_time)
                            with open(result_file,'a') as fd:
                                fd.write(str(inference_time)+'\n')
                    restart_containers(single_tier)
            if operator =="sptq earlyexit":
                for single_tier in single_tiers:
                    url, result_file=construct_url_for_sptq_earlyexit(single_tier, subject)
                    with open(result_file,'w') as fd:
                        fd.write('Experiment Results\n')
                    for i in range(6):
                        print("Experiment:",i+1)
                        for img in imagenet_dataset:
                            with open(os.path.join('imagenet_100_images', img), "rb") as image_file:
                                im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                            start = timer()
                            result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                            inference_time = timer() - start
                            print(result," Inference Time(s): ",inference_time)
                            with open(result_file,'a') as fd:
                                fd.write(str(inference_time)+'\n')
                    restart_containers(single_tier)
                for multi_tier in multi_tiers:
                    url, result_file=construct_url_for_sptq_earlyexit(multi_tier, subject)
                    with open(result_file,'w') as fd:
                        fd.write('Experiment Results\n')
                    for i in range(6):
                        print("Experiment:",i+1)
                        for img in imagenet_dataset:
                            with open(os.path.join('imagenet_100_images', img), "rb") as image_file:
                                im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                            start = timer()
                            result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                            inference_time = timer() - start
                            print(result," Inference Time(s): ",inference_time)
                            with open(result_file,'a') as fd:
                                fd.write(str(inference_time)+'\n')
                    restart_containers(multi_tier)
    if subject == "fcn":
        for operator in operators:
            if operator =="identity":
                for single_tier in single_tiers:
                    url, result_file=construct_url_for_identity(single_tier, subject)
                    with open(result_file,'w') as fd:
                        fd.write('Experiment Results\n')
                    for i in range(6):
                        print("Experiment:",i+1)
                        for img in coco_dataset:
                            with open(os.path.join('coco_100_images', img), "rb") as image_file:
                                im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                            start = timer()
                            result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                            inference_time = timer() - start
                            print(result," Inference Time(s): ",inference_time)
                            with open(result_file,'a') as fd:
                                fd.write(str(inference_time)+'\n')
                    restart_containers(single_tier)
                for multi_tier in multi_tiers:
                    url, result_file=construct_url_for_partition(multi_tier, subject)
                    with open(result_file,'w') as fd:
                        fd.write('Experiment Results\n')
                    for i in range(6):
                        print("Experiment:",i+1)
                        for img in coco_dataset:
                            with open(os.path.join('coco_100_images', img), "rb") as image_file:
                                im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                            start = timer()
                            result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                            inference_time = timer() - start
                            print(result," Inference Time(s): ",inference_time)
                            with open(result_file,'a') as fd:
                                fd.write(str(inference_time)+'\n')
                    restart_containers(multi_tier)
            if operator =="sptq":
                for single_tier in single_tiers:
                    url, result_file=construct_url_for_sptq(single_tier, subject)
                    with open(result_file,'w') as fd:
                        fd.write('Experiment Results\n')
                    for i in range(6):
                        print("Experiment:",i+1)
                        for img in coco_dataset:
                            with open(os.path.join('coco_100_images', img), "rb") as image_file:
                                im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                            start = timer()
                            result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                            inference_time = timer() - start
                            print(result," Inference Time(s): ",inference_time)
                            with open(result_file,'a') as fd:
                                fd.write(str(inference_time)+'\n')
                    restart_containers(single_tier)
            if operator =="earlyexit":
                for single_tier in single_tiers:
                    url, result_file=construct_url_for_earlyexit(single_tier, subject)
                    with open(result_file,'w') as fd:
                        fd.write('Experiment Results\n')
                    for i in range(6):
                        print("Experiment:",i+1)
                        for img in coco_dataset:
                            with open(os.path.join('coco_100_images', img), "rb") as image_file:
                                im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                            start = timer()
                            result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                            inference_time = timer() - start
                            print(result," Inference Time(s): ",inference_time)
                            with open(result_file,'a') as fd:
                                fd.write(str(inference_time)+'\n')
                    restart_containers(single_tier)
            if operator =="sptq earlyexit":
                for single_tier in single_tiers:
                    url, result_file=construct_url_for_sptq_earlyexit(single_tier, subject)
                    with open(result_file,'w') as fd:
                        fd.write('Experiment Results\n')
                    for i in range(6):
                        print("Experiment:",i+1)
                        for img in coco_dataset:
                            with open(os.path.join('coco_100_images', img), "rb") as image_file:
                                im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                            start = timer()
                            result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                            inference_time = timer() - start
                            print(result," Inference Time(s): ",inference_time)
                            with open(result_file,'a') as fd:
                                fd.write(str(inference_time)+'\n')
                    restart_containers(single_tier)
                for multi_tier in multi_tiers:
                    url, result_file=construct_url_for_sptq_earlyexit(multi_tier, subject)
                    with open(result_file,'w') as fd:
                        fd.write('Experiment Results\n')
                    for i in range(6):
                        print("Experiment:",i+1)
                        for img in coco_dataset:
                            with open(os.path.join('coco_100_images', img), "rb") as image_file:
                                im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                            start = timer()
                            result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                            inference_time = timer() - start
                            print(result," Inference Time(s): ",inference_time)
                            with open(result_file,'a') as fd:
                                fd.write(str(inference_time)+'\n')
                    restart_containers(multi_tier)
    if subject == "duc":
        for operator in operators:
            if operator =="identity":
                for single_tier in single_tiers:
                    url, result_file=construct_url_for_identity(single_tier, subject)
                    with open(result_file,'w') as fd:
                        fd.write('Experiment Results\n')
                    for i in range(6):
                        print("Experiment:",i+1)
                        for img in cityscapes_dataset:
                            with open(os.path.join('cityscapes_100_images', img), "rb") as image_file:
                                im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                            start = timer()
                            result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                            inference_time = timer() - start
                            print(result," Inference Time(s): ",inference_time)
                            with open(result_file,'a') as fd:
                                fd.write(str(inference_time)+'\n')
                    restart_containers(single_tier)
                for multi_tier in multi_tiers:
                    url, result_file=construct_url_for_partition(multi_tier, subject)
                    with open(result_file,'w') as fd:
                        fd.write('Experiment Results\n')
                    for i in range(6):
                        print("Experiment:",i+1)
                        for img in cityscapes_dataset:
                            with open(os.path.join('cityscapes_100_images', img), "rb") as image_file:
                                im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                            start = timer()
                            result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                            inference_time = timer() - start
                            print(result," Inference Time(s): ",inference_time)
                            with open(result_file,'a') as fd:
                                fd.write(str(inference_time)+'\n')
                    restart_containers(multi_tier)
            if operator =="sptq":
                for single_tier in single_tiers:
                    url, result_file=construct_url_for_sptq(single_tier, subject)
                    with open(result_file,'w') as fd:
                        fd.write('Experiment Results\n')
                    for i in range(6):
                        print("Experiment:",i+1)
                        for img in cityscapes_dataset:
                            with open(os.path.join('cityscapes_100_images', img), "rb") as image_file:
                                im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                            start = timer()
                            result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                            inference_time = timer() - start
                            print(result," Inference Time(s): ",inference_time)
                            with open(result_file,'a') as fd:
                                fd.write(str(inference_time)+'\n')
                    restart_containers(single_tier)
            if operator =="earlyexit":
                for single_tier in single_tiers:
                    url, result_file=construct_url_for_earlyexit(single_tier, subject)
                    with open(result_file,'w') as fd:
                        fd.write('Experiment Results\n')
                    for i in range(6):
                        print("Experiment:",i+1)
                        for img in cityscapes_dataset:
                            with open(os.path.join('cityscapes_100_images', img), "rb") as image_file:
                                im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                            start = timer()
                            result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                            inference_time = timer() - start
                            print(result," Inference Time(s): ",inference_time)
                            with open(result_file,'a') as fd:
                                fd.write(str(inference_time)+'\n')
                    restart_containers(single_tier)
            if operator =="sptq earlyexit":
                for single_tier in single_tiers:
                    url, result_file=construct_url_for_sptq_earlyexit(single_tier, subject)
                    with open(result_file,'w') as fd:
                        fd.write('Experiment Results\n')
                    for i in range(6):
                        print("Experiment:",i+1)
                        for img in cityscapes_dataset:
                            with open(os.path.join('cityscapes_100_images', img), "rb") as image_file:
                                im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                            start = timer()
                            result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                            inference_time = timer() - start
                            print(result," Inference Time(s): ",inference_time)
                            with open(result_file,'a') as fd:
                                fd.write(str(inference_time)+'\n')
                    restart_containers(single_tier)
                for multi_tier in multi_tiers:
                    url, result_file=construct_url_for_sptq_earlyexit(multi_tier, subject)
                    with open(result_file,'w') as fd:
                        fd.write('Experiment Results\n')
                    for i in range(6):
                        print("Experiment:",i+1)
                        for img in cityscapes_dataset:
                            with open(os.path.join('cityscapes_100_images', img), "rb") as image_file:
                                im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                            start = timer()
                            result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                            inference_time = timer() - start
                            print(result," Inference Time(s): ",inference_time)
                            with open(result_file,'a') as fd:
                                fd.write(str(inference_time)+'\n')
                    restart_containers(multi_tier)          

shutdown_all_containers()
