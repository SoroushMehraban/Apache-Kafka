import time
import json
from datetime import datetime
from data_generator import generate_message
from kafka import KafkaProducer


def serializer(message):
    """serializes the message as JSON"""
    return json.dumps(message).encode('utf-8')


if __name__ == '__main__':
    producer = KafkaProducer(
        bootstrap_servers={'localhost:9092'},
        value_serializer=serializer
    )

    while True:
        dummy_message = generate_message()
        print(f"[LOG - {datetime.now()}] message: {dummy_message}")
        producer.send('messages', dummy_message)

        time.sleep(5)

