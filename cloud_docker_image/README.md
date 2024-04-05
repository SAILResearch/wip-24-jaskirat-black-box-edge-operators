# Prerequisite

## 1. Environment

```shell
pip install -r requirements.txt
```

## 3. Prepare Dataset

Download Validation data
1. [ILSVR2012 Imagenet dataset](http://www.image-net.org/challenges/LSVRC/2012/downloads).
2. [MS COCO 2017 dataset](https://cocodataset.org/#download).
3. [cityscapes dataset](https://www.cityscapes-dataset.com/downloads/).

## 3. Create a Network Bridge for Cloud Docker Container

```shell
docker network create cloud_network
```

## 4. Prepare Cloud Docker Container

```shell
docker build -t cloud_inference .
docker run -it --net=cloud_network --cap-add=NET_ADMIN --name cloud_inference_container --gpus device=0 -e PYTHONUNBUFFERED=1 --cpus="16" --memory="64g" -p 5002:5002 -d cloud_inference
```

