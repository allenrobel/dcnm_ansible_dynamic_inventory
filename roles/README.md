# Usage for playbooks/roles/*

## dynamic inventory

These roles use a dynamic inventory generated with playbooks/roles/dynamic_inventory_env.py.

This inventory script expects the following environment variables to be defined.

If an environment variable is not defined, and a default is defined below, then the script assigns that default.

#### NDFC_IP4

- The IPv4 address of your NDFC/ND controller
- Roles
    - all

#### NDFC_PASSWORD

- The password for your NDFC/ND controller
- Roles
    - all

#### NDFC_USERNAME

- The username for your NDFC/ND controller
- Default
    - admin
- Roles
    - all

#### NXOS_PASSWORD

- Sets both nxos_password and switch_password Ansible vars
- The password for any NXOS switches
- Roles
    - dcnm_bootflash (read as switch_password)
    - dcnm_image_policy (read as switch_password)
    - dcnm_image_upgrade (read as switch_password)
    - dcnm_maintenance_mode (read as nxos_password)

#### NXOS_USERNAME

- The username for any NXOS switches
- Sets both nxos_username and switch_username Ansible vars
- Default
    - admin
- Roles
    - dcnm_bootflash (read as switch_username)
    - dcnm_image_policy (read as switch_username)
    - dcnm_image_upgrade (read as switch_username)
    - dcnm_maintenance_mode (read as nxos_username)

