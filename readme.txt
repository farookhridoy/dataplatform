
Docker Container List:

flink-taskmanager
flink-jobmanager
kafka-connect
kafka
kibana
s3-storage
elasticsearch
mysql
zookeeper
eventgenerator

** check running docker container
sudo docker ps

** check container logs
sudo docker logs -f <container name>
sudo docker logs -f mysql


** start docker container
sudo docker start <Container name> <container name>
sudo docker start eventgenerator flink-taskmanager flink-jobmanager


** stop docker container
sudo docker stop <Container name> <container name>
sudo docker stop eventgenerator


** import kibana dashboard
check http://localhost:5601/app/ is up and running then run below command

curl -X POST "localhost:5601/api/saved_objects/_import" -H "kbn-xsrf: true" --form file=@./kibana/dashboard/dataplatform.ndjson

