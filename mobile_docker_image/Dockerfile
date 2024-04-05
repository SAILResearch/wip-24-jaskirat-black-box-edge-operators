FROM python:3.9-slim
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
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
