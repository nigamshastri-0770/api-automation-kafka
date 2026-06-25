from jsonschema import validate
from jsonschema.exceptions import ValidationError


class ContractValidator:

    @staticmethod
    def validate_schema(response_data, schema):

        try:
            validate(
                instance=response_data,
                schema=schema
            )

            return True

        except ValidationError as e:
            raise AssertionError(
                f"\nContract Validation Failed\n{e}"
            )