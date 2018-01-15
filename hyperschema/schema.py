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

from . import link, data


class Schema(object):
    def __init__(self, links_node=None, session=None):
        if links_node is not None:
            self.links = {
                link_data['rel']: link.Link(
                    link_data['href'],
                    link_data['method'],
                    link_data['schema'] if 'schema' in link_data else None,
                    link_data['targetSchema'] if 'targetSchema' in link_data else None,
                    session
                ) for link_data in links_node}
        else:
            self.links = {}

    def show(self, rel):
        return self.links[rel] if rel in self.links else None

    def follow(self, rel, payload=None):
        if rel in self.links:
            return self.links[rel].follow(payload)
        else:
            return data.Data()

    def __repr__(self):
        return "Schema(rels=[" + ", ".join(self.links.keys()) + "])"
