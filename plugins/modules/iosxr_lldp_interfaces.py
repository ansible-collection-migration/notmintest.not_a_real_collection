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
The module file for iosxr_lldp_interfaces
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
module: iosxr_lldp_interfaces
short_description: Manage Link Layer Discovery Protocol (LLDP) attributes of interfaces on IOS-XR devices.
description:
  - This module manages Link Layer Discovery Protocol (LLDP) attributes of interfaces on IOS-XR devices.
notes:
  - Tested against IOS-XR 6.1.3.
  - This module works with connection C(network_cli). See L(the IOS-XR Platform Options,../network/user_guide/platform_iosxr.html).
author: Nilashish Chakraborty (@nilashishc)
options:
  config:
    description: A dictionary of LLDP interfaces options.
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - Name/Identifier of the interface or Ether-Bundle.
        type: str
      destination:
        description:
          - Specifies LLDP destination configuration on the interface.
        suboptions:
          mac_address:
            description:
              - Specifies the LLDP destination mac address on the interface.
            type: str
            choices: ['ieee-nearest-bridge', 'ieee-nearest-non-tmpr-bridge']
        type: dict
      receive:
        description:
          - Enable/disable LLDP RX on an interface.
        type: bool
      transmit:
        description:
          - Enable/disable LLDP TX on an interface.
        type: bool
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
#
# ------------
# Before state
# ------------
#
#
# RP/0/RP0/CPU0:ios#sh run int
# Mon Aug 12 12:40:23.104 UTC
# interface TenGigE0/0/0/0
#  ipv4 address 192.0.2.11 255.255.255.192
# !
# interface preconfigure GigabitEthernet0/0/0/1
# !
# interface preconfigure GigabitEthernet0/0/0/2
# !
#
#

- name: Merge provided configuration with running configuration
  iosxr_lldp_interfaces:
    config:
      - name: GigabitEthernet0/0/0/1
        destination:
          mac_address: ieee-nearest-non-tmpr-bridge
        transmit: False

      - name: GigabitEthernet0/0/0/2
        destination:
          mac_address: ieee-nearest-bridge
        receive: False
    state: merged

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#
# "before": [
#        {
#            "name": "TenGigE0/0/0/0"
#        },
#        {
#            "name": "GigabitEthernet0/0/0/1"
#        },
#        {
#            "name": "GigabitEthernet0/0/0/2"
#        }
# ]
#
# "commands": [
#        "interface GigabitEthernet0/0/0/2",
#        "lldp destination mac-address ieee-nearest-non-tmpr-bridge",
#        "lldp transmit disable",
#        "interface GigabitEthernet0/0/0/1",
#        "lldp receive disable",
#        "lldp destination mac-address ieee-nearest-bridge"
# ]
#
# "after": [
#        {
#            "name": "TenGigE0/0/0/0"
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/1",
#            "receive": false
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-non-tmpr-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/2",
#            "transmit": false
#        }
# ]
#
#
# ------------
# After state
# ------------
#
#
# RP/0/RP0/CPU0:ios#sh run int
# Mon Aug 12 12:49:51.517 UTC
# interface TenGigE0/0/0/0
#  ipv4 address 192.0.2.11 255.255.255.192
# !
# interface preconfigure GigabitEthernet0/0/0/1
#  lldp
#   receive disable
#   destination mac-address
#    ieee-nearest-bridge
#   !
#  !
# !
# interface preconfigure GigabitEthernet0/0/0/2
#  lldp
#   transmit disable
#   destination mac-address
#    ieee-nearest-non-tmpr-bridge
#   !
#  !
# !
#
#


# Using replaced
#
#
# -------------
# Before state
# -------------
#
#
# RP/0/RP0/CPU0:ios#sh run int
# Mon Aug 12 12:49:51.517 UTC
# interface TenGigE0/0/0/0
#  ipv4 address 192.0.2.11 255.255.255.192
# !
# interface preconfigure GigabitEthernet0/0/0/1
#  lldp
#   receive disable
#   destination mac-address
#    ieee-nearest-bridge
#   !
#  !
# !
# interface preconfigure GigabitEthernet0/0/0/2
#  lldp
#   transmit disable
#   destination mac-address
#    ieee-nearest-non-tmpr-bridge
#   !
#  !
# !
#
#

- name: Replace existing LLDP configurations of specified interfaces with provided configuration
  iosxr_lldp_interfaces:
    config:
      - name: GigabitEthernet0/0/0/1
        destination:
          mac_address: ieee-nearest-non-tmpr-bridge
    state: replaced

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
# "before": [
#        {
#            "name": "TenGigE0/0/0/0"
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/1",
#            "receive": false
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-non-tmpr-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/2",
#            "transmit": false
#        }
# ]
#
#
# "commands": [
#        "interface GigabitEthernet0/0/0/1",
#        "no lldp receive disable",
#        "lldp destination mac-address ieee-nearest-non-tmpr-bridge"
# ]
#
#
# "after": [
#        {
#            "name": "TenGigE0/0/0/0"
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-non-tmpr-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/1"
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-non-tmpr-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/2",
#            "transmit": false
#        }
# ]
#
#
# ------------
# After state
# ------------
#
#
# RP/0/RP0/CPU0:ios#sh run int
# Mon Aug 12 13:02:57.062 UTC
# interface TenGigE0/0/0/0
#  ipv4 address 192.0.2.11 255.255.255.192
# !
# interface preconfigure GigabitEthernet0/0/0/1
#  lldp
#   destination mac-address
#    ieee-nearest-non-tmpr-bridge
#   !
#  !
# !
# interface preconfigure GigabitEthernet0/0/0/2
#  lldp
#   transmit disable
#   destination mac-address
#    ieee-nearest-non-tmpr-bridge
#   !
#  !
# !
#
#


