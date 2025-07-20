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

import json
from os import environ

"""
# Summary
Dynamic inventory for DCNM Collection integration tests. Inventory
is built from environment variables.

## Usage

### Mandatory general variables

The following general environment variables are related
to credentials, controller reachability, and role/testcase
assignment.  These should be considered mandatory; though
the NXOS_* variables are not strictly needed unless called
for by the specific role/testcase.

Values below are examples, and should be modified for your
setup and the roles/testcases you are running.

```bash
export ND_ROLE=dcnm_vrf         # The role to run
export ND_TESTCASE=query        # The testcase to run
export ND_IP4=10.1.1.1          # Controller IPv4 address
export ND_PASSWORD=MyPassword   # Controller password
export ND_USERNAME=admin        # Controller username
export NXOS_PASSWORD=MyPassword # Switch password
export NXOS_USERNAME=admin      # Switch username
```

### Fabrics

We can add more fabrics later as the need arises...

```bash
export ND_FABRIC_1=MyFabric1   # Assigned to var fabric_1
export ND_FABRIC_2=MyFabric2   # Assigned to var fabric_2
export ND_FABRIC_3=MyFabric3   # Assigned to var fabric_3

```

### Interfaces

Interface usage varies by testcase.  See individual
testcase YAML files for details regarding each test's
usage.

#### Interface naming convention

##### Environment variables

ND_INTERFACE_[A][b]

Where:

A - The number of the switch to which the interface belongs
b - An incrementing lower-case letter in range a-z

###### Examples:

```bash
export ND_INTERFACE_1a=Ethernet1/1
export ND_INTERFACE_2a=Ethernet1/1
export ND_INTERFACE_2b=Ethernet1/2
export ND_INTERFACE_3a=Ethernet2/4
```

Above:

- switch_1 has one interface; Ethernet1/1
- switch_2 two interfaces; Ethernet1/1 and Ethernet1/2
- switch_3 has one interface; Ethernet2/4

##### Test case variables

Interface variables within test cases follow the same convention
as above, but are lowercase, and remove the leading ND_.

###### Examples

interface_1a - 1st interface on switch_1
interface_1b - 2st interface on switch_1
etc...
"""
nd_role = environ.get("ND_ROLE", "dcnm_vrf")
nd_testcase = environ.get("ND_TESTCASE", "query")

fabric_1 = environ.get("ND_FABRIC_1")
test_fabric = environ.get("ND_FABRIC_1") # For dcnm_network tests
nd_ip4 = environ.get("ND_IP4")
nd_password = environ.get("ND_PASSWORD")
nd_testcase = environ.get("ND_TESTCASE")
nd_username = environ.get("ND_USERNAME", "admin")
nxos_password = environ.get("NXOS_PASSWORD")
nxos_username = environ.get("NXOS_USERNAME", "admin")

# Base set of switches
bgw_1 = environ.get("ND_BGW_1_IP4", "172.22.150.112")
bgw_2 = environ.get("ND_BGW_2_IP4", "172.22.150.113")
leaf_1 = environ.get("ND_LEAF_1_IP4", "172.22.150.103")
leaf_2 = environ.get("ND_LEAF_2_IP4", "172.22.150.104")
leaf_3 = environ.get("ND_LEAF_3_IP4", "172.22.150.105")
leaf_4 = environ.get("ND_LEAF_4_IP4", "172.22.150.109")
spine_1 = environ.get("ND_SPINE_1_IP4", "172.22.150.112")
spine_2 = environ.get("ND_SPINE_2_IP4", "172.22.150.113")

# Placeholders if you'd rather directly set each of
# the switch vars instead of setting the switch vars
# from the switch roles above.
switch_1 = environ.get("ND_SWITCH_1_IP4", "172.22.150.112")
switch_2 = environ.get("ND_SWITCH_2_IP4", "172.22.150.113")
switch_3 = environ.get("ND_SWITCH_3_IP4", "172.22.150.103")
switch_4 = environ.get("ND_SWITCH_4_IP4", "172.22.150.104")

