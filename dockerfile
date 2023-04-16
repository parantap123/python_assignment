FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev && \
    pip install -r requirements.txt

COPY . .

CMD ["python", "financial/app.py"]
