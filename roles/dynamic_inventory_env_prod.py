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
# pylint: disable=line-too-long,too-few-public-methods
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
export ND_DOMAIN=radius         # The controller login domain
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

from __future__ import absolute_import, division, print_function

__metaclass__ = type  # pylint: disable=invalid-name
__copyright__ = "Copyright (c) 2024 Cisco and/or its affiliates."
__author__ = "Allen Robel"

import json
from dataclasses import dataclass, field
from os import environ
from typing import Any


def _required(var_name, description) -> str:
    """Get required environment variable or raise ValueError."""
    value = environ.get(var_name)
    if not value:
        raise ValueError(f"{var_name} environment variable must be set to {description}")
    return value

def _default_children() -> list[str]:
    children: list[str] = []
    children.extend(["bgw_1", "bgw_2", "bgw1", "bgw2"])
    children.extend(["spine_1", "spine_2", "spine1", "spine2"])
    children.extend(["leaf_1", "leaf_2", "leaf_3", "leaf_4", "leaf1", "leaf2", "leaf3", "leaf4"])
    children.extend(["switch1", "switch2", "switch3", "switch4"])
    return children


@dataclass
class ConfigNdConnection:
    """
    # Summary

    Ansible connection-related attributes for Nexus Dashboard

    - use_ssl: ansible_httpapi_use_ssl
    - validate_certs: ansible_httpapi_validate_certs
    - connection: ansible_connection
    - network_os: ansible_network_os
    - nd_domain: ansible_httpapi_login_domain
    - nd_ip4: ND controller IP
    - nd_password: ansible_password
    - nd_username: ansible_user

    """
    use_ssl: bool = True
    validate_certs: bool = False
    connection: str = "ansible.netcommon.httpapi"
    network_os: str = "cisco.dcnm.dcnm"
    nd_domain: str = _required("ND_DOMAIN", "ND login domain e.g. 'local', 'radius', etc.")
    nd_ip4: str = _required("ND_IP4", "ND controller IP")
    nd_password: str = _required("ND_PASSWORD", "ND controller password")
    nd_username: str = environ.get("ND_USERNAME", "admin")


@dataclass
class ConfigNxosConnection:
    """
    # Summary

    Ansible connection-related attributes for NXOS switches.

    - become: ansible_become
    - become_method: ansible_become_method
    - connection: ansible_connection
    - network_os: ansible_network_os
    - nxos_password: switch password
    - nxos_username: switch username
    """
    become: bool = True
    become_method: str = "enable"
    connection: str = "ansible.netcommon.network_cli"
    network_os: str = "cisco.nxos.nxos"
    nxos_password: str = _required("NXOS_PASSWORD", "NXOS switch password")
    nxos_username: str = environ.get("NXOS_USERNAME", "admin")


@dataclass
class ConfigTestRunner:
    """Integration Test environment variable config container."""
    nd_role: str = _required("ND_ROLE", "integration test role name e.g. dcnm_vrf, dcnm_fabric_group, etc.")
    nd_testcase: str = _required("ND_TESTCASE", "integration test name e.g. test_fabric_query_basic")


@dataclass
class ConfigTestFabric:
    """Fabric environment variable config container."""
    fabric_1: str = environ.get("ND_FABRIC_1", "SITE1")
    fabric_2: str = environ.get("ND_FABRIC_2", "SITE2")
    fabric_3: str = environ.get("ND_FABRIC_3", "SITE3")


@dataclass
class ConfigTestFabricGroup:
    """Fabric Group environment variable config container."""
    fabric_group_1: str = environ.get("ND_FABRIC_GROUP_1", "MCFG1")
    fabric_group_2: str = environ.get("ND_FABRIC_GROUP_2", "MCFG2")
    fabric_group_3: str = environ.get("ND_FABRIC_GROUP_3", "MCFG3")

    fabric_type_1: str = environ.get("ND_FABRIC_TYPE_1", "MCFG")
    fabric_type_2: str = environ.get("ND_FABRIC_TYPE_2", "MCFG")
    fabric_type_3: str = environ.get("ND_FABRIC_TYPE_3", "MCFG")


