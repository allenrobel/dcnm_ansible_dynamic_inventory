#!/usr/bin/env python3
import json
from os import environ
ndfc_ip4 = environ.get("NDFC_IP4")
ndfc_password = environ.get("NDFC_PASSWORD")
ndfc_username = environ.get("NDFC_USERNAME", "admin")
nxos_password = environ.get("NXOS_PASSWORD")
nxos_username = environ.get("NXOS_USERNAME", "admin")
spine_1 = environ.get("NDFC_SPINE_1")
spine_2 = environ.get("NDFC_SPINE_2")
leaf_1 = environ.get("NDFC_LEAF_1")
leaf_2 = environ.get("NDFC_LEAF_2")
leaf_3 = environ.get("NDFC_LEAF_3")
leaf_4 = environ.get("NDFC_LEAF_4")
switch_1 = environ.get("NDFC_SWITCH_1")
switch_2 = environ.get("NDFC_SWITCH_2")

output = {
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "ungrouped",
            "ndfc",
            "nxos"
        ],
        "vars": {
            "ansible_httpapi_use_ssl": "true",
            "ansible_httpapi_validate_certs": "false",
            "ansible_password": ndfc_password,
            "ansible_python_interpreter": "python",
            "ansible_user": ndfc_username,
            "switch_username": nxos_username,
            "switch_password": nxos_password,
            "nxos_username": nxos_username,
            "nxos_password": nxos_password,
            "switch1": switch_1,
            "switch2": switch_2,
            "spine1": spine_1,
            "spine2": spine_2,
            "leaf1": leaf_1,
            "leaf2": leaf_2,
            "leaf3": leaf_3,
            "leaf4": leaf_4
        }
    },
    "ndfc": {
        "hosts": [
            ndfc_ip4
        ],
        "vars": {
            "ansible_connection": "ansible.netcommon.httpapi",
            "ansible_network_os": "cisco.dcnm.dcnm"
        }
    },
    "nxos": {
        "children": [
            "spine1",
            "spine2",
            "leaf1",
            "leaf2",
            "leaf3",
            "leaf4",
            "switch1",
            "switch2"
        ],
        "vars": {
            "ansible_become": "true",
            "ansible_become_method": "enable",
            "ansible_connection": "ansible.netcommon.network_cli",
            "ansible_network_os": "cisco.nxos.nxos"
        }
    },
    "spine1": {
        "hosts": [
            spine_1
        ]
    },
    "spine2": {
        "hosts": [
            spine_2
        ]
    },
    "leaf1": {
        "hosts": [
            leaf_1
        ]
    },
    "leaf2": {
        "hosts": [
            leaf_2
        ]
    },
    "leaf3": {
        "hosts": [
            leaf_3
        ]
    },
    "leaf4": {
        "hosts": [
            leaf_4
        ]
    },
    "switch1": {
        "hosts": [
            switch_1
        ]
    },
    "switch2": {
        "hosts": [
            switch_2
        ]
    }
}

print(json.dumps(output))
