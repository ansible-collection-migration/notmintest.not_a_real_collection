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
The module file for nxos_vlans
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'network'}


DOCUMENTATION = '''
---
module: nxos_vlans
short_description: Create VLAN and manage VLAN configurations on NX-OS Interfaces
description: This module creates and manages VLAN configurations on Cisco NX-OS Interfaces.
author: Trishna Guha (@trishnaguha)
notes:
  - Tested against NXOS 7.3.(0)D1(1) on VIRL
options:
  config:
    description: A dictionary of Vlan options
    type: list
    suboptions:
      vlan_id:
        description:
          - Vlan ID.
        type: int
        required: true
      name:
        description:
          - Name of VLAN.
        type: str
      state:
        description:
          - Manage operational state of the vlan.
        type: str
        choices: ['active', 'suspend']
      enabled:
        description:
          - Manage administrative state of the vlan.
        type: bool
      mode:
        description:
          - Set vlan mode to classical ethernet or fabricpath.
            This is a valid option for Nexus 5000, 6000 and 7000 series.
        type: str
        choices: ['ce','fabricpath']
      mapped_vni:
        description:
          - The Virtual Network Identifier (VNI) ID that is mapped to the
            VLAN.
        type: int
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

# Before state:
# -------------
# vlan 1

- name: Merge provided configuration with device configuration.
  nxos_vlans:
    config:
      - vlan_id: 5
        name: test-vlan5
      - vlan_id: 10
        enabled: False
    state: merged

# After state:
# ------------
# vlan 5
#   name test-vlan5
#   state active
#   no shutdown
# vlan 10
#   state active
#   shutdown


# Using replaced

# Before state:
# -------------
# vlan 1
# vlan 5
#   name test-vlan5
# vlan 10
#   shutdown

- name: Replace device configuration of specified vlan with provided configuration.
  nxos_vlans:
    config:
      - vlan_id: 5
        name: test-vlan
        enabled: False
      - vlan_id: 10
        enabled: False
    state: replaced

# After state:
# ------------
# vlan 1
# vlan 5
#   name test-vlan
#   state active
#   shutdown
# vlan 10
#   state active
#   shutdown


# Using overridden

# Before state:
# -------------
# vlan 1
# vlan 3
#   name testing
# vlan 5
#   name test-vlan5
#   shutdown
# vlan 10
#   shutdown

- name: Override device configuration of all vlans with provided configuration.
  nxos_vlans:
    config:
      - vlan_id: 5
        name: test-vlan
      - vlan_id: 10
        state: active
    state: overridden

# After state:
# ------------
# vlan 1
# vlan 5
#   name test-vlan
#   state active
#   no shutdown
# vlan 10
#   state active
#   no shutdown


# Using deleted

# Before state:
# -------------
# vlan 1
# vlan 5
# vlan 10

- name: Delete vlans.
  nxos_vlans:
    config:
      - vlan_id: 5
      - vlan_id: 10
    state: deleted

# After state:
# ------------
# vlan 1


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
  sample: ['vlan 5', 'name test-vlan5', 'state suspend']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.network.nxos.argspec.vlans.vlans import VlansArgs
from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.network.nxos.config.vlans.vlans import Vlans


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=VlansArgs.argument_spec,
                           supports_check_mode=True)

    result = Vlans(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
