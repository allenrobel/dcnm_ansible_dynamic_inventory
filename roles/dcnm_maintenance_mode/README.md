# Usage for playbooks/roles/dcnm_maintenance_mode

## Setup fabrics

```bash
export ANSIBLE_INVENTORY=/path/to/dynamic_inventory_env.py
export ND_TESTCASE=00_setup_fabrics_1x_rw
ansible-playbook dcnm_tests.yaml -i $ANSIBLE_INVENTORY
```

## Role-specific environment variables

### ND_TESTCASE

One of the following

- 00_setup_fabrics_1x_rw
- 00_setup_fabrics_2x_rw
- 01_merged_maintenance_mode_deploy_no_wait_switch_level
- 02_merged_normal_mode_deploy_no_wait_switch_level
- 03_merged_maintenance_mode_deploy_no_wait_top_level
- 04_merged_normal_mode_deploy_no_wait_top_level
- 05_merged_maintenance_mode_deploy_wait_top_level
- 06_merged_normal_mode_deploy_wait_top_level
- 07_merged_maintenance_mode_deploy_wait_switch_level
- 08_merged_normal_mode_deploy_wait_switch_level
- 09_merged_maintenance_mode_no_deploy

## Modifications to dcnm_tests.yaml

Set the following as desired for your testcases

```yaml
  vars:
    fabric_name_1: VXLAN_EVPN_Fabric
    fabric_type_1: VXLAN_EVPN
    fabric_name_2: VXLAN_EVPN_MSD_Fabric
    fabric_type_2: VXLAN_EVPN_MSD
    fabric_name_3: LAN_CLASSIC_Fabric
    fabric_type_3: LAN_CLASSIC
    fabric_name_4: IPFM_Fabric
    fabric_type_4: IPFM
```
