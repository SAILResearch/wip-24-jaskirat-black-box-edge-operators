# Prerequisite

## 1. Environment

```shell
pip install -r requirements.txt
```

> Note: Validated ONNX Runtime [Version](/docs/source/installation_guide.md#validated-software-environment).

## 2. Prepare Model

```shell
python prepare_model.py --output_model='fcn-resnet101-11.onnx'
```

## 3. Prepare Dataset

Download dataset [MS COCO 2017 dataset](https://cocodataset.org/#download).

# Run

## 1. SPTQ Quantization

```bash
bash run_quant.sh --input_model=fcn-resnet101-11.onnx  \ # model path as *.onnx
                   --dataset_location=path/to/val2017/ \
                   --label_path=/path/to/instances_val2017.json \
                   --output_model=fcn-resnet101-11_int8_sptq.onnx \ # model path as *.onnx
                   --quant_format=QDQ
```

## 2. Partitioning

```shell
python fcn_partition.py
```

## 3. Early Exiting

```shell
python fcn_earlyexit.py
```

## 4. Quantize Early Exiting

```shell
python fcn_quantize_earlyexit.py
```
## 4. Quantize Early Exit Partitioning

```shell
python fcn_quantize_earlyexit_partition.py
```

