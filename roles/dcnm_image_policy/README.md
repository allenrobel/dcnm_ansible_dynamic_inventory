# Usage for playbooks/roles/dcnm_image_policy

## Test image policy deletion

```bash
export ANSIBLE_INVENTORY=/path/to/dynamic_inventory_env.py
export NDFC_TESTCASE=dcnm_image_policy_deleted
ansible-playbook dcnm_tests.yaml -i $ANSIBLE_INVENTORY
```

## Role-specific environment variables

### NDFC_TESTCASE

- One of the following
    - dcnm_image_policy_deleted
    - dcnm_image_policy_deleted_all_policies
    - dcnm_image_policy_merged
    - dcnm_image_policy_overridden
    - dcnm_image_policy_query
    - dcnm_image_policy_replaced

## Modifications to dcnm_tests.yaml

- Set the following as desired for your testcases

```yaml
  vars:
    image_policy_1: "KR5M"
    image_policy_2: "NR1F"
    epld_image_1: n9000-epld.10.2.5.M.img
    epld_image_2: n9000-epld.10.3.1.F.img
    nxos_image_1: n9000-dk9.10.2.5.M.bin
    nxos_image_2: n9000-dk9.10.3.1.F.bin
    nxos_release_1: 10.2.5_nxos64-cs_64bit
    nxos_release_2: 10.3.1_nxos64-cs_64bit
```
