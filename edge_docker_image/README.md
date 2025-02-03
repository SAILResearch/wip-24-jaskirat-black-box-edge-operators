# Prerequisite

## 1. Prepare Dataset

Download Validation data
1. [ILSVR2012 Imagenet dataset](http://www.image-net.org/challenges/LSVRC/2012/downloads).
2. [MS COCO 2017 dataset](https://cocodataset.org/#download).
3. [cityscapes dataset](https://www.cityscapes-dataset.com/downloads/).

## 2. Create a Network Bridge for connecting Mobile and Edge Docker Containers in a shared server

```shell
docker network create mobile_edge_network
```

## 3. Prepare Edge Docker Container 

```shell
docker build -t edge_inference .
docker run -it --net=mobile_edge_network --cap-add=NET_ADMIN --name edge_inference_container -e PYTHONUNBUFFERED=1 --cpus="8" --memory="16g" -p 5001:5001 -d edge_inference
```
## 4. SSh tunneling of the shared server with the external server to exchange API requests between Edge and Cloud Docker containers

```shell
ssh -o ServerAliveInterval=60 -f -N -L :5002:localhost:5002 username@servername
```
<<<<<<< HEAD

The speed test tool confirmed that the network bandwidths used are restricted to a particular value.
=======
The speed test tool confirmed that the network bandwidths are restricted to approximately a particular value.
>>>>>>> e5e0e2d07c90a51308649bca623284a4e4c76992