@dataclass
class ConfigTestInterface:
    """
    # Summary

    Interface environment variable config container.

    ## Notes
    - interface_1a 
    - interface_1b
    - interface_2a: vrf-lite capable
    - interface_2b: vrf-lite capable
    - interface_3a
    """
    interface_1a: str = environ.get("ND_INTERFACE_1a", "Ethernet1/1")
    interface_1b: str = environ.get("ND_INTERFACE_1b", "Ethernet1/2")
    interface_2a: str = environ.get("ND_INTERFACE_2a", "Ethernet1/1")
    interface_2b: str = environ.get("ND_INTERFACE_2b", "Ethernet1/2")
    interface_3a: str = environ.get("ND_INTERFACE_3a", "Ethernet1/3")


@dataclass
class ConfigTestSwitch:
    """
    # Summary

    Switch IP environment variable config container.

    ## Notes

    - bgw_1: vrf capable
    - bgw_2: vrf capable
    - spine_1: vrf-lite capable
    - spine_2: vrf-lite capable
    """
    children: list[str] = field(default_factory=_default_children)
    bgw_1_ip4: str = environ.get("ND_BGW_1_IP4", "192.168.14.11")
    bgw_2_ip4: str = environ.get("ND_BGW_2_IP4", "192.168.14.12")
    spine_1_ip4: str = environ.get("ND_SPINE_1_IP4", "192.168.14.21")
    spine_2_ip4: str = environ.get("ND_SPINE_2_IP4", "192.168.14.22")
    leaf_1_ip4: str = environ.get("ND_LEAF_1_IP4", "192.168.14.51")
    leaf_2_ip4: str = environ.get("ND_LEAF_2_IP4", "192.168.14.52")
    leaf_3_ip4: str = environ.get("ND_LEAF_3_IP4", "192.168.14.53")
    leaf_4_ip4: str = environ.get("ND_LEAF_4_IP4", "192.168.14.54")


@dataclass
class ConfigTestSwitchBgw:
    """
    # Summary

    Border Gateway Switch IP environment variable config container.

    ## Notes

    - bgw_1: vrf capable
    - bgw_2: vrf incapable
    """
    switch_1_ip4: str = environ.get("ND_BGW_1_IP4", "192.168.14.11")
    switch_2_ip4: str = environ.get("ND_BGW_2_IP4", "192.168.14.12")


@dataclass
class ConfigTestSwitchSpine:
    """
    # Summary

    Spine switch IP environment variable config container.

    ## Notes

    - spine_1: vrf-lite capable
    - spine_2: vrf-lite capable
    """
    switch_1_ip4: str = environ.get("ND_SPINE_1_IP4", "192.168.14.21")
    switch_2_ip4: str = environ.get("ND_SPINE_2_IP4", "192.168.14.22")


@dataclass
class ConfigTestSwitchLeaf:
    """
    # Summary

    Leaf switch IP environment variable config container.
    """
    switch_1_ip4: str = environ.get("ND_LEAF_1_IP4", "192.168.14.51")
    switch_2_ip4: str = environ.get("ND_LEAF_2_IP4", "192.168.14.52")
    switch_3_ip4: str = environ.get("ND_LEAF_3_IP4", "192.168.14.53")
    switch_4_ip4: str = environ.get("ND_LEAF_4_IP4", "192.168.14.54")


@dataclass
class ConfigTestSwitchVrfCapable:
    """VRF capable switch environment variable config holder."""
    switch_1: str = environ.get("ND_BGW_1_IP4", "192.168.14.11")


@dataclass
class ConfigTestSwitchVrfLiteCapable:
    """VRF-Lite capable switch environment variable config holder."""
    switch_1: str = environ.get("ND_SPINE_1_IP4", "192.168.14.21")
    switch_2: str = environ.get("ND_SPINE_2_IP4", "192.168.14.22")


@dataclass
class ConfigTestSwitchVrfIncapable:
    """VRF incapable switch environment variable config holder."""
    switch_1: str = environ.get("ND_BGW_2_IP4", "192.168.14.12")


