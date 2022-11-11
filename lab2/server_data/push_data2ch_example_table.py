from clickhouse_driver import Client
import json
import os

client = Client(host='localhost', port=9090)

table_name = "example_table"

with open(os.path.join(os.path.dirname(__file__), "lab02_train_exploded50.json"), 'r', encoding='utf-8') as f:
    values = [json.loads(line) for line in f]
    print(f"Got {len(values)} rows")

query = f"INSERT INTO {table_name} FORMAT JSONEachRow"
res = client.execute(query, values)
