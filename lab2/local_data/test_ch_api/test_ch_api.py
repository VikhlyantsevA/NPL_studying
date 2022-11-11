from urllib import parse
import requests
import os

host = "5.188.140.232"
clickhouse_port = 8123

table = "my_table_gender_age_dist"
data_format = "JSONEachRow"
curr_path = os.path.dirname(__file__)
message_source_path = os.path.join(curr_path, "lab02_train_exploded50.json")

query = f"INSERT INTO {table} FORMAT {data_format}"
query_quote = parse.quote(query)
print(f"Prepared query: {query_quote}")

messages = open(message_source_path).read()
url = 'http://{}:{}/?query={}'.format(host, clickhouse_port, query_quote)
res = requests.post(url, data=messages.encode("utf-8"))
print(res.status_code, res.text)