@dataclass
class ConfigTestVrf:
    """VRF environment variable config holder."""
    vrf_1: str = environ.get("ND_VRF_1", "vrf-1")
    vrf_2: str = environ.get("ND_VRF_2", "vrf-2")


def _ndfc_config() -> dict[str, Any]:
    return {
        "hosts": [ConfigNdConnection().nd_ip4],
        "vars": {
            "ansible_connection": ConfigNdConnection().connection,
            "ansible_network_os": ConfigNdConnection().network_os,
            "ansible_httpapi_login_domain": ConfigNdConnection().nd_domain,
        },
    }

def _nxos_config() -> dict[str, Any]:
    return {
        "children": _default_children(),
        "vars": {
            "ansible_become": ConfigNxosConnection().become,
            "ansible_become_method": ConfigNxosConnection().become_method,
            "ansible_connection": ConfigNxosConnection().connection,
            "ansible_network_os": ConfigNxosConnection().network_os,
        },
    }

@dataclass
class ConfigHostNdfc:
    """
    # Summary

    NDFC hosts environment variable config container.

    ## See Also

    _ndfc_config function.
    """
    output: dict[str, Any] = field(default_factory=_ndfc_config)


@dataclass
class ConfigHostsNxos:
    """
    # Summary

    NXOS hosts environment variable config container.

    ## See Also

    _nxos_config function.
    """
    output: dict[str, Any] = field(default_factory=_nxos_config)


@dataclass
class ConfigTestcaseDcnmNetwork:
    """dcnm_vrf testcase specific environment variable config holder."""
    _fabrics = ConfigTestFabric()
    _switches = ConfigTestSwitchLeaf()
    _vrfs = ConfigTestVrf()

    fabric_1: str = _fabrics.fabric_1
    interface_1a: str = environ.get("ND_INTERFACE_1a", "Ethernet1/1")
    interface_1b: str = environ.get("ND_INTERFACE_1b", "Ethernet1/2")
    interface_1c: str = environ.get("ND_INTERFACE_1c", "Ethernet1/3")
    interface_1d: str = environ.get("ND_INTERFACE_1d", "Ethernet1/4")
    interface_2a: str = environ.get("ND_INTERFACE_2a", "Ethernet1/1")
    interface_2b: str = environ.get("ND_INTERFACE_2b", "Ethernet1/2")
    interface_2c: str = environ.get("ND_INTERFACE_2c", "Ethernet1/3")
    interface_2d: str = environ.get("ND_INTERFACE_2d", "Ethernet1/4")
    switch_1: str = _switches.switch_1_ip4
    switch_2: str = _switches.switch_2_ip4
    vrf_1: str = _vrfs.vrf_1


@dataclass
class ConfigTestcaseDcnmVrf:
    """
    # Summary

    dcnm_vrf testcase specific environment variable config holder.

    ## Notes

    - VXLAN/EVPN Fabric Name
      - fabric_1
      - all tests
    - switch_1
       - vrf capable
       - all tests
    - switch_2
       - vrf-lite capable
       - all tests
    - switch_3
       - NOT vrf-lite capable
       - merged
    - interface_1a
       - no tests
    - interface_2a
       - [deleted, merged, overridden, query, replaced, vrf_lite]
       - switch_2 VRF LITE extensions
    - interface_2b
       - [vrf_lite]
       - switch_2 VRF LITE extensions
    - interface_3a
       - [merged, vrf_lite]
       - switch_3 non-vrf-lite capable switch
    """
    _fabrics = ConfigTestFabric()
    _vrf_capable_switches = ConfigTestSwitchVrfCapable()
    _vrf_lite_switches = ConfigTestSwitchVrfLiteCapable()
    _vrf_incapable_switches = ConfigTestSwitchVrfIncapable()
    _vrfs = ConfigTestVrf()

    fabric_1: str = _fabrics.fabric_1
    switch_1: str = _vrf_capable_switches.switch_1
    switch_2: str = _vrf_lite_switches.switch_1
    switch_3: str = _vrf_incapable_switches.switch_1
    vrf_1: str = _vrfs.vrf_1
    vrf_2: str = _vrfs.vrf_2


