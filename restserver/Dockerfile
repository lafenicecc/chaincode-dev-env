FROM hyperledger/fabric-tools
ENV TZ Asia/Shanghai

RUN apt-get update \
        && apt-get install -y python-pip \
        && apt-get install -y vim tree \
        && pip install --upgrade pip
        && rm -rf /var/cache/apt

WORKDIR /app
COPY ./requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

# use this in development
CMD ["python", "restserver.py"]
