#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for vyos_lag_interfaces
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'network'
}

DOCUMENTATION = '''
---
module: vyos_lag_interfaces
short_description: Manages attributes of link aggregation groups on VyOS network devices.
description: This module manages attributes of link aggregation groups on VyOS network devices.
notes:
  - Tested against VyOS 1.1.8 (helium).
  - This module works with connection C(network_cli). See L(the VyOS OS Platform Options,../network/user_guide/platform_vyos.html).
author: Rohit Thakur (@rohitthakur2590)
options:
  config:
    description: A list of link aggregation group configurations.
    type: list
    suboptions:
      name:
        description:
          - Name of the link aggregation group (LAG) or bond.
        type: str
        required: True
      mode:
        description:
          - LAG or bond mode.
        type: str
        choices:
          - 802.3ad
          - active-backup
          - broadcast
          - round-robin
          - transmit-load-balance
          - adaptive-load-balance
          - xor-hash
      members:
        description:
          - List of member interfaces for the LAG (bond).
        type: list
        suboptions:
          member:
            description:
              - Name of the member interface.
            type: str
      primary:
        description:
          - Primary device interfaces for the LAG (bond).
        type: str
      hash_policy:
        description:
          - LAG or bonding transmit hash policy.
        type: str
        choices:
          - layer2
          - layer2+3
          - layer3+4
      arp_monitor:
        description:
          - ARP Link monitoring parameters.
        type: dict
        suboptions:
          interval:
            description:
              - ARP link monitoring frequency in milliseconds.
            type: int
          target:
            description:
              -  IP address to use for ARP monitoring.
            type: list
  state:
    description:
      - The state of the configuration after module completion.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged

'''
EXAMPLES = """
# Using merged
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration  commands | grep bond
# set interfaces bonding bond2
# set interfaces bonding bond3
#
- name: Merge provided configuration with device configuration
  vyos_lag_interfaces:
    config:
      - name: bond2
        mode: active-backup
        members:
         - member: eth2
         - member: eth1
        hash_policy: layer2
        primary: eth2

      - name: 'bond3'
        mode: 'active-backup'
        hash_policy: 'layer2+3'
        members:
         - member: eth3
        primary: 'eth3'
    state: merged
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": [
#        {
#            "name": "bond2"
#        },
#        {
#            "name": "bond3"
#        }
#    ],
#
# "commands": [
#        "set interfaces bonding bond2 hash-policy 'layer2'",
#        "set interfaces bonding bond2 mode 'active-backup'",
#        "set interfaces ethernet eth2 bond-group bond2",
#        "set interfaces ethernet eth1 bond-group bond2",
#        "set interfaces bonding bond2 primary 'eth2'",
#        "set interfaces bonding bond3 hash-policy 'layer2+3'",
#        "set interfaces bonding bond3 mode 'active-backup'",
#        "set interfaces ethernet eth3 bond-group bond3",
#        "set interfaces bonding bond3 primary 'eth3'"
#    ]
#
#     "after": [
#        {
#            "hash_policy": "layer2",
#            "members": [
#                {
#                    "member": "eth1"
#                },
#                {
#                    "member": "eth2"
#                }
#            ],
#            "mode": "active-backup",
#            "name": "bond2",
#            "primary": "eth2"
#        },
#        {
#            "hash_policy": "layer2+3",
#            "members": [
#                {
#                    "member": "eth3"
#                }
#            ],
#            "mode": "active-backup",
#            "name": "bond3",
#            "primary": "eth3"
#        }
#    ]
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration  commands | grep bond
# set interfaces bonding bond2 hash-policy 'layer2'
# set interfaces bonding bond2 mode 'active-backup'
# set interfaces bonding bond2 primary 'eth2'
# set interfaces bonding bond3 hash-policy 'layer2+3'
# set interfaces bonding bond3 mode 'active-backup'
# set interfaces bonding bond3 primary 'eth3'
# set interfaces ethernet eth1 bond-group 'bond2'
# set interfaces ethernet eth2 bond-group 'bond2'
# set interfaces ethernet eth3 bond-group 'bond3'


# Using replaced
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration  commands | grep bond
# set interfaces bonding bond2 hash-policy 'layer2'
# set interfaces bonding bond2 mode 'active-backup'
# set interfaces bonding bond2 primary 'eth2'
# set interfaces bonding bond3 hash-policy 'layer2+3'
# set interfaces bonding bond3 mode 'active-backup'
# set interfaces bonding bond3 primary 'eth3'
# set interfaces ethernet eth1 bond-group 'bond2'
# set interfaces ethernet eth2 bond-group 'bond2'
# set interfaces ethernet eth3 bond-group 'bond3'
#
- name: Replace device configurations of listed LAGs with provided configurations
  vyos_lag_interfaces:
    config:
      - name: bond3
        mode: '802.3ad'
        hash_policy: 'layer2'
        members:
         - member: eth3
    state: replaced
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": [
#        {
#            "hash_policy": "layer2",
#            "members": [
#                {
#                    "member": "eth1"
#                },
#                {
#                    "member": "eth2"
#                }
#            ],
#            "mode": "active-backup",
#            "name": "bond2",
#            "primary": "eth2"
#        },
#        {
#            "hash_policy": "layer2+3",
#            "members": [
#                {
#                    "member": "eth3"
#                }
#            ],
#            "mode": "active-backup",
#            "name": "bond3",
#            "primary": "eth3"
#        }
#    ],
#
# "commands": [
#        "delete interfaces bonding bond3 primary",
#        "set interfaces bonding bond3 hash-policy 'layer2'",
#        "set interfaces bonding bond3 mode '802.3ad'"
#    ],
#
# "after": [
#        {
#            "hash_policy": "layer2",
#            "members": [
#                {
#                    "member": "eth1"
#                },
#                {
#                    "member": "eth2"
#                }
#            ],
#            "mode": "active-backup",
#            "name": "bond2",
#            "primary": "eth2"
#        },
#        {
#            "hash_policy": "layer2",
#            "members": [
#                {
#                    "member": "eth3"
#                }
#            ],
#            "mode": "802.3ad",
#            "name": "bond3"
#        }
#    ],
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration  commands | grep bond
# set interfaces bonding bond2 hash-policy 'layer2'
# set interfaces bonding bond2 mode 'active-backup'
# set interfaces bonding bond2 primary 'eth2'
# set interfaces bonding bond3 hash-policy 'layer2'
# set interfaces bonding bond3 mode '802.3ad'
# set interfaces ethernet eth1 bond-group 'bond2'
# set interfaces ethernet eth2 bond-group 'bond2'
# set interfaces ethernet eth3 bond-group 'bond3'


# Using overridden
#
# Before state
# --------------
#
# vyos@vyos:~$ show configuration  commands | grep bond
# set interfaces bonding bond2 hash-policy 'layer2'
# set interfaces bonding bond2 mode 'active-backup'
# set interfaces bonding bond2 primary 'eth2'
# set interfaces bonding bond3 hash-policy 'layer2'
# set interfaces bonding bond3 mode '802.3ad'
# set interfaces ethernet eth1 bond-group 'bond2'
# set interfaces ethernet eth2 bond-group 'bond2'
# set interfaces ethernet eth3 bond-group 'bond3'
#
- name: Overrides all device configuration with provided configuration
  vyos_lag_interfaces:
    config:
      - name: bond3
        mode: active-backup
        members:
         - member: eth1
         - member: eth2
         - member: eth3
        primary: eth3
        hash_policy: layer2
    state: overridden
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": [
#        {
#            "hash_policy": "layer2",
#            "members": [
#                {
#                    "member": "eth1"
#                },
#                {
#                    "member": "eth2"
#                }
#            ],
#            "mode": "active-backup",
#            "name": "bond2",
#            "primary": "eth2"
#        },
#        {
#            "hash_policy": "layer2",
#            "members": [
#                {
#                    "member": "eth3"
#                }
#            ],
#            "mode": "802.3ad",
#            "name": "bond3"
#        }
#    ],
#
#    "commands": [
#        "delete interfaces bonding bond2 hash-policy",
#        "delete interfaces ethernet eth1 bond-group bond2",
#        "delete interfaces ethernet eth2 bond-group bond2",
#        "delete interfaces bonding bond2 mode",
#        "delete interfaces bonding bond2 primary",
#        "set interfaces bonding bond3 mode 'active-backup'",
#        "set interfaces ethernet eth1 bond-group bond3",
#        "set interfaces ethernet eth2 bond-group bond3",
#        "set interfaces bonding bond3 primary 'eth3'"
#    ],
#
# "after": [
#        {
#            "name": "bond2"
#        },
#        {
#            "hash_policy": "layer2",
#            "members": [
#                {
#                    "member": "eth1"
#                },
#                {
#                    "member": "eth2"
#                },
#                {
#                    "member": "eth3"
#                }
#            ],
#            "mode": "active-backup",
#            "name": "bond3",
#            "primary": "eth3"
#        }
#    ],
#
#
# After state
# ------------
#
# vyos@vyos:~$ show configuration  commands | grep bond
# set interfaces bonding bond2
# set interfaces bonding bond3 hash-policy 'layer2'
# set interfaces bonding bond3 mode 'active-backup'
# set interfaces bonding bond3 primary 'eth3'
# set interfaces ethernet eth1 bond-group 'bond3'
# set interfaces ethernet eth2 bond-group 'bond3'
# set interfaces ethernet eth3 bond-group 'bond3'


# Using deleted
#
# Before state
# -------------
#
# vyos@vyos:~$ show configuration  commands | grep bond
# set interfaces bonding bond2 hash-policy 'layer2'
# set interfaces bonding bond2 mode 'active-backup'
# set interfaces bonding bond2 primary 'eth2'
# set interfaces bonding bond3 hash-policy 'layer2+3'
# set interfaces bonding bond3 mode 'active-backup'
# set interfaces bonding bond3 primary 'eth3'
# set interfaces ethernet eth1 bond-group 'bond2'
# set interfaces ethernet eth2 bond-group 'bond2'
# set interfaces ethernet eth3 bond-group 'bond3'
#
- name: Delete LAG attributes of given interfaces (Note This won't delete the interface itself)
  vyos_lag_interfaces:
    config:
      - name: bond2
      - name: bond3
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
# "before": [
#        {
#            "hash_policy": "layer2",
#            "members": [
#                {
#                    "member": "eth1"
#                },
#                {
#                    "member": "eth2"
#                }
#            ],
#            "mode": "active-backup",
#            "name": "bond2",
#            "primary": "eth2"
#        },
#        {
#            "hash_policy": "layer2+3",
#            "members": [
#                {
#                    "member": "eth3"
#                }
#            ],
#            "mode": "active-backup",
#            "name": "bond3",
#            "primary": "eth3"
#        }
#    ],
# "commands": [
#        "delete interfaces bonding bond2 hash-policy",
#        "delete interfaces ethernet eth1 bond-group bond2",
#        "delete interfaces ethernet eth2 bond-group bond2",
#        "delete interfaces bonding bond2 mode",
#        "delete interfaces bonding bond2 primary",
#        "delete interfaces bonding bond3 hash-policy",
#        "delete interfaces ethernet eth3 bond-group bond3",
#        "delete interfaces bonding bond3 mode",
#        "delete interfaces bonding bond3 primary"
#    ],
#
# "after": [
#        {
#            "name": "bond2"
#        },
#        {
#            "name": "bond3"
#        }
#    ],
#
# After state
# ------------
# vyos@vyos:~$ show configuration  commands | grep bond
# set interfaces bonding bond2
# set interfaces bonding bond3


"""
RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample:
    - 'set interfaces bonding bond2'
    - 'set interfaces bonding bond2 hash-policy layer2'
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.network.vyos.argspec.lag_interfaces. \
    lag_interfaces import Lag_interfacesArgs
from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.network.vyos.config.lag_interfaces.lag_interfaces import Lag_interfaces


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [('state', 'merged', ('config',)),
                   ('state', 'replaced', ('config',)),
                   ('state', 'overridden', ('config',))]
    module = AnsibleModule(argument_spec=Lag_interfacesArgs.argument_spec, required_if=required_if,
                           supports_check_mode=True)

    result = Lag_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
