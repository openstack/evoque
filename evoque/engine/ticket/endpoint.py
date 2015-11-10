# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from evoque.db import api as db_api


class Handler(object):

    def __init__(self):
        super(Handler, self).__init__()

    def ticket_create(self, context, name):
        values = {'name': name}
        ticket = db_api.ticket_create(context, values)
        return {'ticket': ticket}
