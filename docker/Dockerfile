# Usar uma imagem oficial do Airflow
FROM apache/airflow:2.6.0-python3.10

# Configuração do ambiente
ENV AIRFLOW_HOME=/opt/airflow

# Instala dependências adicionais necessárias
RUN pip install requests pandas

# Copia a DAG e scripts para o contêiner
COPY dags/ $AIRFLOW_HOME/dags/
COPY scripts/ $AIRFLOW_HOME/scripts/

# Define o comando padrão ao iniciar o contêiner
CMD ["airflow", "standalone"]