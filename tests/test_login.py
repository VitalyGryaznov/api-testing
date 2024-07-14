from time import sleep
import os

import allure
import pytest

from api.object_endpoint import Object
from api.object_schemas import create_object_response_schema
from helpers.response_helpers import assert_status_code_equals, assert_data_equals, validate_with_json_schema
from helpers.test_data_helper import get_valid_object


@allure.feature('object')
@allure.story('create')
@pytest.mark.object
def test_create_and_get_by_id():
    """
    This test is creating object via post and verifies that I can get this object via get by id, and it contains
    valid data
    """
    with allure.step('creating a user'):
        payload = get_valid_object()
        object = Object()
        create_response = object.create_object(payload)
        assert_status_code_equals(create_response, 200)
        objectId = create_response.json()['id']
    with allure.step('getting a user by id and validating response'):
        get_by_id_response = object.get_object_by_id(objectId)
        assert_status_code_equals(get_by_id_response, 200)
        expected_response = payload.copy()
        expected_response['id'] = objectId
        assert_data_equals(get_by_id_response, expected_response)

@allure.feature('object')
@allure.story('create')
@pytest.mark.object
def test_create_validate_response_with_schema():
    """
    This test is creating object via post and verifies that response if fitting the schema
    """
    payload = get_valid_object()
    object = Object()
    create_response = object.create_object(payload)
    assert_status_code_equals(create_response, 200)
    validate_with_json_schema(create_response, create_object_response_schema)


@allure.feature('object')
@allure.story('delete')
@pytest.mark.object
def test_delete_and_get_by_id():
    """
    This test is deleting itme and trying to get it by id
    """
    payload = get_valid_object()
    object = Object()
    create_response = object.create_object(payload)
    objectId = create_response.json()['id']
    object.delete_object(objectId)
    get_by_id_response = object.get_object_by_id(objectId)
    assert_status_code_equals(get_by_id_response, 404)