# Using overridden
#
#
# -------------
# Before state
# -------------
#
#
# RP/0/RP0/CPU0:ios#sh run int
# Mon Aug 12 13:15:40.465 UTC
# interface TenGigE0/0/0/0
#  ipv4 address 192.0.2.11 255.255.255.192
# !
# interface preconfigure GigabitEthernet0/0/0/1
#  lldp
#   receive disable
#   destination mac-address
#    ieee-nearest-bridge
#   !
#  !
# !
# interface preconfigure GigabitEthernet0/0/0/2
#  lldp
#   transmit disable
#   destination mac-address
#    ieee-nearest-non-tmpr-bridge
#   !
#  !
# !
#
#

- name: Override the LLDP configurations of all the interfaces with provided configurations
  iosxr_lldp_interfaces:
    config:
      - name: GigabitEthernet0/0/0/1
        transmit: False
    state: overridden

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#
# "before": [
#        {
#            "name": "TenGigE0/0/0/0"
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/1",
#            "receive": false
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-non-tmpr-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/2",
#            "transmit": false
#        }
# ]
#
# "commands": [
#        "interface GigabitEthernet0/0/0/2",
#        "no lldp destination mac-address ieee-nearest-non-tmpr-bridge",
#        "no lldp transmit disable",
#        "interface GigabitEthernet0/0/0/1",
#        "no lldp destination mac-address ieee-nearest-bridge",
#        "no lldp receive disable",
#        "lldp transmit disable"
# ]
#
#
# "after": [
#        {
#            "name": "TenGigE0/0/0/0"
#        },
#        {
#            "name": "GigabitEthernet0/0/0/1",
#            "transmit": false
#        },
#        {
#            "name": "GigabitEthernet0/0/0/2"
#        }
# ]
#
#
# ------------
# After state
# ------------
#
#
# RP/0/RP0/CPU0:ios#sh run int
# Mon Aug 12 13:22:25.604 UTC
# interface TenGigE0/0/0/0
#  ipv4 address 192.0.2.11 255.255.255.192
# !
# interface preconfigure GigabitEthernet0/0/0/1
#  lldp
#   transmit disable
#  !
# !
# interface preconfigure GigabitEthernet0/0/0/2
# !
#
#


# Using deleted
#
#
# -------------
# Before state
# -------------
#
#
# RP/0/RP0/CPU0:ios#sh run int
# Mon Aug 12 13:26:21.498 UTC
# interface TenGigE0/0/0/0
#  ipv4 address 192.0.2.11 255.255.255.192
# !
# interface preconfigure GigabitEthernet0/0/0/1
#  lldp
#   receive disable
#   destination mac-address
#    ieee-nearest-bridge
#   !
#  !
# !
# interface preconfigure GigabitEthernet0/0/0/2
#  lldp
#   transmit disable
#   destination mac-address
#    ieee-nearest-non-tmpr-bridge
#   !
#  !
# !
#
#

- name: Delete LLDP configurations of all interfaces (Note - This won't delete the interfaces themselves)
  iosxr_lldp_interfaces:
    state: deleted

#
#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#
# "before": [
#        {
#            "name": "TenGigE0/0/0/0"
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/1",
#            "receive": false
#        },
#        {
#            "destination": {
#                "mac_address": "ieee-nearest-non-tmpr-bridge"
#            },
#            "name": "GigabitEthernet0/0/0/2",
#            "transmit": false
#        }
# ]
#
#
# "commands": [
#        "interface GigabitEthernet0/0/0/1",
#        "no lldp destination mac-address ieee-nearest-bridge",
#        "no lldp receive disable",
#        "interface GigabitEthernet0/0/0/2",
#        "no lldp destination mac-address ieee-nearest-non-tmpr-bridge",
#        "no lldp transmit disable"
# ]
#
#
# "after": [
#        {
#            "name": "TenGigE0/0/0/0"
#        },
#        {
#            "name": "GigabitEthernet0/0/0/1"
#        },
#        {
#            "name": "GigabitEthernet0/0/0/2"
#        }
# ]
#
#
# ------------
# After state
# ------------
#
#
# RP/0/RP0/CPU0:ios#sh run int
# Mon Aug 12 13:30:14.618 UTC
# interface TenGigE0/0/0/0
#  ipv4 address 192.0.2.11 255.255.255.192
# !
# interface preconfigure GigabitEthernet0/0/0/1
# !
# interface preconfigure GigabitEthernet0/0/0/2
# !
#
#

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
  sample: ['interface GigabitEthernet0/0/0/1', 'lldp destination mac-address ieee-nearest-non-tmpr-bridge', 'no lldp transmit disable']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.network.iosxr.argspec.lldp_interfaces.lldp_interfaces import Lldp_interfacesArgs
from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.network.iosxr.config.lldp_interfaces.lldp_interfaces import Lldp_interfaces


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [('state', 'merged', ('config',)),
                   ('state', 'replaced', ('config',)),
                   ('state', 'overridden', ('config',))]
    module = AnsibleModule(argument_spec=Lldp_interfacesArgs.argument_spec, required_if=required_if,
                           supports_check_mode=True)

    result = Lldp_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
