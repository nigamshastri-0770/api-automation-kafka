import time

from kafka_client_lib.kafka_client import (
    get_consumer
)

from config.setting import (
    KAFKA_TOPIC
)


def fetch_event(
        correlation_id=None,
        timeout=20
):

    consumer = get_consumer(
        KAFKA_TOPIC
    )

    start = time.time()

    while (
        time.time()
        -
        start
        <
        timeout
    ):

        records = consumer.poll(
            timeout_ms=1000
        )

        for _, msgs in records.items():

            for msg in msgs:

                event = msg.value

                if (
                    correlation_id
                    is None
                ):

                    return event

                if (
                    event.get(
                        "correlation_id"
                    )
                    ==
                    correlation_id
                ):

                    return event

    raise Exception(
        "Event not found"
    )


def fetch_latest_event(
        timeout=20
):

    return fetch_event(
        timeout=timeout
    )