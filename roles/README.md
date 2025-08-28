# Example usage for playbooks/roles/*

```bash
export ND_ROLES_HOME=$HOME/ansible/playbooks/roles
export ANSIBLE_INVENTORY=$ND_ROLES_HOME/dynamic_inventory_env.py
cd $ND_ROLES_HOME/roles/dcnm_fabric
ansible-playbook playbook_merged_dcnm.yaml -i $ANSIBLE_INVENTORY
```

## dynamic inventory

These roles use a dynamic inventory generated with playbooks/roles/dynamic_inventory_env.py.

This inventory script expects the following environment variables to be defined.

If an environment variable is not defined, and a default is defined below, then the script assigns that default.

## Environment variables used in most roles

### ND_IP4

- The IPv4 address of the ND/NDFC controller
- Roles
  - all

### ND_PASSWORD

- The password for the ND/NDFC controller
- Roles
  - dcnm_bootflash
    - ``switch_password``
  - dcnm_image_policy
    - ``switch_password``
  - dcnm_image_upgrade
    - ``switch_password``
  - dcnm_maintenance_mode
    - ``nxos_password``

### ND_TESTCASE

- The testcase to run
- Roles
  - all
- Playbooks
  - dcnm_*/dcnm_tests.yaml
- Notes
  - See README.md in each role directory for list of testcases for that role

### ND_USERNAME

- The username for the ND/NDFC controller
- Default
  - admin
- Roles
  - dcnm_bootflash
    - ``switch_username``
  - dcnm_image_policy
    - ``switch_username``
  - dcnm_image_upgrade
    - ``switch_username``
  - dcnm_maintenance_mode
    - ``nxos_username``

## Environment variables used in a subset of roles

### ND_BGW_1_IP4

- The IPv4 address of the first BGW switch
- Default
  - 10.1.1.1
- Roles
  - Currently none

### ND_BGW_2_IP4

- The IPv4 address of the second BGW switch
- Default
  - 10.1.1.2
- Roles
  - Currently none

### ND_LEAF_1_IP4

- The IPv4 address of the first leaf switch
- Default
  - 10.1.1.5
- Sets Ansible vars
  - ``leaf1``
  - ``leaf_1``
- Roles
  - ``dcnm_fabric`` deploy testcases only
    - ``dcnm_fabric_merged_save_deploy_ipfm``
      - ``leaf_1``
    - ``dcnm_fabric_merged_save_deploy``
      - ``leaf_1``
    - ``dcnm_fabric_replaced_save_deploy``
      - ``leaf_1``
    - ``dcnm_fabric_replaced_save_deploy_ipfm``
      - ``leaf_1``
    - ``dcnm_maintenance_mode``
      - All testcases
        - ``leaf_1``
      - ``00_setup_fabrics_2x_rw``
        - ``leaf_1``
    - ``dcnm_image_upgrade``
      - ``01_setup_add_switches_to_fabric``
        - reads ``leaf1`` to set ``ansible_switch_1``
      - ``deleted_1x_switch``
        - reads ``leaf1`` to set ``ansible_switch_1``
      - ``deleted``
        - reads ``leaf1`` to set ``ansible_switch_1``
      - ``merged_global_config``
        - reads ``leaf1`` to set ``ansible_switch_1``
      - ``merged_override_global_config_1x_switch``
        - reads ``leaf1`` to set ``ansible_switch_1``
      - ``merged_override_global_config``
        - reads ``leaf1`` to set ``ansible_switch_1``
      - ``query``
        - reads ``leaf1`` to set ``ansible_switch_1``

### ND_LEAF_2_IP4

- The IPv4 address of the second leaf switch
- Default
  - 10.1.1.6
- Sets Ansible vars
  - ``leaf2``
  - ``leaf_2``
- Roles
  - ``dcnm_fabric`` deploy testcases only
    - ``dcnm_fabric_merged_save_deploy``
      - ``leaf_2``
    - ``dcnm_fabric_replaced_save_deploy``
      - ``leaf_2``
    - ``dcnm_maintenance_mode``
      - All testcases
        - ``leaf_2``
    - ``dcnm_image_upgrade``
      - ``01_setup_add_switches_to_fabric``
        - reads ``leaf2`` to set ``ansible_switch_2``
      - ``deleted``
        - reads ``leaf2`` to set ``ansible_switch_2``
      - ``merged_global_config``
        - reads ``leaf2`` to set ``ansible_switch_2``
      - ``merged_override_global_config``
        - reads ``leaf2`` to set ``ansible_switch_2``
      - ``query``
        - reads ``leaf2`` to set ``ansible_switch_2``

### ND_LEAF_3_IP4

- The IPv4 address of the third leaf switch
- Default
  - 10.1.1.7
- Roles
  - Currently none

### ND_LEAF_4_IP4

- The IPv4 address of the fourth leaf switch
- Default
  - 10.1.1.8
- Roles
  - Currently none

### ND_SPINE_1_IP4

- The IPv4 address of the first spine switch
- Default
  - 10.1.1.3
- Sets ansible vars
  - ``spine1``
- Roles
  - ``dcnm_image_upgrade``
    - ``01_setup_add_switches_to_fabric``
      - reads ``spine1`` to set ``ansible_switch_3``
    - ``deleted``
      - reads ``spine1`` to set ``ansible_switch_3``
    - ``merged_global_config``
      - reads ``spine1`` to set ``ansible_switch_3``
    - ``merged_override_global_config``
      - reads ``spine1`` to set ``ansible_switch_3``
    - ``query``
      - reads ``spine1`` to set ``ansible_switch_3``
- Playbooks
  - ``dcnm_image_upgrade/dcnm_tests.yaml`` (``spine1``)

### ND_SPINE_2_IP4

- The IPv4 address of the second spine switch
- Default
  - 10.1.1.4
- Sets ansible vars
  - ``spine2``
- Roles
  - Currently none
- Playbooks
  - Currently none

### ND_SWITCH_1_IP4

- The IPv4 address of the first switch
- Roles
  - ``dcnm_bootflash`` (reads ``switch1``)
- Playbooks
  - ``dcnm_bootflash/create_files.yaml`` (``switch1``)
  - ``dcnm_bootflash/delete_files.yaml`` (``switch1``)
  - ``dcnm_bootflash/dcnm_tests.yaml`` (``switch1``)

### ND_SWITCH_2_IP4

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
export ND_IP4=10.1.1.1
export ND_PASSWORD=my_nd_password
export ND_TESTCASE=dcnm_fabric_merged_basic
export ND_USERNAME=my_nd_username
export NXOS_PASSWORD=my_nxos_password
export NXOS_USERNAME=my_nxos_username
export ND_BGW_1_IP4=10.1.1.2
export ND_BGW_2_IP4=10.1.1.3
export ND_LEAF_1_IP4=10.1.1.4
export ND_LEAF_2_IP4=10.1.1.5
export ND_LEAF_3_IP4=10.1.1.6
export ND_LEAF_4_IP4=10.1.1.7
export ND_SPINE_1_IP4=10.1.1.8
export ND_SPINE_2_IP4=10.1.1.9
export ND_SWITCH_1_IP4=10.1.1.4
export ND_SWITCH_2_IP4=10.1.1.5
```
