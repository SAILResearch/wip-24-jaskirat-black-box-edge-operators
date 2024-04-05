# Prerequisite

## 1. Environment

```shell
pip install -r requirements.txt
```

> Note: Validated ONNX Runtime [Version](/docs/source/installation_guide.md#validated-software-environment).

## 2. Prepare Model

```shell
python prepare_resnet_original_model.py --output_model='wide-resnet101.onnx'
```

```shell
python prepare_resnext_original_model.py --output_model='resnext101.onnx'
```

## 3. Prepare Dataset

Download dataset [ILSVR2012 validation Imagenet dataset](http://www.image-net.org/challenges/LSVRC/2012/downloads).

Download label:

```shell
wget http://dl.caffe.berkeleyvision.org/caffe_ilsvrc12.tar.gz
tar -xvzf caffe_ilsvrc12.tar.gz val.txt
```

# Run

## 1. SPTQ Quantization

```bash
bash run_quant.sh --input_model=wide-resnet101.onnx \  # model path as *.onnx
                   --dataset_location=/path/to/imagenet \
                   --label_path=/path/to/val.txt \
                   --output_model=wide-resnet101_int8_sptq.onnx \  # model path as *.onnx
                   --quant_format=QDQ
```

```bash
bash run_quant.sh --input_model=resnext101.onnx \  # model path as *.onnx
                   --dataset_location=/path/to/imagenet \
                   --label_path=/path/to/val.txt \
                   --output_model=resnext101_int8_sptq.onnx \  # model path as *.onnx
                   --quant_format=QDQ
```

## 2. Partitioning

```shell
python resnet_partition.py
python resnext_partition.py
```

## 3. Early Exiting

```shell
python resnet_earlyexit.py
python resnext_earlyexit.py
```

## 4. Quantize Early Exiting

```shell
python resnet_quantize_earlyexit.py
python resnext_quantize_earlyexit.py
```
## 4. Quantize Early Exit Partitioning

```shell
python resnet_quantize_earlyexit_partition.py
python resnext_quantize_earlyexit_partition.py
```


