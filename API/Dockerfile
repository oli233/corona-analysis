FROM python:3

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN mkdir -p /app
WORKDIR /app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./API/requirements.txt /app/requirements.txt
COPY ./DataDriver /app/DataDriver

RUN pip install -r requirements.txt

COPY ./API /app

EXPOSE 5000/tcp

ENTRYPOINT [ "python" ]

CMD [ "API.py" ]
# CMD ["test.py"]
