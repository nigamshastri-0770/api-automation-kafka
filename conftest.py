from validators.contract_validator import ContractValidator


import pytest


@pytest.fixture
def validate_contract():

    def _validate(response, schema):

        payload = response.json()

        ContractValidator.validate_schema(
            payload,
            schema
        )

    return _validate