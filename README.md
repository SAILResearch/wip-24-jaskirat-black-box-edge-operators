1. mobile_docker_image, edge_docker_image, and cloud_docker_image folder contains the code for setting up Mobile, Edge, and Cloud containers for Inference Experiments.
2. black_box_operators folder contains the scripts for generating the operators.
3. Inference_Results contains the Accuracy and latency results of the operators.
4. Run_Latency_experiments contains the script for running the latency experiments.
5. graphs folder contains the graphs of partitioning-based operators.
6. The models generated are attached in the Release Section.


Used the following port forwarding in Server1 to connect edge tier in Server 1 with the cloud tier in Server2.
ssh -o ServerAliveInterval=60 -f -N -L :5002:localhost:5002 username@server2 Ip address

Use the following port forwarding in Server1 to restart or stop the cloud tier in Server2
ssh -o ServerAliveInterval=60 -f -N -L :8000:localhost:8000 username@server2 Ip address

The speed test tool confirmed that the network bandwidths are restricted to approximately a particular value.
