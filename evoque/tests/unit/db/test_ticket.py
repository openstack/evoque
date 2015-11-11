# Copyright 2015 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Tests for manipulating Bays via the DB API"""

from evoque.tests.unit import base
from evoque.tests.unit.db import utils


class DBTicketTestCase(base.DBTestCase):

    def test_ticket_create(self):
        ticket = utils.ticket_create(self.context)
        self.assertEqual(ticket.name, 'test-ticket')
