# Usage for playbooks/roles/*

## dynamic inventory

These roles use a dynamic inventory generated with ``playbooks/roles/dynamic_inventory_env.py``.

``dynamic_inventory_env.py`` expects the following environment variables to be defined.

If an environment variable is not defined, and a default is defined below, then the script assigns that default.

## Environment variables used in most roles

### NDFC_IP4

- The IPv4 address of the ND/NDFC controller
- Roles
    - all

### NDFC_PASSWORD

- The password for the ND/NDFC controller
- Roles
    - all

### NDFC_TESTCASE

- The testcase to run
- Roles
    - all
- Playbooks
    - dcnm_*/dcnm_tests.yaml
- Notes
    - See README.md in each role directory for list of testcases for that role

### NDFC_USERNAME

- The username for the ND/NDFC controller
- Default
    - admin
- Roles
    - all

## Environment variables used in a subset of roles

### NDFC_BGW_1_IP4

- The IPv4 address of the first BGW switch
- Roles
    - Currently none

### NDFC_BGW_2_IP4

- The IPv4 address of the second BGW switch
- Roles
    - Currently none

### NDFC_LEAF_1_IP4

- The IPv4 address of the first leaf switch
- Sets Ansible vars
    - ``leaf1``
    - ``leaf_1``
- Roles
    - ``dcnm_maintenance_mode`` (reads into ``leaf_1``)
    - ``dcnm_image_upgrade`` (reads ``leaf1`` to set ``ansible_switch_1``)

### NDFC_LEAF_2_IP4

- The IPv4 address of the second leaf switch
- Sets Ansible vars
    - ``leaf2``
    - ``leaf_2``
- Roles
    - ``dcnm_maintenance_mode`` (reads ``leaf_2``)
    - ``dcnm_image_upgrade`` (reads ``leaf2`` to set ``ansible_switch_2``)

### NDFC_LEAF_3_IP4

- The IPv4 address of the third leaf switch
- Roles
    - Currently none

### NDFC_LEAF_4_IP4

- The IPv4 address of the fourth leaf switch
- Roles
    - Currently none

### NDFC_SPINE_1_IP4

- The IPv4 address of the first spine switch
- Sets ansible vars
    - ``spine1``
- Roles
    - ``dcnm_image_upgrade`` (reads ``spine1`` to set ``ansible_switch_3``)
- Playbooks
    - ``dcnm_image_upgrade/dcnm_tests.yaml`` (``spine1``)

### NDFC_SWITCH_1_IP4

- The IPv4 address of the first switch
- Roles
    - ``dcnm_bootflash`` (reads ``switch1``)
- Playbooks
    - ``dcnm_bootflash/create_files.yaml`` (``switch1``)
    - ``dcnm_bootflash/delete_files.yaml`` (``switch1``)
    - ``dcnm_bootflash/dcnm_tests.yaml`` (``switch1``)

### NDFC_SWITCH_2_IP4

- The IPv4 address of the second switch
- Roles
    - dcnm_bootflash (reads into ``switch2``)
- Playbooks
    - ``dcnm_bootflash/create_files.yaml`` (``switch2``)
    - ``dcnm_bootflash/delete_files.yaml`` (``switch2``)
    - ``dcnm_bootflash/dcnm_tests.yaml`` (``switch2``)


### NXOS_PASSWORD

- The password for NX-OS switches
- Sets both ``nxos_password`` and ``switch_password`` Ansible vars
- Roles
    - dcnm_bootflash (``switch_password``)
    - dcnm_image_policy (``switch_password``)
    - dcnm_image_upgrade (``switch_password``)
    - dcnm_maintenance_mode (``nxos_password``)


### NXOS_USERNAME
- The username for NX-OS switches
- Sets both ``nxos_username`` and ``switch_username`` Ansible vars
- Default
    - admin
- Roles
    - dcnm_bootflash (``switch_username``)
    - dcnm_image_policy (``switch_username``)
    - dcnm_image_upgrade (``switch_username``)
    - dcnm_maintenance_mode (``nxos_username``)

## Example for bash shells

```bash
export NDFC_IP4=10.1.1.1
export NDFC_PASSWORD=my_ndfc_password
export NDFC_TESTCASE=dcnm_fabric_merged_basic
export NDFC_USERNAME=my_ndfc_username
export NXOS_PASSWORD=my_nxos_password
export NXOS_USERNAME=my_nxos_username
export NDFC_BGW_1_IP4=10.1.1.2
export NDFC_BGW_2_IP4=10.1.1.3
export NDFC_LEAF_1_IP4=10.1.1.4
export NDFC_LEAF_2_IP4=10.1.1.5
export NDFC_LEAF_3_IP4=10.1.1.6
export NDFC_LEAF_4_IP4=10.1.1.7
export NDFC_SPINE_1_IP4=10.1.1.8
export NDFC_SPINE_2_IP4=10.1.1.9
export NDFC_SWITCH_1_IP4=10.1.1.4
export NDFC_SWITCH_2_IP4=10.1.1.5
```
