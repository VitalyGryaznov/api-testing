import json
import os

import allure
import requests


class Object:
    URL = "{baseUrl}objects".format(baseUrl=os.getenv("BASE_URL"))

    @allure.step('Create new object')
    def create_object(self, payload):
        return requests.post(self.URL, json=payload)

    @allure.step('Get object by id')
    def get_object_by_id(self, object_id):
        return requests.get("{URL}/{id}".format(URL=self.URL, id=object_id))

    @allure.step('Get all objects')
    def get_all_objects(self):
        return requests.get(self.URL)


    @allure.step('delete object')
    def delete_object(self, object_id):
        return requests.delete("{URL}/{id}".format(URL=self.URL, id=object_id))