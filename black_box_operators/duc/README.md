# Prerequisite

## 1. Environment

```shell
pip install -r requirements.txt
```

> Note: Validated ONNX Runtime [Version](/docs/source/installation_guide.md#validated-software-environment).

## 2. Prepare Model

```shell
python prepare_model.py --output_model='ResNet101-DUC-12.onnx'
```

## 3. Prepare Dataset

Download dataset [cityscapes dataset](https://www.cityscapes-dataset.com/downloads/).

Dataset directories:

```bash
cityscapes
├── gtFine
|   └── val
├── leftImg8bit
|   └── val
```

# Run

## 1. SPTQ Quantization

```bash
bash run_quant.sh --input_model=ResNet101-DUC-12.onnx  \ # model path as *.onnx
                   --output_model=ResNet101-DUC-12_int8_sptq.onnx \ # model path as *.onnx
                   --dataset_location=/path/to/cityscapes/leftImg8bit/val \
                   --quant_format="QOperator"
```

## 2. Partitioning

```shell
python duc_partition.py
```

## 3. Early Exiting

```shell
python duc_earlyexit.py
```

## 4. Quantize Early Exiting

```shell
python duc_quantize_earlyexit.py
```
## 4. Quantize Early Exit Partitioning

```shell
python duc_quantize_earlyexit_partition.py
```
