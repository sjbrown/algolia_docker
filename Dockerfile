FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt update -y && apt install -y \
    git \
    vim \
    python-pip \
    python3-pip

RUN pip3 install --upgrade 'algoliasearch>=2.0,<3.0'
RUN pip3 install 'asyncio>=3.4,<4.0' 'aiohttp>=2.0,<4.0' 'async_timeout>=2.0,<4.0'
RUN apt-get install -y npm
RUN npm install -g npx
RUN npm install vue-instantsearch algoliasearch instantsearch.css

COPY . /app
WORKDIR /app

ENTRYPOINT /bin/bash


