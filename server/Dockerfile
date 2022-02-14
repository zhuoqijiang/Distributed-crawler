FROM python:3

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED 1

COPY . ./server
WORKDIR /server
#RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "manage.py", "runserver"]
CMD ["localhost:8080"]

