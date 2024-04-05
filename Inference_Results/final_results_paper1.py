import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
df = pd.DataFrame(columns=['Inference', 'Device', 'Model'])

with open('mobile_resnet_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile',
                        'Model': 'ResNet'}, ignore_index=True)
                        
with open('mobile_resnet_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile',
                        'Model': 'ResNet Quantize'}, ignore_index=True)

with open('mobile_resnet_earlyexit_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile',
                        'Model': 'ResNet EarlyExit'}, ignore_index=True)
with open('mobile_resnet_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile',
                        'Model': 'ResNet Quantize EarlyExit'}, ignore_index=True)
with open('mobile_resnext_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile',
                        'Model': 'ResNext'}, ignore_index=True)
with open('mobile_resnext_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile',
                        'Model': 'ResNext Quantize'}, ignore_index=True)

with open('mobile_resnext_earlyexit_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile',
                        'Model': 'ResNext EarlyExit'}, ignore_index=True)
with open('mobile_resnext_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile',
                        'Model': 'ResNext Quantize EarlyExit'}, ignore_index=True)

with open('mobile_fcn_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile',
                        'Model': 'FCN'}, ignore_index=True)
with open('mobile_fcn_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile',
                        'Model': 'FCN Quantize'}, ignore_index=True)
        
with open('mobile_fcn_earlyexit_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile',
                        'Model': 'FCN EarlyExit'}, ignore_index=True)
with open('mobile_fcn_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile',
                        'Model': 'FCN Quantize EarlyExit'}, ignore_index=True)
with open('mobile_duc_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile',
                        'Model': 'DUC'}, ignore_index=True)
with open('mobile_duc_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile',
                        'Model': 'DUC Quantize'}, ignore_index=True)
with open('mobile_duc_earlyexit_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile',
                        'Model': 'DUC EarlyExit'}, ignore_index=True)
with open('mobile_duc_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile',
                        'Model': 'DUC Quantize EarlyExit'}, ignore_index=True)
with open('edge_resnet_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge',
                        'Model': 'ResNet'}, ignore_index=True)
with open('edge_resnet_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge',
                        'Model': 'ResNet Quantize'}, ignore_index=True)

with open('edge_resnet_earlyexit_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge',
                        'Model': 'ResNet EarlyExit'}, ignore_index=True)
with open('edge_resnet_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge',
                        'Model': 'ResNet Quantize EarlyExit'}, ignore_index=True)

with open('edge_resnext_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge',
                        'Model': 'ResNext'}, ignore_index=True)
with open('edge_resnext_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge',
                        'Model': 'ResNext Quantize'}, ignore_index=True)

with open('edge_resnext_earlyexit_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge',
                        'Model': 'ResNext EarlyExit'}, ignore_index=True)
with open('edge_resnext_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge',
                        'Model': 'ResNext Quantize EarlyExit'}, ignore_index=True)

with open('edge_fcn_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge',
                        'Model': 'FCN'}, ignore_index=True)
with open('edge_fcn_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge',
                        'Model': 'FCN Quantize'}, ignore_index=True)

with open('edge_fcn_earlyexit_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge',
                        'Model': 'FCN EarlyExit'}, ignore_index=True)
with open('edge_fcn_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge',
                        'Model': 'FCN Quantize EarlyExit'}, ignore_index=True)

with open('edge_duc_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge',
                        'Model': 'DUC'}, ignore_index=True)
with open('edge_duc_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge',
                        'Model': 'DUC Quantize'}, ignore_index=True)

with open('edge_duc_earlyexit_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge',
                        'Model': 'DUC EarlyExit'}, ignore_index=True)
with open('edge_duc_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge',
                        'Model': 'DUC Quantize EarlyExit'}, ignore_index=True)

with open('cloud_resnet_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Cloud',
                        'Model': 'ResNet'}, ignore_index=True)
with open('cloud_resnet_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Cloud',
                        'Model': 'ResNet Quantize'}, ignore_index=True)

with open('cloud_resnet_earlyexit_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Cloud',
                        'Model': 'ResNet EarlyExit'}, ignore_index=True)
with open('cloud_resnet_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Cloud',
                        'Model': 'ResNet Quantize EarlyExit'}, ignore_index=True)

with open('cloud_resnext_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Cloud',
                        'Model': 'ResNext'}, ignore_index=True)
with open('cloud_resnext_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Cloud',
                        'Model': 'ResNext Quantize'}, ignore_index=True)

with open('cloud_resnext_earlyexit_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Cloud',
                        'Model': 'ResNext EarlyExit'}, ignore_index=True)
