FROM python:3.10-alpine

WORKDIR /app

COPY . . 

RUN pip install .

EXPOSE 8080

CMD ["run_srv"]
