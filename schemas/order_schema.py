ORDER_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "order_id": {
            "type": "integer"
        },
        "status": {
            "type": "string"
        },
        "amount": {
            "type": "number"
        },
        "customer": {
            "type": "string"
        }
    },
    "required": [
        "order_id",
        "status",
        "amount",
        "customer"
    ]
}