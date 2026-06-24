import pytest


@pytest.fixture
def order_payload():

    return {

        "order_id":
            1001,

        "amount":
            500
    }