with open('cloud_resnext_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Cloud',
                        'Model': 'ResNext Quantize EarlyExit'}, ignore_index=True)

with open('cloud_fcn_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Cloud',
                        'Model': 'FCN'}, ignore_index=True)
with open('cloud_fcn_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Cloud',
                        'Model': 'FCN Quantize'}, ignore_index=True)

with open('cloud_fcn_earlyexit_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Cloud',
                        'Model': 'FCN EarlyExit'}, ignore_index=True)
with open('cloud_fcn_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Cloud',
                        'Model': 'FCN Quantize EarlyExit'}, ignore_index=True)
        
with open('cloud_duc_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Cloud',
                        'Model': 'DUC'}, ignore_index=True)
with open('cloud_duc_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Cloud',
                        'Model': 'DUC Quantize'}, ignore_index=True)

with open('cloud_duc_earlyexit_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Cloud',
                        'Model': 'DUC EarlyExit'}, ignore_index=True)
with open('cloud_duc_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Cloud',
                        'Model': 'DUC Quantize EarlyExit'}, ignore_index=True)


with open('mobile_cloud_resnet_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile-Cloud',
                        'Model': 'ResNet'}, ignore_index=True)

with open('mobile_cloud_resnet_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile-Cloud',
                        'Model': 'ResNet Quantize EarlyExit'}, ignore_index=True)

with open('mobile_cloud_resnext_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile-Cloud',
                        'Model': 'ResNext'}, ignore_index=True)

with open('mobile_cloud_resnext_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile-Cloud',
                        'Model': 'ResNext Quantize EarlyExit'}, ignore_index=True)

with open('edge_cloud_resnet_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge-Cloud',
                        'Model': 'ResNet'}, ignore_index=True)

with open('edge_cloud_resnet_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge-Cloud',
                        'Model': 'ResNet Quantize EarlyExit'}, ignore_index=True)
        
with open('edge_cloud_resnext_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge-Cloud',
                        'Model': 'ResNext'}, ignore_index=True)

with open('edge_cloud_resnext_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge-Cloud',
                        'Model': 'ResNext Quantize EarlyExit'}, ignore_index=True)
        
with open('mobile_edge_resnet_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile-Edge',
                        'Model': 'ResNet'}, ignore_index=True)

with open('mobile_edge_resnet_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile-Edge',
                        'Model': 'ResNet Quantize EarlyExit'}, ignore_index=True)

with open('mobile_edge_resnext_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile-Edge',
                        'Model': 'ResNext'}, ignore_index=True)

with open('mobile_edge_resnext_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile-Edge',
                        'Model': 'ResNext Quantize EarlyExit'}, ignore_index=True)

with open('mobile_edge_fcn_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile-Edge',
                        'Model': 'FCN'}, ignore_index=True)
        
with open('mobile_edge_fcn_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile-Edge',
                        'Model': 'FCN Quantize EarlyExit'}, ignore_index=True)

with open('mobile_edge_duc_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile-Edge',
                        'Model': 'DUC'}, ignore_index=True)
        
with open('mobile_edge_duc_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile-Edge',
                        'Model': 'DUC Quantize EarlyExit'}, ignore_index=True)

with open('mobile_cloud_fcn_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile-Cloud',
                        'Model': 'FCN'}, ignore_index=True)

with open('mobile_cloud_fcn_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile-Cloud',
                        'Model': 'FCN Quantize EarlyExit'}, ignore_index=True)

with open('mobile_cloud_duc_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile-Cloud',
                        'Model': 'DUC'}, ignore_index=True)

with open('mobile_cloud_duc_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Mobile-Cloud',
                        'Model': 'DUC Quantize EarlyExit'}, ignore_index=True)
        
with open('edge_cloud_fcn_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge-Cloud',
                        'Model': 'FCN'}, ignore_index=True)

with open('edge_cloud_fcn_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge-Cloud',
                        'Model': 'FCN Quantize EarlyExit'}, ignore_index=True)
        
with open('edge_cloud_duc_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge-Cloud',
                        'Model': 'DUC'}, ignore_index=True)
        
with open('edge_cloud_duc_earlyexit_int8_sptq_results.txt', 'r') as f:
    lines = f.readlines()[1:][-500:]
    for value in lines:
        df = df._append({'Inference': value, 'Device': 'Edge-Cloud',
                        'Model': 'DUC Quantize EarlyExit'}, ignore_index=True)

df.to_csv('Inference_Results_Paper1.csv', index=False)
