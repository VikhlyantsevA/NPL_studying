#!/bin/bash

cat create_rt_table.txt | clickhouse-client --port 9090 --multiline
cat create_in_table.txt | clickhouse-client --port 9090 --multiline
cat create_view.txt | clickhouse-client --port 9090 --multiline
cat create_agg_hourly_table.txt | clickhouse-client --port 9090 --multiline
