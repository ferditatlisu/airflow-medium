https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml

mkdir ./dags ./logs ./plugins

echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

docker compose up airflow-init

docker-compose up
