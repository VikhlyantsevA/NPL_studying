from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
from airflow_clickhouse_plugin.operators.clickhouse_operator import ClickHouseOperator
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQL_DIR = os.path.join(BASE_DIR, 'sql')

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

with DAG(
    dag_id='alexander_vikhlyantsev_lab02',
    default_args=default_args,
    schedule_interval=None,
    tags=['lab02']
) as dag:
    default_ch_params = dict(
        clickhouse_conn_id='ch_conn',
        database='default'
    )

    with open(os.path.join(SQL_DIR, 'truncate_agg.sql')) as f:
        truncate_agg_sql = f.read()

    with open(os.path.join(SQL_DIR, 'push2agg.sql')) as f:
        push2agg_sql = f.read()

    with open(os.path.join(SQL_DIR, 'truncate_rt.sql')) as f:
        truncate_rt_sql = f.read()

    start = DummyOperator(task_id='start')

    truncate_agg_table = ClickHouseOperator(
        task_id='truncate_agg_table',
        sql=truncate_agg_sql,
        ** default_ch_params
    )

    push2agg_table = ClickHouseOperator(
        task_id='push2agg_table',
        sql=push2agg_sql,
        ** default_ch_params
    )

    truncate_rt_table = ClickHouseOperator(
        task_id='truncate_rt_table',
        sql=truncate_rt_sql,
        ** default_ch_params
    )

    finish = DummyOperator(task_id='finish')

    start >> truncate_agg_table >> push2agg_table >> truncate_rt_table >> finish
