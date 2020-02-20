#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_appengine_firewall_rule
description:
- A single firewall rule that is evaluated against incoming traffic and provides an
  action to take on matched requests.
short_description: Creates a GCP FirewallRule
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
    type: str
  description:
    description:
    - An optional string description of this rule.
    required: false
    type: str
  source_range:
    description:
    - IP address or range, defined using CIDR notation, of requests that this rule
      applies to.
    required: true
    type: str
  action:
    description:
    - The action to take if this rule matches.
    - 'Some valid choices include: "UNSPECIFIED_ACTION", "ALLOW", "DENY"'
    required: true
    type: str
  priority:
    description:
    - A positive integer that defines the order of rule evaluation.
    - Rules with the lowest priority are evaluated first.
    - A default rule at priority Int32.MaxValue matches all IPv4 and IPv6 traffic
      when no previous rule matches. Only the action of this rule can be modified
      by the user.
    required: false
    type: int
  project:
    description:
    - The Google Cloud Platform project to use.
    type: str
  auth_kind:
    description:
    - The type of credential used.
    type: str
    required: true
    choices:
    - application
    - machineaccount
    - serviceaccount
  service_account_contents:
    description:
    - The contents of a Service Account JSON file, either in a dictionary or as a
      JSON string that represents it.
    type: jsonarg
  service_account_file:
    description:
    - The path of a Service Account JSON file if serviceaccount is selected as type.
    type: path
  service_account_email:
    description:
    - An optional service account email address if machineaccount is selected and
      the user does not wish to use the default email.
    type: str
  scopes:
    description:
    - Array of scopes to be used
    type: list
  env_type:
    description:
    - Specifies which Ansible environment you're running this module within.
    - This should not be set unless you know what you're doing.
    - This only alters the User Agent string for any API requests.
    type: str
notes:
- 'API Reference: U(https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.firewall.ingressRules)'
- 'Official Documentation: U(https://cloud.google.com/appengine/docs/standard/python/creating-firewalls#creating_firewall_rules)'
- for authentication, you can set service_account_file using the C(gcp_service_account_file)
  env variable.
- for authentication, you can set service_account_contents using the C(GCP_SERVICE_ACCOUNT_CONTENTS)
  env variable.
- For authentication, you can set service_account_email using the C(GCP_SERVICE_ACCOUNT_EMAIL)
  env variable.
- For authentication, you can set auth_kind using the C(GCP_AUTH_KIND) env variable.
- For authentication, you can set scopes using the C(GCP_SCOPES) env variable.
- Environment variables values will only be used if the playbook values are not set.
- The I(service_account_email) and I(service_account_file) options are mutually exclusive.
'''

EXAMPLES = '''
- name: create a firewall rule
  gcp_appengine_firewall_rule:
    priority: 1000
    source_range: 10.0.0.0
    action: ALLOW
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
description:
  description:
  - An optional string description of this rule.
  returned: success
  type: str
sourceRange:
  description:
  - IP address or range, defined using CIDR notation, of requests that this rule applies
    to.
  returned: success
  type: str
action:
  description:
  - The action to take if this rule matches.
  returned: success
  type: str
priority:
  description:
  - A positive integer that defines the order of rule evaluation.
  - Rules with the lowest priority are evaluated first.
  - A default rule at priority Int32.MaxValue matches all IPv4 and IPv6 traffic when
    no previous rule matches. Only the action of this rule can be modified by the
    user.
  returned: success
  type: int
'''

################################################################################
# Imports
################################################################################

from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, replace_resource_dict
import json

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            description=dict(type='str'),
            source_range=dict(required=True, type='str'),
            action=dict(required=True, type='str'),
            priority=dict(type='int'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/cloud-platform']

    state = module.params['state']

    fetch = fetch_resource(module, self_link(module))
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), fetch)
                fetch = fetch_resource(module, self_link(module))
                changed = True
        else:
            delete(module, self_link(module))
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module))
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link):
    auth = GcpSession(module, 'appengine')
    return return_if_object(module, auth.post(link, resource_to_request(module)))


def update(module, link, fetch):
    auth = GcpSession(module, 'appengine')
    params = {'updateMask': updateMask(resource_to_request(module), response_to_hash(module, fetch))}
    request = resource_to_request(module)
    del request['name']
    return return_if_object(module, auth.patch(link, request, params=params))


def updateMask(request, response):
    update_mask = []
    if request.get('description') != response.get('description'):
        update_mask.append('description')
    if request.get('sourceRange') != response.get('sourceRange'):
        update_mask.append('sourceRange')
    if request.get('action') != response.get('action'):
        update_mask.append('action')
    if request.get('priority') != response.get('priority'):
        update_mask.append('priority')
    return ','.join(update_mask)


def delete(module, link):
    auth = GcpSession(module, 'appengine')
    return return_if_object(module, auth.delete(link))


def resource_to_request(module):
    request = {u'description': module.params.get('description'), u'sourceRange': module.params.get('source_range'), u'action': module.params.get('action')}
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, 'appengine')
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    return "https://appengine.googleapis.com/v1/apps/{project}/firewall/ingressRules/{priority}".format(**module.params)


def collection(module):
    return "https://appengine.googleapis.com/v1/apps/{project}/firewall/ingressRules".format(**module.params)


def return_if_object(module, response, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {u'description': response.get(u'description'), u'sourceRange': response.get(u'sourceRange'), u'action': response.get(u'action')}


if __name__ == '__main__':
    main()
