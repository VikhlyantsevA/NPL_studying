# Run kcat in docker container. Run consumer to read topic with <topic_name>
docker run -it --network=host edenhill/kcat:1.7.1 -b <kafka_host_ip>:9092 -C -t <topic_name>

# Run kcat in docker container. Run producer to produce data to topic with <topic_name>
docker run -it --network=host edenhill/kcat:1.7.1 -b <kafka_host_ip>:9092 -P -t <topic_name>

# Run kcat in docker container. List topics info
docker run -it --network=host edenhill/kcat:1.7.1 -b <kafka_host_ip>:9092 -L

