from airflow import DAG
from airflow.models import BaseOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.utils.decorators import apply_defaults
from datetime import datetime, timedelta
import re


from airflow import DAG
from datetime import datetime


class S3RegexListOperator(BaseOperator):
    @apply_defaults
    def __init__(
        self,
        bucket_name: str,
        prefix: str,
        regex_pattern: str,
        aws_conn_id: str = "aws_default",
        *args,
        **kwargs,
    ):
        super(S3RegexListOperator, self).__init__(*args, **kwargs)
        self.bucket_name = bucket_name
        self.prefix = prefix
        self.regex_pattern = regex_pattern
        self.aws_conn_id = aws_conn_id

    def execute(self, context):
        s3 = S3Hook(aws_conn_id=self.aws_conn_id)
        all_files = s3.list_keys(bucket_name=self.bucket_name, prefix=self.prefix)

        if not all_files:
            self.log.info(
                "No files found in the bucket %s with prefix %s",
                self.bucket_name,
                self.prefix,
            )
            return []

        matching_files = [
            file for file in all_files if re.match(self.regex_pattern, file)
        ]

        self.log.info(
            "Found %d files matching the pattern %s",
            len(matching_files),
            self.regex_pattern,
        )
        context["ti"].xcom_push(key="matching_files", value=matching_files)

        return matching_files


default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 9, 1),
    "retries": 1,
}


def process_new_file(**kwargs):
    s3_keys = kwargs["ti"].xcom_pull(
        task_ids="listup_mcap_files_in_datalake", key="matching_files"
    )
    if len(s3_keys) == 0:
        print("No files are found, something wrong heppens.")
    else:
        for s3_key in s3_keys:
            print(f"New file detected: {s3_key}")


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 8, 29),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "preprocess_rosbag",
    default_args=default_args,
    description="When you upload new data to the minio storage datalake, preprocess data.",
    schedule_interval=timedelta(minutes=2),
    catchup=False,
    max_active_runs=1,
)

list_matching_files = S3RegexListOperator(
    task_id="listup_mcap_files_in_datalake",
    bucket_name="datalake",
    prefix="rosbag/",
    regex_pattern=r"^.*\.mcap$",
    aws_conn_id="aws_default",
    dag=dag,
)

process_file = PythonOperator(
    task_id="process_file",
    provide_context=True,
    python_callable=process_new_file,
    dag=dag,
)

list_matching_files >> process_file
