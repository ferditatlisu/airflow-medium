FROM apache/airflow:2.3.4
COPY requirements.txt .
RUN pip3 install -r requirements.txt