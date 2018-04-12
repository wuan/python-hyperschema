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
import logging

from requests import Session

from . import data, schema

logger = logging.getLogger(__name__)

def create_dict(text):
    if text is not None and text != '':
        return json.loads(text)
    else:
        return {}


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
            logger.warning("ERROR: %s,  method %s, status %d: '%s'", self.href, self.method, response.status_code, response.text)
            response_data = {}
        else:
            logger.info("follow %s", self.href)
            response_data = create_dict(response.text)

        return self.create_data_schema(response_data, self.session)

    @classmethod
    def create_data_schema(self, payload, session):

        schema = self.create_schema(payload, session)
        if 'members' in payload:
            return data.ListData([self.create_data_schema(member, session) for member in payload['members']],
                                 payload['total'],
                                 payload['limit'], payload['offset'], schema)
        return data.Data(payload, schema)

    @classmethod
    def create_schema(self, payload, session):
        schema_object = schema.Schema(
            payload['_schema']['links'] if '_schema' in payload and 'links' in payload['_schema'] else None, session)
        if '_schema' in payload:
            del payload['_schema']
        return schema_object

    def __repr__(self):
        return "Link({}, method={})".format(self.href, self.method)
