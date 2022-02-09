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
### Kafka topics
All kafka shell scripts are located in  **opt/kafka_<VERSION>/bin/**. Hence, we can navigate there by entering the
following command:  
`cd opt/kafka_<VERSION>/bin/`  
#### create
`kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic <TOPIC_NAME>`
#### list
`kafka-topics.sh --list --zookeeper zookeeper:2181`
#### describe
You may use the following command to get information about a topic such as partition count or replication factor:
`kafka-topics.sh --describe --zookeeper zookeeper:2181 --topic <TOPIC_NAME>`
#### delete
`kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic <TOPIC_NAME>`
### Kafka producers
To begin with, we create a new topic named "messages" that simulates a multi-user chat:  
`kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic messages`

To connect to producer shell, enter the following command:
`kafka-console-producer.sh --broker-list kafka:9092 --topic messages`

Then, in whichever format we like, we may insert two messages:  
`{'user_id': 1, 'recipient_id': 2, 'meesage': 'Hi.'}`  
`{'user_id': 2, 'recipient_id': 1, 'meesage': 'Hello there.'}`

Once it's done, press `CTRL + C` to close the producer shell.
### Kafka consumers
To connect to consumer shell, enter the following command:
`kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic messages`

As you can see, nothing occurs after the consumer is started.
That is because the consumer by default does not display all messages,
but just the incoming ones.

To validate this, open two terminals and connect to the kafka shell,
followed by concurrently opening the kafka producer and consumer and
entering a message from the producer. As you can see, the customer
immediately gets the message.

**What if we want to list all produced messages for a specific topic!?**  
To do that, use the following command when trying to connect to the consumer shell:
`kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic meesages --from-beginning`
## Python usage
**First step**: create a topic from kafka shell if does not exist.  
**Second step**: Install python kafka package:  
`pip install kafka-python`  
**Third step**: Execute consumer.py and producer.py respectively. every 5 seconds a message is sent to the messages
topic and consumer is able to show that.
