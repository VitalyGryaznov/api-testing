import pytest
from jsonschema import validate, ValidationError
def assert_status_code_equals(response, status_code: int):
    assert response.status_code == status_code


def assert_data_equals(response, data):
    assert response.json() == data


def validate_with_json_schema(response, schema):
    try:
        validate(instance=response.json(), schema=schema)
    except ValidationError as e:
        pytest.fail(f"Response schema validation failed: {e}")