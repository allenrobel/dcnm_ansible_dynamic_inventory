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

ndfc_ip4 = environ.get("NDFC_IP4")
ndfc_password = environ.get("NDFC_PASSWORD")
ndfc_testcase = environ.get("NDFC_TESTCASE")
ndfc_username = environ.get("NDFC_USERNAME", "admin")
nxos_password = environ.get("NXOS_PASSWORD")
nxos_username = environ.get("NXOS_USERNAME", "admin")
bgw_1 = environ.get("NDFC_BGW_1_IP4")
bgw_2 = environ.get("NDFC_BGW_2_IP4")
leaf_1 = environ.get("NDFC_LEAF_1_IP4")
leaf_2 = environ.get("NDFC_LEAF_2_IP4")
leaf_3 = environ.get("NDFC_LEAF_3_IP4")
leaf_4 = environ.get("NDFC_LEAF_4_IP4")
spine_1 = environ.get("NDFC_SPINE_1_IP4")
spine_2 = environ.get("NDFC_SPINE_2_IP4")
switch_1 = environ.get("NDFC_SWITCH_1_IP4")
switch_2 = environ.get("NDFC_SWITCH_2_IP4")

output = {
    "_meta": {"hostvars": {}},
    "all": {
        "children": ["ungrouped", "dcnm", "ndfc", "nxos"],
        "vars": {
            "ansible_httpapi_use_ssl": "true",
            "ansible_httpapi_validate_certs": "false",
            "ansible_password": ndfc_password,
            "ansible_python_interpreter": "python",
            "ansible_user": ndfc_username,
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
            "testcase": ndfc_testcase
        },
    },
    "dcnm": {
        "hosts": [ndfc_ip4],
        "vars": {
            "ansible_connection": "ansible.netcommon.httpapi",
            "ansible_network_os": "cisco.dcnm.dcnm",
        },
    },
    "ndfc": {
        "hosts": [ndfc_ip4],
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
