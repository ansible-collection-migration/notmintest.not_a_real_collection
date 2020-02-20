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
The module file for eos_lacp
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
module: eos_lacp
short_description: Manage Global Link Aggregation Control Protocol (LACP) on Arista EOS devices.
description:
  - This module manages Global Link Aggregation Control Protocol (LACP) on Arista EOS devices.
author: Nathaniel Case (@Qalthos)
notes:
- Tested against Arista EOS 4.20.10M
- This module works with connection C(network_cli). See the
  L(EOS Platform Options,../network/user_guide/platform_eos.html).
options:
  config:
    description: LACP global options.
    type: dict
    suboptions:
      system:
        description: LACP system options.
        type: dict
        suboptions:
          priority:
            description:
              - The system priority to use in LACP negotiations.
              - Lower value is higher priority.
              - Refer to vendor documentation for valid values.
            type: int
  state:
    description:
      - The state of the configuration after module completion.
    type: str
    choices:
    - merged
    - replaced
    - deleted
    default: merged
'''
EXAMPLES = """
# Using merged

# Before state:
# -------------
# veos# show running-config | include lacp
# lacp system-priority 10

- name: Merge provided global LACP attributes with device attributes
  eos_lacp:
    config:
      system:
        priority: 20
    state: merged

# After state:
# ------------
# veos# show running-config | include lacp
# lacp system-priority 20
#


# Using replaced

# Before state:
# -------------
# veos# show running-config | include lacp
# lacp system-priority 10

- name: Replace device global LACP attributes with provided attributes
  eos_lacp:
    config:
      system:
        priority: 20
    state: replaced

# After state:
# ------------
# veos# show running-config | include lacp
# lacp system-priority 20
#


# Using deleted

# Before state:
# -------------
# veos# show running-config | include lacp
# lacp system-priority 10

- name: Delete global LACP attributes
  eos_lacp:
    state: deleted

# After state:
# ------------
# veos# show running-config | include lacp
#


"""
RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['lacp system-priority 10']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.network.eos.argspec.lacp.lacp import LacpArgs
from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.network.eos.config.lacp.lacp import Lacp


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=LacpArgs.argument_spec,
                           supports_check_mode=True)

    result = Lacp(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
