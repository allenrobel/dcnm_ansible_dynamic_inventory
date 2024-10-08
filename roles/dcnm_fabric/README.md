# Usage for playbooks/roles/dcnm_fabric

## Test basic fabric deletion

```bash
export ANSIBLE_INVENTORY=/path/to/dynamic_inventory_env.py
export NDFC_TESTCASE=dcnm_fabric_deleted_basic
ansible-playbook dcnm_tests.yaml -i $ANSIBLE_INVENTORY
```

## Role-specific environment variables

### NDFC_TESTCASE

- One of the following
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