# Base set of interfaces
interface_1a = environ.get("ND_INTERFACE_1a", "Ethernet1/1")
interface_1b = environ.get("ND_INTERFACE_1b", "Ethernet1/2")
interface_1c = environ.get("ND_INTERFACE_1c", "Ethernet1/3")
interface_1d = environ.get("ND_INTERFACE_1d", "Ethernet1/4")
interface_2a = environ.get("ND_INTERFACE_2a", "Ethernet1/1")
interface_2b = environ.get("ND_INTERFACE_2b", "Ethernet1/2")
interface_2c = environ.get("ND_INTERFACE_2c", "Ethernet1/3")
interface_2d = environ.get("ND_INTERFACE_2d", "Ethernet1/4")
interface_3a = environ.get("ND_INTERFACE_3a", "Ethernet1/3")

# -----------------
# dcnm_vrf
# -----------------
if nd_role == "dcnm_vrf":
    vrf_1 = environ.get("ND_VRF_1", "vrf-1")
    vrf_2 = environ.get("ND_VRF_2", "vrf-2")
    # VXLAN/EVPN Fabric Name
    # fabric_1
    #   - all tests
    # switch_1
    #   - all tests
    #     - vrf capable
    # switch_2
    #   - all tests
    #     - vrf-lite capable
    # switch_3
    #   - merged
    #     - NOT vrf-lite capable
    # interface_1a
    #   - no tests
    # interface_2a
    #   - [deleted, merged, overridden, query, replaced, vrf_lite]
    #     - switch_2 VRF LITE extensions
    # interface_2b
    #   - [vrf_lite]
    #      - switch_2 VRF LITE extensions
    # interface_3a
    #   - [merged, vrf_lite]
    #     - switch_3 non-vrf-lite capable switch
    #
elif nd_role == "vrf_lite":
    # VXLAN/EVPN Fabric Name
    # Uses fabric_1
    # switch_1: vrf-lite capable
    switch_1 = spine_1
    # switch_2: vrf-lite capable
    switch_2 = spine_2
    # switch_3: vrf capable
    switch_3 = bgw_1
elif nd_role == "scale":
    pass
elif nd_role == "dcnm_network":
    switch_1 = leaf_1
    switch_2 = leaf_2
    interface_1a = environ.get("ND_INTERFACE_1a", "Ethernet1/1")
    interface_1b = environ.get("ND_INTERFACE_1b", "Ethernet1/2")
    interface_1c = environ.get("ND_INTERFACE_1c", "Ethernet1/3")
    interface_1d = environ.get("ND_INTERFACE_1d", "Ethernet1/4")
    interface_2a = environ.get("ND_INTERFACE_2a", "Ethernet1/1")
    interface_2b = environ.get("ND_INTERFACE_2b", "Ethernet1/2")
    interface_2c = environ.get("ND_INTERFACE_2c", "Ethernet1/3")
    interface_2d = environ.get("ND_INTERFACE_2d", "Ethernet1/4")
    vrf_1 = environ.get("ND_VRF_1", "vrf-1")
    vrf_2 = environ.get("ND_VRF_2", "vrf-2")
else:
    switch_1 = leaf_1
    switch_2 = spine_1
    switch_3 = bgw_1
    switch_4 = bgw_2
    vrf_1 = environ.get("ND_VRF_1", "vrf-1")
    vrf_2 = environ.get("ND_VRF_2", "vrf-2")

# output is printed to STDOUT, where ansible-playbook -i reads it.
# If you change any vars above, be sure to add them below.
# We'll clean this up as the integration test vars are standardized.

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
            "fabric_1": fabric_1,
            "test_fabric": test_fabric,
            "testcase": nd_testcase,
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
            "switch_1": switch_1,
            "switch_2": switch_2,
            "switch_3": switch_3,
            "switch_4": switch_4,
            "ansible_switch1": switch_1,
            "ansible_switch2": switch_2,
            "interface_1a": interface_1a,
            "interface_1b": interface_1b,
            "interface_1c": interface_1c,
            "interface_1d": interface_1d,
            "interface_2a": interface_2a,
            "interface_2b": interface_2b,
            "interface_2c": interface_2c,
            "interface_2d": interface_2d,
            "interface_3a": interface_3a,
            "vrf_1": vrf_1,
            "vrf_2": vrf_2,
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
            "switch3",
            "switch4",
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
    "switch3": {"hosts": [switch_3]},
    "switch4": {"hosts": [switch_4]},
}

print(json.dumps(output, indent=4, sort_keys=True))
