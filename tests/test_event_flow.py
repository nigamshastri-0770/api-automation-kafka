import allure

from producers.event_producer import publish_event
from consumers.event_consumer import fetch_event
from validators.event_validator import EventValidator


@allure.feature(
    "Kafka Event Flow"
)

@allure.story(
    "Publish and consume event"
)

def test_order_event(
        order_payload
):

    with allure.step(
            "Publish Event"
    ):

        produced = publish_event(
            order_payload
        )

    with allure.step(
            "Consume Event"
    ):

        consumed = fetch_event(

            produced[
                "correlation_id"
            ]
        )

    with allure.step(
            "Validate Event"
    ):

        assert EventValidator.validate(
            consumed
        )