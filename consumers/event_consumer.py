import time

from kafka_client_lib.kafka_client import (
    get_consumer
)

from config.setting import (
    KAFKA_TOPIC
)

from core.logger import (
    get_logger
)


logger = get_logger(
    __name__
)


def fetch_event(
        correlation_id=None,
        timeout=20
):

    consumer = None

    try:

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
                timeout_ms=3000
            )

            for _, msgs in records.items():

                for msg in msgs:

                    event = msg.value

                    logger.info(
                        f"Consumed: {event}"
                    )

                    print(
                        "RECEIVED:",
                        event
                    )

                    if correlation_id is None:

                        return event

                    if (

                        event.get(
                            "correlation_id"
                        )

                        ==

                        correlation_id
                    ):

                        logger.info(
                            "Matched event"
                        )

                        return event

        logger.warning(
            "Timeout waiting event"
        )

        raise Exception(
            "Event not found"
        )

    finally:

        if consumer:

            consumer.close()

            logger.info(
                "Consumer closed"
            )


def fetch_latest_event(
        timeout=20
):

    return fetch_event(
        timeout=timeout
    )