#!/usr/bin/env python3
#
# Copyright (c) 2024 Cisco and/or its affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__copyright__ = "Copyright (c) 2024 Cisco and/or its affiliates."
__author__ = "Allen Robel"

"""
# Summary
Dynamic inventory for DCNM Collection integration tests. Inventory
is built from environment variables.

# Usage

See README.md in the top-level of this repository and define the environment
variables described there appropriately for your environment.
"""
import json
from os import environ

nd_ip4 = environ.get("ND_IP4")
nd_password = environ.get("ND_PASSWORD")
nd_testcase = environ.get("ND_TESTCASE")
nd_username = environ.get("ND_USERNAME", "admin")
nxos_password = environ.get("NXOS_PASSWORD")
nxos_username = environ.get("NXOS_USERNAME", "admin")
bgw_1 = environ.get("ND_BGW_1_IP4", "10.1.1.1")
bgw_2 = environ.get("ND_BGW_2_IP4", "10.1.1.2")
leaf_1 = environ.get("ND_LEAF_1_IP4", "10.1.1.5")
leaf_2 = environ.get("ND_LEAF_2_IP4", "10.1.1.6")
leaf_3 = environ.get("ND_LEAF_3_IP4", "10.1.1.7")
leaf_4 = environ.get("ND_LEAF_4_IP4", "10.1.1.8")
spine_1 = environ.get("ND_SPINE_1_IP4", "10.1.1.3")
spine_2 = environ.get("ND_SPINE_2_IP4", "10.1.1.4")
switch_1 = environ.get("ND_SWITCH_1_IP4", "10.1.1.5")
switch_2 = environ.get("ND_SWITCH_2_IP4", "10.1.1.3")

output = {
    "_meta": {"hostvars": {}},
    "all": {
        "children": ["ungrouped", "dcnm", "ndfc", "nxos"],
        "vars": {
            "ansible_httpapi_use_ssl": "true",
            "ansible_httpapi_validate_certs": "false",
            "ansible_password": nd_password,
            "ansible_python_interpreter": "python",
            "ansible_user": nd_username,
            "bgw1": bgw_1,
            "bgw2": bgw_2,
            "leaf1": leaf_1,
            "leaf2": leaf_2,
            "leaf_1": leaf_1,
            "leaf_2": leaf_2,
            "leaf3": leaf_3,
            "leaf4": leaf_4,
            "nxos_username": nxos_username,
            "nxos_password": nxos_password,
            "switch_password": nxos_password,
            "switch_username": nxos_username,
            "spine1": spine_1,
            "spine2": spine_2,
            "switch1": switch_1,
            "switch2": switch_2,
            "testcase": nd_testcase
        },
    },
    "dcnm": {
        "hosts": [nd_ip4],
        "vars": {
            "ansible_connection": "ansible.netcommon.httpapi",
            "ansible_network_os": "cisco.dcnm.dcnm",
        },
    },
    "ndfc": {
        "hosts": [nd_ip4],
        "vars": {
            "ansible_connection": "ansible.netcommon.httpapi",
            "ansible_network_os": "cisco.dcnm.dcnm",
        },
    },
    "nxos": {
        "children": [
            "bgw1",
            "bgw2",
            "leaf_1",
            "leaf_2",
            "leaf1",
            "leaf2",
            "leaf3",
            "leaf4",
            "spine1",
            "spine2",
            "switch1",
            "switch2",
        ],
        "vars": {
            "ansible_become": "true",
            "ansible_become_method": "enable",
            "ansible_connection": "ansible.netcommon.network_cli",
            "ansible_network_os": "cisco.nxos.nxos",
        },
    },
    "bgw1": {"hosts": [bgw_1]},
    "bgw2": {"hosts": [bgw_2]},
    "leaf_1": {"hosts": [leaf_1]},
    "leaf_2": {"hosts": [leaf_2]},
    "leaf1": {"hosts": [leaf_1]},
    "leaf2": {"hosts": [leaf_2]},
    "leaf3": {"hosts": [leaf_3]},
    "leaf4": {"hosts": [leaf_4]},
    "spine1": {"hosts": [spine_1]},
    "spine2": {"hosts": [spine_2]},
    "switch1": {"hosts": [switch_1]},
    "switch2": {"hosts": [switch_2]},
}

print(json.dumps(output))
