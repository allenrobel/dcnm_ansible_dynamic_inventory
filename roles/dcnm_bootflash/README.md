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

## Test file deletion for explicitly-named file

```bash
export ANSIBLE_INVENTORY=/path/to/dynamic_inventory_env.py
export NDFC_TESTCASE=dcnm_bootflash_deleted_specific
ansible-playbook dcnm_tests.yaml -i $ANSIBLE_INVENTORY
```

## Role-specific environment variables

### NDFC_SWITCH_1_IP4

- The IPv4 address of the first switch

### NDFC_SWITCH_2_IP4

- The IPv4 address of the second switch

### NDFC_TESTCASE

- One of the following
    - dcnm_bootflash_deleted_specific
    - dcnm_bootflash_deleted_wildcard
    - dcnm_bootflash_query_specific
    - dcnm_bootflash_query_wildcard

## Modifications to dcnm_tests.yaml

- No modifications are needed if default values are used.
- If it is desired to override environment variable values, uncomment and modify per below.
- If a change to filenames is desired, override the defaults per below.

```yaml
  vars:
    # Uncomment ONE testcase to override environment variable NDFC_TESTCASE
    # testcase: dcnm_bootflash_deleted_specific
    # testcase: dcnm_bootflash_deleted_wildcard
    # testcase: dcnm_bootflash_query_specific
    # testcase: dcnm_bootflash_query_wildcard
    # Uncomment to override environment variable NDFC_USERNAME
    # switch_username: my_switch_username
    # Uncomment to override environment variable NDFC_PASSWORD
    # switch_password: my_switch_password
    # Uncomment to override environment variable NDFC_SWITCH_1_IP4
    # switch1: 10.1.1.1
    # Uncomment to override environment variable NDFC_SWITCH_2_IP4
    # switch2: 10.1.1.2
    # The vars below are included in the role's defaults/main.yaml
    # If it is desired to override the defaults, uncomment and
    # modify these.
    # switch1_file1: air.ndfc_ut
    # switch1_file2: earth.ndfc_ut
    # switch1_file3: fire.ndfc_ut
    # switch1_file4: water.ndfc_ut
    # switch2_file1: black.ndfc_ut
    # switch2_file2: blue.ndfc_ut
    # switch2_file3: green.ndfc_ut
    # switch2_file4: red.ndfc_ut
    # wildcard_filepath: "*:/*.ndfc_ut"
```