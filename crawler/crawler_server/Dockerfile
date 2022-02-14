FROM ubuntu

RUN apt-get update -y && \  
    apt-get install -y python3-pip python3-dev python3-yaml python3-cryptography

COPY . ./crawler_server
WORKDIR /crawler_server
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD [ "main.py" ]

