from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError

import json
import time

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


def get_producer(
        retries=5
):

    delay = 2

    for attempt in range(retries):

        try:

            return KafkaProducer(

                bootstrap_servers=KAFKA_SERVER,

                value_serializer=serializer,

                retries=5,

                request_timeout_ms=10000,

                api_version=(3, 6)
            )

        except KafkaError:

            if attempt == retries - 1:
                raise

            print(
                f"Kafka retry {attempt + 1}/{retries}"
            )

            time.sleep(
                delay
            )

            delay *= 2


def get_consumer(
        topic,
        retries=5
):

    delay = 2

    for attempt in range(retries):

        try:

            return KafkaConsumer(

                topic,

                bootstrap_servers=KAFKA_SERVER,

                auto_offset_reset="earliest",

                value_deserializer=deserializer,

                group_id=None
            )

        except KafkaError:

            if attempt == retries - 1:
                raise

            print(
                f"Consumer retry {attempt + 1}/{retries}"
            )

            time.sleep(
                delay
            )

            delay *= 2