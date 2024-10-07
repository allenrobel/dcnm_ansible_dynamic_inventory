# Usage for playbooks/roles/*

## dynamic inventory

This role uses two dynamic inventories.

 - See ../README.md for the first inventory.
 - See below for the second inventory.
 
The second inventory is in the current directory.

- roles/dcnm_bootflash/local_inventory.py

It expects the following environment vars to be set.

### SWITCH_1

- The IPv4 address of the first switch

### SWITCH_2

- The IPv4 address of the second switch
