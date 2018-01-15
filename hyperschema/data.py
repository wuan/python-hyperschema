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

from .schema import Schema


class Data(object):
    def __init__(self, data=None, schema=None):
        self.data = data
        self.schema = schema if schema else Schema()

    def update(self):
        return self.follow('self')

    def follow(self, rel, payload=None):
        return self.schema.follow(rel, payload)

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
    def __init__(self, members, total, limit, offset, schema):
        self.members = members
        self.total = total
        self.limit = limit
        self.offset = offset
        self.schema = schema

    def show(self, rel):
        return self.schema.show(rel)

    def follow(self, rel, payload=None):
        return self.schema.follow(rel, payload)

    def __iter__(self):
        return iter(self.members)

    def __repr__(self):
        return "ListData({}, {})".format(self.members, self.schema)
