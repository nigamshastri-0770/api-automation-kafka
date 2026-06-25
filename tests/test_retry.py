from producers.event_producer import (
    publish_event
)


def test_retry():

    payload = {

        "order_id": 200,

        "amount": 900
    }

    result = (
        publish_event(
            payload
        )
    )

    assert result