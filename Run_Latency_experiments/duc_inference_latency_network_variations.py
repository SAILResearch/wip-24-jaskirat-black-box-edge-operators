import base64
from io import BytesIO
import os
import json
import requests
from timeit import default_timer as timer
from subprocess import Popen, PIPE
import time
dataset = ['frankfurt_000001_065850_leftImg8bit.png']
from datetime import datetime

def restart_mobile_edge_container(container_name,mobile_edge_bandwidth):
    curl_command='docker restart {}'.format(container_name)
    process = Popen(curl_command, shell=True, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    if error:
        print("Error: {}".format(error.decode('utf-8')))
    else:
        curl_command = 'docker exec -d {} bash -c "chmod +x ./network_{}mbps.sh;./network_{}mbps.sh"'.format(container_name,mobile_edge_bandwidth,mobile_edge_bandwidth)
        process = Popen(curl_command, shell=True, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if error:
            print("Error: {}".format(error.decode('utf-8')))
        else:
            print("Container {} restarted successfully and Network script successfully executed.".format(container_name))

def restart_edge_container(container_name,mobile_edge_bandwidth,edge_cloud_bandwidth):
    curl_command='docker restart {}'.format(container_name)
    process = Popen(curl_command, shell=True, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    if error:
        print("Error: {}".format(error.decode('utf-8')))
    else:
        curl_command = 'docker exec -d {} bash -c "chmod +x ./network_{}_{}mbps.sh;./network_{}_{}mbps.sh"'.format(container_name,mobile_edge_bandwidth,edge_cloud_bandwidth,mobile_edge_bandwidth,edge_cloud_bandwidth)
        process = Popen(curl_command, shell=True, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if error:
            print("Error: {}".format(error.decode('utf-8')))
        else:
             print("Container {} restarted successfully.".format(container_name))

def stop_mobile_edge_container(container_name):
    curl_command='docker stop {}'.format(container_name)
    process = Popen(curl_command, shell=True, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    if error:
        print("Error: {}".format(error.decode('utf-8')))
    else:
        print("Container {} stopped successfully.".format(container_name))

def restart_cloud_container(container_name,edge_cloud_bandwidth):
    curl_command = 'curl -X POST -d "container_name={}" http://localhost:8000/restart_container_{}mbps'.format(container_name,edge_cloud_bandwidth)
    process = Popen(curl_command, shell=True, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    print(output)

def stop_cloud_container(container_name):
    curl_command = 'curl -X POST -d "container_name={}" http://localhost:8000/stop_container'.format(container_name)
    process = Popen(curl_command, shell=True, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    print(output)

def construct_url_for_identity(tier,subject,mobile_edge_bandwidth, edge_cloud_bandwidth):
    base_url = 'http://0.0.0.0:5000/run_{}_single_inference_{}'
    results_file= '{}_{}_{}_{}_results.txt'
    return base_url.format(tier,subject), results_file.format(tier, subject, mobile_edge_bandwidth, edge_cloud_bandwidth)

def construct_url_for_partition(tier,subject,mobile_edge_bandwidth, edge_cloud_bandwidth):
    base_url = 'http://0.0.0.0:5000/run_{}_split_single_inference_{}'
    results_file= '{}_{}_{}_{}_results.txt'
    return base_url.format(tier,subject), results_file.format(tier, subject, mobile_edge_bandwidth,edge_cloud_bandwidth)

def construct_url_for_earlyexit(tier,subject,mobile_edge_bandwidth, edge_cloud_bandwidth):
    base_url = 'http://0.0.0.0:5000/run_{}_earlyexit2_single_inference_{}'
    results_file= '{}_{}_earlyexit_{}_{}_results.txt'
    return base_url.format(tier,subject), results_file.format(tier, subject, mobile_edge_bandwidth, edge_cloud_bandwidth)

def construct_url_for_sptq(tier,subject,mobile_edge_bandwidth, edge_cloud_bandwidth):
    base_url = 'http://0.0.0.0:5000/run_{}_single_inference_{}_int8_sptq'
    results_file= '{}_{}_int8_sptq_{}_{}_results.txt'
    return base_url.format(tier,subject), results_file.format(tier, subject, mobile_edge_bandwidth, edge_cloud_bandwidth)

def construct_url_for_sptq_partition(tier,subject,mobile_edge_bandwidth, edge_cloud_bandwidth):
    base_url = 'http://0.0.0.0:5000/run_{}_split_single_inference_{}_int8_sptq'
    results_file= '{}_{}_int8_sptq_{}_{}_results.txt'
    return base_url.format(tier,subject), results_file.format(tier, subject, mobile_edge_bandwidth, edge_cloud_bandwidth)

def construct_url_for_sptq_earlyexit(tier,subject,mobile_edge_bandwidth, edge_cloud_bandwidth):
    base_url = 'http://0.0.0.0:5000/run_{}_earlyexit2_single_inference_{}_int8_sptq'
    results_file= '{}_{}_earlyexit_int8_sptq_{}_{}_results.txt'
    return base_url.format(tier,subject), results_file.format(tier, subject, mobile_edge_bandwidth, edge_cloud_bandwidth)

single_tiers=['mobile','edge','cloud']
multi_tiers=['mobile_edge','edge_cloud','mobile_cloud']
operators=['identity','sptq','earlyexit','sptq earlyexit']
subjects=['duc']

mobile_edge_bandwidths=[10,50,100,150,200]
edge_cloud_bandwidths=[10,50,100,150,200]

def restart_containers(tier,mobile_edge_bandwidth,edge_cloud_bandwidth):
    if tier=='mobile':
        restart_mobile_edge_container('mobile_inference_container',mobile_edge_bandwidth)
    if tier=='edge':
        restart_mobile_edge_container('mobile_inference_container',mobile_edge_bandwidth)
        restart_mobile_edge_container('edge_inference_container',mobile_edge_bandwidth)
    if tier=='cloud':
        restart_mobile_edge_container('mobile_inference_container',mobile_edge_bandwidth)
        restart_edge_container('edge_inference_container',mobile_edge_bandwidth,edge_cloud_bandwidth)
        restart_cloud_container('cloud_inference_container',edge_cloud_bandwidth)
    if tier=='mobile_edge':
        restart_mobile_edge_container('mobile_inference_container',mobile_edge_bandwidth)
        restart_mobile_edge_container('edge_inference_container',mobile_edge_bandwidth)
    if tier=='edge_cloud':
        restart_mobile_edge_container('mobile_inference_container',mobile_edge_bandwidth)
        restart_edge_container('edge_inference_container',mobile_edge_bandwidth,edge_cloud_bandwidth)
        restart_cloud_container('cloud_inference_container',edge_cloud_bandwidth)
    if tier=='mobile_cloud':
        restart_mobile_edge_container('mobile_inference_container',mobile_edge_bandwidth)
        restart_edge_container('edge_inference_container',mobile_edge_bandwidth,edge_cloud_bandwidth)
        restart_cloud_container('cloud_inference_container',edge_cloud_bandwidth)
    time.sleep(20)

def shutdown_all_containers():
    stop_mobile_edge_container('mobile_inference_container')
    stop_mobile_edge_container('edge_inference_container')
    stop_cloud_container('cloud_inference_container')

def initial_restart_of_containers():
    restart_mobile_edge_container('mobile_inference_container', 200)
    restart_mobile_edge_container('edge_inference_container', 200)
    restart_cloud_container('cloud_inference_container', 200)
    time.sleep(20)

initial_restart_of_containers()

for operator in operators:
    if operator =="identity":
        for subject in subjects:
            for single_tier in single_tiers:
                if single_tier == 'mobile' or single_tier == 'edge':
                    for mobile_edge_bandwidth in mobile_edge_bandwidths:
                        url, result_file=construct_url_for_identity(single_tier, subject, mobile_edge_bandwidth, '')
                        with open(result_file,'w') as fd:
                            fd.write('Experiment Results\n')
                        for i in range(6):
                            print("Experiment:",i+1)
                            for img in dataset:
                                with open(os.path.join('cityscapes_100_images', img), "rb") as image_file:
                                    im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                                start = timer()
                                result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                                inference_time = timer() - start
                                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                print(result, " Inference Time(s): ", inference_time, " Timestamp: ", timestamp)
                                with open(result_file,'a') as fd:
                                    fd.write("{}, {}\n".format(timestamp, inference_time))
                        restart_containers(single_tier,mobile_edge_bandwidth,'')
                
                if single_tier == 'cloud':
                    for mobile_edge_bandwidth in mobile_edge_bandwidths:
                        for edge_cloud_bandwidth in edge_cloud_bandwidths:
                            url, result_file=construct_url_for_identity(single_tier, subject, mobile_edge_bandwidth, edge_cloud_bandwidth)
                            with open(result_file,'w') as fd:
                                fd.write('Experiment Results\n')
                            for i in range(6):
                                print("Experiment:",i+1)
                                for img in dataset:
                                    with open(os.path.join('cityscapes_100_images', img), "rb") as image_file:
                                        im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                                    start = timer()
                                    result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                                    inference_time = timer() - start
                                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                    print(result, " Inference Time(s): ", inference_time, " Timestamp: ", timestamp)
                                    with open(result_file,'a') as fd:
                                        fd.write("{}, {}\n".format(timestamp, inference_time))
                            restart_containers(single_tier,mobile_edge_bandwidth,edge_cloud_bandwidth)

            for multi_tier in multi_tiers:
                if multi_tier == 'edge_cloud' or multi_tier == 'mobile_cloud':
                    for mobile_edge_bandwidth in mobile_edge_bandwidths:
                        for edge_cloud_bandwidth in edge_cloud_bandwidths:
                            url, result_file=construct_url_for_partition(multi_tier, subject, mobile_edge_bandwidth, edge_cloud_bandwidth)
                            with open(result_file,'w') as fd:
                                fd.write('Experiment Results\n')
                            for i in range(6):
                                print("Experiment:",i+1)
                                for img in dataset:
                                    with open(os.path.join('cityscapes_100_images', img), "rb") as image_file:
                                        im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                                    start = timer()
                                    result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                                    inference_time = timer() - start
                                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                    print(result, " Inference Time(s): ", inference_time, " Timestamp: ", timestamp)
                                    with open(result_file,'a') as fd:
                                        fd.write("{}, {}\n".format(timestamp, inference_time))
                            restart_containers(multi_tier,mobile_edge_bandwidth,edge_cloud_bandwidth)

                if multi_tier == 'mobile_edge':
                    for mobile_edge_bandwidth in mobile_edge_bandwidths:
                        url, result_file=construct_url_for_partition(multi_tier, subject, mobile_edge_bandwidth, '')
                        with open(result_file,'w') as fd:
                            fd.write('Experiment Results\n')
                        for i in range(6):
                            print("Experiment:",i+1)
                            for img in dataset:
                                with open(os.path.join('cityscapes_100_images', img), "rb") as image_file:
                                    im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                                start = timer()
                                result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                                inference_time = timer() - start
                                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                print(result, " Inference Time(s): ", inference_time, " Timestamp: ", timestamp)
                                with open(result_file,'a') as fd:
                                    fd.write("{}, {}\n".format(timestamp, inference_time))
                        restart_containers(multi_tier,mobile_edge_bandwidth,'')

    if operator =="sptq":
        for subject in subjects:
            for single_tier in single_tiers:
                if single_tier == 'mobile' or single_tier == 'edge':
                    for mobile_edge_bandwidth in mobile_edge_bandwidths:
                        url, result_file=construct_url_for_sptq(single_tier, subject, mobile_edge_bandwidth, '')
                        with open(result_file,'w') as fd:
                            fd.write('Experiment Results\n')
                        for i in range(6):
                            print("Experiment:",i+1)
                            for img in dataset:
                                with open(os.path.join('cityscapes_100_images', img), "rb") as image_file:
                                    im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                                start = timer()
                                result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                                inference_time = timer() - start
                                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                print(result, " Inference Time(s): ", inference_time, " Timestamp: ", timestamp)
                                with open(result_file,'a') as fd:
                                    fd.write("{}, {}\n".format(timestamp, inference_time))
                        restart_containers(single_tier,mobile_edge_bandwidth,'')

                if single_tier == 'cloud':
                    for mobile_edge_bandwidth in mobile_edge_bandwidths:
                        for edge_cloud_bandwidth in edge_cloud_bandwidths:
                            url, result_file=construct_url_for_sptq(single_tier, subject, mobile_edge_bandwidth, edge_cloud_bandwidth)
                            with open(result_file,'w') as fd:
                                fd.write('Experiment Results\n')
                            for i in range(6):
                                print("Experiment:",i+1)
                                for img in dataset:
                                    with open(os.path.join('cityscapes_100_images', img), "rb") as image_file:
                                        im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                                    start = timer()
                                    result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                                    inference_time = timer() - start
                                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                    print(result, " Inference Time(s): ", inference_time, " Timestamp: ", timestamp)
                                    with open(result_file,'a') as fd:
                                        fd.write("{}, {}\n".format(timestamp, inference_time))
                            restart_containers(single_tier,mobile_edge_bandwidth,edge_cloud_bandwidth)

            for multi_tier in multi_tiers:
                if multi_tier == 'edge_cloud' or multi_tier == 'mobile_cloud':
                    for mobile_edge_bandwidth in mobile_edge_bandwidths:
                        for edge_cloud_bandwidth in edge_cloud_bandwidths:
                            url, result_file=construct_url_for_sptq_partition(multi_tier, subject,mobile_edge_bandwidth,edge_cloud_bandwidth)
                            with open(result_file,'w') as fd:
                                fd.write('Experiment Results\n')
                            for i in range(6):
                                print("Experiment:",i+1)
                                for img in dataset:
                                    with open(os.path.join('cityscapes_100_images', img), "rb") as image_file:
                                        im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                                    start = timer()
                                    result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                                    inference_time = timer() - start
                                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                    print(result, " Inference Time(s): ", inference_time, " Timestamp: ", timestamp)
                                    with open(result_file,'a') as fd:
                                        fd.write("{}, {}\n".format(timestamp, inference_time))
                            restart_containers(multi_tier,mobile_edge_bandwidth,edge_cloud_bandwidth)

    if operator =="earlyexit":
        for subject in subjects:
            for single_tier in single_tiers:
                if single_tier == 'mobile' or single_tier == 'edge':
                    for mobile_edge_bandwidth in mobile_edge_bandwidths:
                        for edge_cloud_bandwidth in edge_cloud_bandwidths:
                            url, result_file=construct_url_for_earlyexit(single_tier, subject, mobile_edge_bandwidth, edge_cloud_bandwidth)
                            with open(result_file,'w') as fd:
                                fd.write('Experiment Results\n')
                            for i in range(6):
                                print("Experiment:",i+1)
                                for img in dataset:
                                    with open(os.path.join('cityscapes_100_images', img), "rb") as image_file:
                                        im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                                    start = timer()
                                    result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                                    inference_time = timer() - start
                                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                    print(result, " Inference Time(s): ", inference_time, " Timestamp: ", timestamp)
                                    with open(result_file,'a') as fd:
                                        fd.write("{}, {}\n".format(timestamp, inference_time))
                            restart_containers(single_tier,mobile_edge_bandwidth,edge_cloud_bandwidth)

                if single_tier == 'cloud':
                    for mobile_edge_bandwidth in mobile_edge_bandwidths:
                        for edge_cloud_bandwidth in edge_cloud_bandwidths:
                            url, result_file=construct_url_for_earlyexit(single_tier, subject, mobile_edge_bandwidth, edge_cloud_bandwidth)
                            with open(result_file,'w') as fd:
                                fd.write('Experiment Results\n')
                            for i in range(6):
                                print("Experiment:",i+1)
                                for img in dataset:
                                    with open(os.path.join('cityscapes_100_images', img), "rb") as image_file:
                                        im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                                    start = timer()
                                    result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                                    inference_time = timer() - start
                                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                    print(result, " Inference Time(s): ", inference_time, " Timestamp: ", timestamp)
                                    with open(result_file,'a') as fd:
                                        fd.write("{}, {}\n".format(timestamp, inference_time))
                            restart_containers(single_tier,mobile_edge_bandwidth,edge_cloud_bandwidth)
            
            for multi_tier in multi_tiers:
                if multi_tier == 'edge_cloud' or multi_tier == 'mobile_cloud':
                    for mobile_edge_bandwidth in mobile_edge_bandwidths:
                        for edge_cloud_bandwidth in edge_cloud_bandwidths:
                            url, result_file=construct_url_for_earlyexit(multi_tier, subject, mobile_edge_bandwidth, edge_cloud_bandwidth)
                            with open(result_file,'w') as fd:
                                fd.write('Experiment Results\n')
                            for i in range(6):
                                print("Experiment:",i+1)
                                for img in dataset:
                                    with open(os.path.join('cityscapes_100_images', img), "rb") as image_file:
                                        im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                                    start = timer()
                                    result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                                    inference_time = timer() - start
                                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                    print(result, " Inference Time(s): ", inference_time, " Timestamp: ", timestamp)
                                    with open(result_file,'a') as fd:
                                        fd.write("{}, {}\n".format(timestamp, inference_time))
                            restart_containers(multi_tier,mobile_edge_bandwidth,edge_cloud_bandwidth)

    if operator =="sptq earlyexit":
        for subject in subjects:
            for single_tier in single_tiers:
                if single_tier ==  'mobile' or single_tier == 'edge':
                    for mobile_edge_bandwidth in mobile_edge_bandwidths:
                        url, result_file=construct_url_for_sptq_earlyexit(single_tier, subject, mobile_edge_bandwidth,'')
                        with open(result_file,'w') as fd:
                            fd.write('Experiment Results\n')
                        for i in range(6):
                            print("Experiment:",i+1)
                            for img in dataset:
                                with open(os.path.join('cityscapes_100_images', img), "rb") as image_file:
                                    im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                                start = timer()
                                result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                                inference_time = timer() - start
                                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                print(result, " Inference Time(s): ", inference_time, " Timestamp: ", timestamp)
                                with open(result_file,'a') as fd:
                                    fd.write("{}, {}\n".format(timestamp, inference_time))
                        restart_containers(single_tier,mobile_edge_bandwidth,edge_cloud_bandwidth)
                
                if single_tier == 'cloud':
                    for mobile_edge_bandwidth in mobile_edge_bandwidths:
                        for edge_cloud_bandwidth in edge_cloud_bandwidths:
                            url, result_file=construct_url_for_sptq_earlyexit(single_tier, subject, mobile_edge_bandwidth, edge_cloud_bandwidth)
                            with open(result_file,'w') as fd:
                                fd.write('Experiment Results\n')
                            for i in range(6):
                                print("Experiment:",i+1)
                                for img in dataset:
                                    with open(os.path.join('cityscapes_100_images', img), "rb") as image_file:
                                        im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                                    start = timer()
                                    result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                                    inference_time = timer() - start
                                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                    print(result, " Inference Time(s): ", inference_time, " Timestamp: ", timestamp)
                                    with open(result_file,'a') as fd:
                                        fd.write("{}, {}\n".format(timestamp, inference_time))
                            restart_containers(single_tier,mobile_edge_bandwidth,edge_cloud_bandwidth)

            for multi_tier in multi_tiers:
                if multi_tier == 'edge_cloud' or multi_tier == 'mobile_cloud':
                    for mobile_edge_bandwidth in mobile_edge_bandwidths:
                        for edge_cloud_bandwidth in edge_cloud_bandwidths:
                            url, result_file=construct_url_for_sptq_earlyexit(multi_tier, subject, mobile_edge_bandwidth, edge_cloud_bandwidth)
                            with open(result_file,'w') as fd:
                                fd.write('Experiment Results\n')
                            for i in range(6):
                                print("Experiment:",i+1)
                                for img in dataset:
                                    with open(os.path.join('cityscapes_100_images', img), "rb") as image_file:
                                        im_b64  = base64.b64encode(image_file.read()).decode("utf8")
                                    start = timer()
                                    result=requests.post(url,json=[im_b64],headers={'Content-Type': 'application/json', 'Accept':'application/json'}).json()
                                    inference_time = timer() - start
                                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                    print(result, " Inference Time(s): ", inference_time, " Timestamp: ", timestamp)
                                    with open(result_file,'a') as fd:
                                        fd.write("{}, {}\n".format(timestamp, inference_time))
                            restart_containers(multi_tier,mobile_edge_bandwidth,edge_cloud_bandwidth)

shutdown_all_containers()
