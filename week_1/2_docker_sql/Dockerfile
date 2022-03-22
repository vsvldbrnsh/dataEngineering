FROM python:3.9

RUN pip install pandas sqlalchemy psycopg2
RUN apt-get install wget

WORKDIR /app

COPY data_ingest.py data_ingest.py

ENTRYPOINT ["python", "data_ingest.py"]