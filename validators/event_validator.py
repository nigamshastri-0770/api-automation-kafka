from jsonschema import validate
from schemas.event_schema import EVENT_SCHEMA


class EventValidator:

    @staticmethod
    def validate(data):

        validate(
            instance=data,
            schema=EVENT_SCHEMA
        )

        return True