# Usage for playbooks/roles/dcnm_fabric

## Test basic fabric deletion

```bash
export ANSIBLE_INVENTORY=/path/to/dynamic_inventory_env.py
export NDFC_TESTCASE=dcnm_fabric_deleted_basic
ansible-playbook dcnm_tests.yaml -i $ANSIBLE_INVENTORY
```

## Role-specific environment variables

### NDFC_TESTCASE

One of the following

- dcnm_fabric_deleted_basic
- dcnm_fabric_deleted_basic_ipfm
- dcnm_fabric_deleted_basic_isn
- dcnm_fabric_deleted_basic_lan_classic
- dcnm_fabric_deleted_basic_msd
- dcnm_fabric_deleted_basic_vxlan
- dcnm_fabric_merged_basic
- dcnm_fabric_merged_basic_ipfm
- dcnm_fabric_merged_basic_isn
- dcnm_fabric_merged_save_deploy
- dcnm_fabric_merged_save_deploy_ipfm
- dcnm_fabric_replaced_basic
- dcnm_fabric_replaced_basic_ipfm
- dcnm_fabric_replaced_basic_isn
- dcnm_fabric_replaced_basic_vxlan
- dcnm_fabric_replaced_basic_vxlan_site_id
- dcnm_fabric_replaced_save_deploy
- dcnm_fabric_replaced_save_deploy_ipfm
- dcnm_fabric_query_basic.yaml

## Modifications to dcnm_tests.yaml

- Set the following as desired for your testcases

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
    fabric_name_5: ISN_Fabric
    fabric_type_5: ISN
```