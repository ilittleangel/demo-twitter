FROM python:3.6.5-slim-stretch
LABEL project="demo-twitter"

WORKDIR /demo-twitter
COPY requirements.txt requirements.txt
RUN pip3.6 install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "/demo-twitter/ingestion.py"]
