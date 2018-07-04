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
from . import link
from .schema import Schema


class Data(object):
    def __init__(self, data=None, status_code=201, schema=None):
        self.data = data
        self.status_code = status_code
        self.schema = schema if schema else Schema()

    def update(self):
        return self.follow('self')

    def follow(self, rel, payload=None):
        return self.schema.follow(rel, payload)

    def extract(self, key, session):
        return link.Link.create_data_schema(self.data[key], self.status_code, session)

    def extractList(self, key, session):
        payload = self.data[key]
        members = [link.Link.create_data_schema(data, self.status_code, session) for data in payload]
        schema = link.Link.create_schema(payload, session)
        return ListData(members, len(members), len(members), 0, self.status_code, schema)

    def show(self, rel):
        return self.schema.show(rel)

    def __getitem__(self, item):
        return self.data[item]

    def is_valid(self):
        return self.data is not None

    def __iter__(self):
        return iter(self.data.keys() if self.data else [])

    def __repr__(self):
        return "Data({}, {})".format(self.data, self.schema)


class ListData(object):
    def __init__(self, members, total, limit, offset, status_code, schema):
        self.members = members
        self.total = total
        self.limit = limit
        self.offset = offset
        self.status_code = status_code
        self.schema = schema

    def show(self, rel):
        return self.schema.show(rel)

    def follow(self, rel, payload=None):
        return self.schema.follow(rel, payload)

    def __iter__(self):
        return iter(self.members)

    def __repr__(self):
        return "ListData({}, {})".format(self.members, self.schema)
