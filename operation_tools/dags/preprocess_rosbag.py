from airflow import DAG
from airflow.models import BaseOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.sensors.s3_key_sensor import S3KeySensor
from airflow.utils.decorators import apply_defaults
from datetime import datetime, timedelta
import re


from airflow import DAG
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 9, 1),
    'retries': 1,
}

# 処理を実行するPython関数
def process_new_file(**kwargs):
    s3_key = kwargs['ti'].xcom_pull(task_ids='check_for_new_file')
    print(f"New file detected: {s3_key}")
    # ここにファイル処理のロジックを記述

# DAGの設定
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 29),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'preprocess_rosbag',
    default_args=default_args,
    description='S3に新しいファイルが追加されたことを検知して処理を実行するDAG',
    schedule_interval=None,  # このDAGはスケジュールではなくセンサーでトリガーされる
    catchup=False,
)

# S3に新しいファイルが追加されたことを検知するセンサー
check_for_new_file = S3KeySensor(
    task_id='check_for_new_file',
    bucket_name='datalake',         # S3バケット名
    bucket_key='rosbag/**.mcap',    # 検知するファイルのパス（ワイルドカードを使用可能）
    wildcard_match=True,            # ワイルドカードでのマッチングを許可
    aws_conn_id='aws_default',      # Airflowで設定されているAWSの接続ID
    timeout=18*60*60,               # センサーのタイムアウト時間
    poke_interval=60,               # 次のチェックまでの待ち時間（秒）
    dag=dag,
)

# 新しいファイルが検知されたら処理を実行するタスク
process_file = PythonOperator(
    task_id='process_file',
    provide_context=True,
    python_callable=process_new_file,
    dag=dag,
)

# タスクの依存関係を設定
check_for_new_file >> process_file
