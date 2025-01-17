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

## 3. Create a Network Bridge for connecting Mobile and Edge Docker Containers

```shell
docker network create mobile_edge_network
```

## 4. Prepare Mobile Docker Container

```shell
docker build -t mobile_inference .
docker run -it --net=mobile_edge_network --cap-add=NET_ADMIN --name mobile_inference_container -e PYTHONUNBUFFERED=1 --cpus="4" --memory="4g" -p 5000:5000 -d mobile_inference
```

The speed test tool confirmed that the network bandwidths are restricted to approximately a particular value.


