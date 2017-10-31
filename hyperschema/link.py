"""
   Copyright 2017 Andreas Würl

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import json

from requests import Session

from .data import Data, ListData
from .schema import Schema


class Link(object):
    def __init__(self, href, method='GET', schema=None, target_schema=None, session=None):
        self.href = href
        self.method = method
        self.schema = schema
        self.target_schema = target_schema
        self.session = session if session else Session()

    def follow(self, payload=None):
        if self.method == 'GET':
            response = self.session.get(self.href)
        elif self.method == 'PUT':
            response = self.session.put(self.href, json=payload)
        elif self.method == 'POST':
            response = self.session.post(self.href, json=payload)
        elif self.method == 'DELETE':
            response = self.session.delete(self.href)
        else:
            raise ValueError("unhandled method type '{}'".format(self.method))

        if response.status_code > 299:
            print("ERROR: {} {} {}".format(self.href, self.method, response.status_code))
            print(response.text)
            data = {}
        else:
            print("follow", self.href)
            data = self.create_json(response.text)

        return self.create_data_schema(data, self.session)

    def create_json(self, text):
        if text is not None and text != '':
            return json.loads(text)
        else:
            return {}

    @classmethod
    def create_data_schema(self, data, session):

        schema = self.create_schema(data, session)
        if 'members' in data:
            return ListData([self.create_data_schema(member, session) for member in data['members']], data['total'],
                            data['limit'], data['offset'], schema)
        return Data(data, schema)

    @classmethod
    def create_schema(self, data, session):
        schema = Schema(data['_schema']['links'] if '_schema' in data and 'links' in data['_schema'] else None, session)
        if '_schema' in data:
            del data['_schema']
        return schema

    def __repr__(self):
        return "Link({}, method={})".format(self.href, self.method)
