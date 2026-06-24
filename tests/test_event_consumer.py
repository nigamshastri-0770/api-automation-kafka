from producers.event_producer import publish_event
from consumers.event_consumer import fetch_latest_event
from utils.validator import validate_event


def test_event_flow():
    payload = {
        "order_id": 101,
        "amount": 500
    }

    publish_event(payload)

    consumed = fetch_latest_event(timeout=15)

    assert validate_event(consumed)
    assert consumed["payload"]["order_id"] == 101
    assert consumed["payload"]["amount"] == 500