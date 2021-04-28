FROM python:3.8-slim
LABEL project="demo-twitter"

WORKDIR /demo-twitter
COPY requirements.txt requirements.txt

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends g++ make

RUN pip3.8 install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "/demo-twitter/ingestion.py"]
