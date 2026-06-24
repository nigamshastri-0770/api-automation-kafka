EVENT_SCHEMA = {

    "type": "object",

    "required": [
        "event_id",
        "correlation_id",
        "type",
        "payload"
    ],

    "properties": {

        "event_id": {
            "type": "string"
        },

        "correlation_id": {
            "type": "string"
        },

        "type": {
            "type": "string"
        },

        "payload": {
            "type": "object"
        }
    }
}