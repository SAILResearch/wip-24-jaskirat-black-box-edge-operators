import pandas as pd

import pandas as pd

# Initialize an empty DataFrame
df = pd.DataFrame(columns=['Inference', 'Device', 'Model', 'Mobile_Edge_Bandwidth', 'Edge_Cloud_Bandwidth'])

# Define the bandwidth values
mobile_edge_bandwidths = [10, 50, 100, 150, 200]
edge_cloud_bandwidths = [10, 50, 100, 150, 200]

# List of models
models = [
    "cloud_fcn", "cloud_resnet", "cloud_resnext", "cloud_duc",
    "cloud_fcn_earlyexit", "cloud_resnet_earlyexit", "cloud_resnext_earlyexit", "cloud_duc_earlyexit",
    "cloud_fcn_int8_sptq", "cloud_resnet_int8_sptq", "cloud_resnext_int8_sptq", "cloud_duc_int8_sptq",
    "cloud_fcn_earlyexit_int8_sptq", "cloud_resnet_earlyexit_int8_sptq", "cloud_resnext_earlyexit_int8_sptq", "cloud_duc_earlyexit_int8_sptq",
    "mobile_cloud_fcn", "mobile_cloud_resnet", "mobile_cloud_resnext", "mobile_cloud_duc",
    "edge_cloud_fcn", "edge_cloud_resnet", "edge_cloud_resnext", "edge_cloud_duc",
    "mobile_cloud_fcn_earlyexit_int8_sptq", "mobile_cloud_resnet_earlyexit_int8_sptq",
    "mobile_cloud_resnext_earlyexit_int8_sptq", "mobile_cloud_duc_earlyexit_int8_sptq",
    "edge_cloud_fcn_earlyexit_int8_sptq", "edge_cloud_resnet_earlyexit_int8_sptq",
    "edge_cloud_resnext_earlyexit_int8_sptq", "edge_cloud_duc_earlyexit_int8_sptq"
]

# Iterate over models
for model in models:
    # Iterate over Mobile-Edge and Edge-Cloud Bandwidth combinations
    for mobile_bw in mobile_edge_bandwidths:
        for edge_bw in edge_cloud_bandwidths:
            # Construct the file path
            file_path = f'{model}/{model}_{mobile_bw}mbps_{edge_bw}mbps_results.txt' 
            # Read the file and extract the lines
            try:
                with open(file_path, 'r') as f:
                    lines = f.readlines()[1:]  # Skip the header line
                
                # Append the lines to the DataFrame
                for value in lines:
                    df = df._append({
                        'Inference': value.strip(),
                        'Device': 'Cloud' if "cloud" in model else "Mobile" if "mobile" in model else "Edge",
                        'Model': model,
                        'Mobile_Edge_Bandwidth': str(mobile_bw),
                        'Edge_Cloud_Bandwidth': str(edge_bw)
                    }, ignore_index=True)
            
            except FileNotFoundError:
                print(f"File not found: {file_path}")


        
df.to_csv('Inference_Results_Paper1.csv', index=False)
