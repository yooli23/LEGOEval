FROM node

COPY ./app/requirements.txt .

RUN apt-get update -y \
    && apt-get install -y \
    python3.6 \
    python3-pip \
    curl \
    git \
    wget \
    && pip3 install --upgrade pip \
    && pip3 install -r requirements.txt

WORKDIR /root

CMD ["/bin/bash"]

