# Usage for playbooks/roles/dcnm_fabrics_vrfs

## Test fabric_vrfs query

```bash
export ANSIBLE_INVENTORY=/path/to/dynamic_inventory_env.py
export ND_TESTCASE=dcnm_fabrics_vrfs_query
ansible-playbook dcnm_tests.yaml -i $ANSIBLE_INVENTORY
```

## Role-specific environment variables

### ND_TESTCASE

One of the following

- dcnm_fabrics_vrfs_query

## Modifications to dcnm_tests.yaml

- Set the following as desired for your testcases

```yaml
  vars:
    fabric_name: f1
```