@dataclass
class ConfigTestcaseDcnmVrfLite:
    """
    # Summary

    dcnm_vrf testcase specific environment variable config holder.

    ## Notes

    - fabric_1: VXLAN/EVPN Fabric
    - switch_1: vrf-lite capable
    - switch_2: vrf-lite capable
    - switch_3: vrf capable
    """
    _fabrics = ConfigTestFabric()
    _vrf_capable_switches = ConfigTestSwitchVrfCapable()
    _vrf_lite_switches = ConfigTestSwitchVrfLiteCapable()
    _vrfs = ConfigTestVrf()

    fabric_1: str = _fabrics.fabric_1
    switch_1: str = _vrf_lite_switches.switch_1
    switch_2: str = _vrf_lite_switches.switch_2
    switch_3: str = _vrf_capable_switches.switch_1
    vrf_1: str = _vrfs.vrf_1
    vrf_2: str = _vrfs.vrf_2


config_nd_connection = ConfigNdConnection()
config_nxos_connection = ConfigNxosConnection()
config_test_runner = ConfigTestRunner()
config_test_fabric = ConfigTestFabric()
config_test_fabric_group = ConfigTestFabricGroup()
config_test_switch = ConfigTestSwitch()
config_test_switch_bgw = ConfigTestSwitchBgw()
config_test_switch_spine = ConfigTestSwitchSpine()
config_test_switch_leaf = ConfigTestSwitchLeaf()
config_test_vrf = ConfigTestVrf()

fabric_1 = config_test_fabric.fabric_1
fabric_name_1 = config_test_fabric.fabric_1
fabric_group_name_1 = config_test_fabric_group.fabric_group_1
fabric_group_type_1 = config_test_fabric_group.fabric_type_1
test_fabric = config_test_fabric.fabric_1  # For dcnm_network tests

# Base set of switches
bgw_1 = config_test_switch_bgw.switch_1_ip4
bgw_2 = config_test_switch_bgw.switch_2_ip4
leaf_1 = config_test_switch_leaf.switch_1_ip4
leaf_2 = config_test_switch_leaf.switch_2_ip4
leaf_3 = config_test_switch_leaf.switch_3_ip4
leaf_4 = config_test_switch_leaf.switch_4_ip4
spine_1 = config_test_switch_spine.switch_1_ip4
spine_2 = config_test_switch_spine.switch_2_ip4

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

testcase: object
role = config_test_runner.nd_role
match role:
    case "dcnm_vrf":
        testcase = ConfigTestcaseDcnmVrf()
        fabric_1 = testcase.fabric_1
        switch_1 = testcase.switch_1
        switch_2 = testcase.switch_2
        switch_3 = testcase.switch_3
        vrf_1 = testcase.vrf_1
        vrf_2 = testcase.vrf_2
    case "vrf_lite":
        testcase = ConfigTestcaseDcnmVrfLite()
        fabric_1 = testcase.fabric_1
        switch_1 = testcase.switch_1
        switch_2 = testcase.switch_2
        switch_3 = testcase.switch_3
        vrf_1 = testcase.vrf_1
        vrf_2 = ConfigTestVrf().vrf_2
    case "dcnm_network":
        testcase = ConfigTestcaseDcnmNetwork()
        fabric_1 = testcase.fabric_1
        interface_1a: str = testcase.interface_1a
        interface_1b: str = testcase.interface_1b
        interface_1c: str = testcase.interface_1c
        interface_1d: str = testcase.interface_1d
        interface_2a: str = testcase.interface_2a
        interface_2b: str = testcase.interface_2b
        interface_2c: str = testcase.interface_2c
        interface_2d: str = testcase.interface_2d
        switch_1 = testcase.switch_1
        switch_2 = testcase.switch_2
        vrf_1 = testcase.vrf_1
        vrf_2 = ConfigTestVrf().vrf_2
    case _:
        switch_1 = config_test_switch_leaf.switch_1_ip4
        switch_2 = config_test_switch_spine.switch_1_ip4
        switch_3 = config_test_switch_bgw.switch_1_ip4
        switch_4 = config_test_switch_bgw.switch_2_ip4
        vrf_1 = config_test_vrf.vrf_1
        vrf_2 = config_test_vrf.vrf_2

