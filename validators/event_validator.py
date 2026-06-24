from jsonschema import validate

from schemas.event_schema import (
    EVENT_SCHEMA
)


class EventValidator:

    @staticmethod
    def validate(event):

        validate(
            event,
            EVENT_SCHEMA
        )

        return True