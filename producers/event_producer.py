import uuid

from kafka_client_lib.kafka_client import (
    get_producer
)


def publish_event(
        payload
):

    producer = (
        get_producer()
    )

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

    future = (

        producer.send(
            "orders",
            event
        )
    )

    future.get(
        timeout=10
    )

    producer.flush()

    producer.close()

    return event