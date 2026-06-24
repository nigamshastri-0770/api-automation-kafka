from kafka import KafkaProducer
from kafka import KafkaConsumer
import json

from config.setting import (
    KAFKA_SERVER
)


def serializer(data):
    return json.dumps(
        data
    ).encode(
        "utf-8"
    )


def deserializer(data):
    return json.loads(
        data.decode(
            "utf-8"
        )
    )


def get_producer():

    return KafkaProducer(

        bootstrap_servers=KAFKA_SERVER,

        value_serializer=serializer
    )


def get_consumer(topic):

    return KafkaConsumer(

        topic,

        bootstrap_servers=KAFKA_SERVER,

        auto_offset_reset="earliest",

        value_deserializer=deserializer,

        group_id=None
    )