# output is printed to STDOUT, where ansible-playbook -i reads it.
# If you change any vars above, be sure to add them below.
# We'll clean this up as the integration test vars are standardized.

output = {
    "_meta": {"hostvars": {}},
    "all": {
        "children": ["ungrouped", "dcnm", "ndfc", "nxos"],
        "vars": {
            "ansible_httpapi_use_ssl": config_nd_connection.use_ssl,
            "ansible_httpapi_validate_certs": config_nd_connection.validate_certs,
            "ansible_password": config_nd_connection.nd_password,
            "ansible_python_interpreter": "python",
            "ansible_user": config_nd_connection.nd_username,
            "fabric_1": fabric_1,
            "fabric_name_1": fabric_name_1,
            "fabric_group_name_1": fabric_group_name_1,
            "fabric_group_type_1": fabric_group_type_1,
            "test_fabric": test_fabric,
            "testcase": config_test_runner.nd_testcase,
            "bgw1": config_test_switch_bgw.switch_1_ip4,
            "bgw2": config_test_switch_bgw.switch_2_ip4,
            "leaf1": config_test_switch_leaf.switch_1_ip4,
            "leaf2": config_test_switch_leaf.switch_2_ip4,
            "leaf_1": config_test_switch_leaf.switch_1_ip4,
            "leaf_2": config_test_switch_leaf.switch_2_ip4,
            "leaf3": config_test_switch_leaf.switch_3_ip4,
            "leaf4": config_test_switch_leaf.switch_4_ip4,
            "nxos_username": config_nxos_connection.nxos_username,
            "nxos_password": config_nxos_connection.nxos_password,
            "switch_password": config_nxos_connection.nxos_password,
            "switch_username": config_nxos_connection.nxos_username,
            "spine1": config_test_switch_spine.switch_1_ip4,
            "spine2": config_test_switch_spine.switch_2_ip4,
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
    "dcnm": ConfigHostNdfc().output,
    "ndfc": ConfigHostNdfc().output,
    "nxos": ConfigHostsNxos().output,
    "bgw_1": {"hosts": [config_test_switch_bgw.switch_1_ip4]},
    "bgw_2": {"hosts": [config_test_switch_bgw.switch_2_ip4]},
    "spine_1": {"hosts": [config_test_switch_spine.switch_1_ip4]},
    "spine_2": {"hosts": [config_test_switch_spine.switch_2_ip4]},
    "leaf_1": {"hosts": [config_test_switch_leaf.switch_1_ip4]},
    "leaf_2": {"hosts": [config_test_switch_leaf.switch_2_ip4]},
    "leaf_3": {"hosts": [config_test_switch_leaf.switch_3_ip4]},
    "leaf_4": {"hosts": [config_test_switch_leaf.switch_4_ip4]},
    "bgw1": {"hosts": [config_test_switch_bgw.switch_1_ip4]},
    "bgw2": {"hosts": [config_test_switch_bgw.switch_2_ip4]},
    "leaf1": {"hosts": [config_test_switch_leaf.switch_1_ip4]},
    "leaf2": {"hosts": [config_test_switch_leaf.switch_2_ip4]},
    "leaf3": {"hosts": [config_test_switch_leaf.switch_3_ip4]},
    "leaf4": {"hosts": [config_test_switch_leaf.switch_4_ip4]},
    "spine1": {"hosts": [config_test_switch_spine.switch_1_ip4]},
    "spine2": {"hosts": [config_test_switch_spine.switch_2_ip4]},
    "switch1": {"hosts": [config_test_switch_leaf.switch_1_ip4]},
    "switch2": {"hosts": [config_test_switch_leaf.switch_2_ip4]},
    "switch3": {"hosts": [config_test_switch_leaf.switch_3_ip4]},
    "switch4": {"hosts": [config_test_switch_leaf.switch_4_ip4]},
}

print(json.dumps(output, indent=4, sort_keys=True))
