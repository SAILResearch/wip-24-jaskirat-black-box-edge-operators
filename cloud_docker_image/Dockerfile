FROM python:3.9-slim
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN apt-get update && apt-get install \
        --no-install-recommends --no-install-suggests -y \
        build-essential \
	protobuf-compiler \
        libgl1-mesa-glx \
	libprotoc-dev \
        libglib2.0-0 \
        libsm6 \
        libxrender1 \
        libxext6 \
	iproute2 \
        curl \
        nano \
	wget \
	unzip
RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh
RUN conda install -c anaconda cudatoolkit -y 
RUN pip install torch==1.13.1+cu117 torchvision --extra-index-url https://download.pytorch.org/whl/cu117
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
