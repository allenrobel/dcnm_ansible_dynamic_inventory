# Usage for playbooks/roles/dcnm_bootflash

## Create files on switch bootflash (in preparation for integration tests)

```bash
export ANSIBLE_INVENTORY=/path/to/dynamic_inventory_env.py
ansible-playbook create_files.yaml -i $ANSIBLE_INVENTORY 
```

## Remove files on switch bootflash (independently of integration tests)

```bash
export ANSIBLE_INVENTORY=/path/to/dynamic_inventory_env.py
ansible-playbook delete_files.yaml -i $ANSIBLE_INVENTORY 
```

## Test file deletion for explicitely-named file

```bash
export ANSIBLE_INVENTORY=/path/to/dynamic_inventory_env.py
export NDFC_TESTCASE=dcnm_bootflash_deleted_specific
ansible-playbook dcnm_tests.yaml -i $ANSIBLE_INVENTORY
```

## Role-specific environment variables

### SWITCH_1

- The IPv4 address of the first switch

### SWITCH_2

- The IPv4 address of the second switch

### NDFC_TESTCASE

- One of the following
    - dcnm_bootflash_deleted_specific
    - dcnm_bootflash_deleted_wildcard
    - dcnm_bootflash_query_specific
    - dcnm_bootflash_query_wildcard
