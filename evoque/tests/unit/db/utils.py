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

"""Evoque test utilities."""

from evoque.db import api as db_api


# Tickets
def ticket_create(context):
    values = {"name": "test-ticket"}
    ticket = db_api.ticket_create(context, values)
    return ticket


def ticket_list(context):
    tickets = db_api.ticket_get_all(context)
    return tickets


# Workflows
def workflow_create(context):
    values = {"name": "test-workflow"}
    workflow = db_api.workflow_create(context, values)
    return workflow


def workflow_list(context):
    workflows = db_api.workflow_get_all(context)
    return workflows
