# Usage for playbooks/roles/dcnm_image_upgrade

## Create fabric as first step in dcnm_image_upgrade testing

```bash
export ANSIBLE_INVENTORY=/path/to/dynamic_inventory_env.py
export ND_TESTCASE=00_setup_create_fabric
ansible-playbook dcnm_tests.yaml -i $ANSIBLE_INVENTORY
```

## Role-specific environment variables

### ND_LEAF_1_IP4
- Read into ansible_switch_1

### ND_LEAF_2_IP4
- Read into ansible_switch_2

### ND_SPINE_1_IP4
- Read into ansible_switch_3

### ND_TESTCASE

One of the following

- 00_setup_create_fabric
- 01_setup_add_switches_to_fabric
- 02_setup_replace_image_policies
- deleted
- deleted_1x_switch
- merged_global_config
- merged_override_global_config
- merged_override_global_config_1x_switch
- query

## Modifications to dcnm_tests.yaml

Set the following as desired for your testcases

```yaml
  vars:
    fabric_name: LAN_Classic_Fabric
    # for dcnm_image_policy and dcnm_image_upgrade roles
    image_policy_1: NR1F
    image_policy_2: NR2F
    # for dcnm_image_policy role
    # install_package_1 must be uploaded to the controller
    install_package_1: cfg_cmp-0.3.1.0-1.x86_64.rpm
    uninstall_package_1: mtx-grpctunnel-2.1.0.0-10.4.1.lib32_64_n9000
    epld_image_1: n9000-epld.10.3.1.F.img
    epld_image_2: n9000-epld.10.3.1.F.img
    nxos_image_1: nxos64-cs.10.3.1.F.bin
    nxos_image_2: nxos64-cs.10.3.2.F.bin
    nxos_release_1: 10.3.1_nxos64-cs_64bit
    nxos_release_2: 10.3.2_nxos64-cs_64bit
    # for dcnm_image_upgrade role
    fabric_name_1: "{{ fabric_name }}"
    ansible_switch_1: "{{ leaf1 }}"
    ansible_switch_2: "{{ leaf2 }}"
    ansible_switch_3: "{{ spine1 }}"
```
