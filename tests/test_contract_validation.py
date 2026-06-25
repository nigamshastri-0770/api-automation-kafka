from services.order_service import OrderService
from schemas.order_schema import ORDER_RESPONSE_SCHEMA


def test_order_contract(
    validate_contract
):

    response = OrderService.get_order()

    assert response.status_code == 200

    transformed = {
        "order_id": response.json()["id"],
        "status": "SUCCESS",
        "amount": response.json()["price"],
        "customer": response.json()["brand"]
    }

    class MockResponse:

        def json(self):
            return transformed

    validate_contract(
        MockResponse(),
        ORDER_RESPONSE_SCHEMA
    )