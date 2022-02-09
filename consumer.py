import json
from kafka import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'messages',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'  # Earliest messages display first
    )
    for message in consumer:
        # print(f"[Log - message received] {json.loads(message.value)}")
        print(json.loads(message.value.decode('utf-8')))
