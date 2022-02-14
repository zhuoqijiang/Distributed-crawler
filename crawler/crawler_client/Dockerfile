FROM ubuntu

RUN apt-get update -y && \  
    apt-get install -y python3-pip python3-dev python3-yaml

COPY . ./crawler_client
WORKDIR /crawler_client
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD [ "main.py" ]

