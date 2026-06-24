def validate_event(event, expected_type="ORDER_CREATED"):
    if not event:
        return False

    if "event_id" not in event:
        return False

    if event.get("type") != expected_type:
        return False

    return True