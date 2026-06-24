from producers.event_producer import (
    publish_event
)

from consumers.event_consumer import (
    fetch_event
)

from validators.event_validator import (
    EventValidator
)


def test_order_event(
        order_payload
):

    produced = publish_event(
        order_payload
    )

    consumed = fetch_event(

        produced[
            "correlation_id"
        ]
    )

    assert (
        EventValidator
        .validate(
            consumed
        )
    )

    assert (

        consumed[
            "payload"
        ]
        ==
        order_payload

    )