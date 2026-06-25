import uuid

from kafka_client_lib.kafka_client import (
    get_producer
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


def publish_event(
        payload
):

    producer = None

    try:

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

        logger.info(
            f"Publishing event: {event}"
        )

        future = (

            producer.send(
                KAFKA_TOPIC,
                event
            )
        )

        metadata = future.get(
            timeout=10
        )

        logger.info(
            f"Published partition={metadata.partition}"
        )

        producer.flush()

        return event

    except Exception as e:

        logger.error(
            f"Producer failed: {str(e)}"
        )

        raise

    finally:

        if producer:

            producer.close()

            logger.info(
                "Producer closed"
            )