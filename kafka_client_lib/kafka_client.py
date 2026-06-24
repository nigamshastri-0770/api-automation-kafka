from kafka import KafkaConsumer
from kafka import KafkaProducer
import json


def get_producer():

    return KafkaProducer(

        bootstrap_servers="localhost:9092",

        value_serializer=lambda x:
        json.dumps(x).encode("utf-8")
    )


def get_consumer(topic):

    consumer = KafkaConsumer(

        topic,

        bootstrap_servers="localhost:9092",

        auto_offset_reset="earliest",

        enable_auto_commit=True,

        group_id=None,

        value_deserializer=lambda x:
        json.loads(
            x.decode(
                "utf-8"
            )
        )
    )

    return consumer