import uuid

from kafka_client_lib.kafka_client import get_producer
from config.setting import KAFKA_TOPIC


def publish_event(payload):

    producer = get_producer()

    event = {

        "event_id": str(
            uuid.uuid4()
        ),

        "correlation_id": str(
            uuid.uuid4()
        ),

        "type": "ORDER_CREATED",

        "payload": payload
    }

    producer.send(
        KAFKA_TOPIC,
        value=event
    )

    producer.flush()

    return event