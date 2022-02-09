# Apache kafka with python and docker
This repository shows how to use apache kafka with python and docker.
## Build and install
To build and install kafka and zookeeper containers, execute the following command:  
`docker-compose -f docker-compose.yml up -d`  
To verify that both services are running, enter the following command:  
`docker ps`
## Usage
### Shell connection
To connect to kafka shell, enter the following command:  
`docker exec -it kafka /bin/sh`  
In the preceding command:
- `exec`: execute
- `-it`: Interacting mode
- `kafka`: container name
- `/bin/sh`: path to the shell
### Topic creation
All kafka shell scripts are located in  **opt/kafka_<VERSION>/bin/**. Hence, we can navigate there by entering the
following command:  
`cd opt/kafka_<VERSION>/bin/`  

To create a kafka topic, enter the following command:  
`kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic <TOPIC NAME>`

You can also list all the topics with the following command:
`kafka-topics.sh --list --zookeeper zookeeper:2181`



