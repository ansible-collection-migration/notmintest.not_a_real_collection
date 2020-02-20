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
module: gcp_compute_router
description:
- Represents a Router resource.
short_description: Creates a GCP Router
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
  name:
    description:
    - Name of the resource. The name must be 1-63 characters long, and comply with
      RFC1035. Specifically, the name must be 1-63 characters long and match the regular
      expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must
      be a lowercase letter, and all following characters must be a dash, lowercase
      letter, or digit, except the last character, which cannot be a dash.
    required: true
    type: str
  description:
    description:
    - An optional description of this resource.
    required: false
    type: str
  network:
    description:
    - A reference to the network to which this router belongs.
    - 'This field represents a link to a Network resource in GCP. It can be specified
      in two ways. First, you can place a dictionary with key ''selfLink'' and value
      of your resource''s selfLink Alternatively, you can add `register: name-of-resource`
      to a gcp_compute_network task and then set this network field to "{{ name-of-resource
      }}"'
    required: true
    type: dict
  bgp:
    description:
    - BGP information specific to this router.
    required: false
    type: dict
    suboptions:
      asn:
        description:
        - Local BGP Autonomous System Number (ASN). Must be an RFC6996 private ASN,
          either 16-bit or 32-bit. The value will be fixed for this router resource.
          All VPN tunnels that link to this router will have the same local ASN.
        required: true
        type: int
      advertise_mode:
        description:
        - User-specified flag to indicate which mode to use for advertisement.
        - 'Valid values of this enum field are: DEFAULT, CUSTOM .'
        - 'Some valid choices include: "DEFAULT", "CUSTOM"'
        required: false
        default: DEFAULT
        type: str
      advertised_groups:
        description:
        - User-specified list of prefix groups to advertise in custom mode.
        - This field can only be populated if advertiseMode is CUSTOM and is advertised
          to all peers of the router. These groups will be advertised in addition
          to any specified prefixes. Leave this field blank to advertise no custom
          groups.
        - 'This enum field has the one valid value: ALL_SUBNETS .'
        required: false
        type: list
      advertised_ip_ranges:
        description:
        - User-specified list of individual IP ranges to advertise in custom mode.
          This field can only be populated if advertiseMode is CUSTOM and is advertised
          to all peers of the router. These IP ranges will be advertised in addition
          to any specified groups.
        - Leave this field blank to advertise no custom IP ranges.
        required: false
        type: list
        suboptions:
          range:
            description:
            - The IP range to advertise. The value must be a CIDR-formatted string.
            required: true
            type: str
          description:
            description:
            - User-specified description for the IP range.
            required: false
            type: str
  region:
    description:
    - Region where the router resides.
    required: true
    type: str
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
- 'API Reference: U(https://cloud.google.com/compute/docs/reference/rest/v1/routers)'
- 'Google Cloud Router: U(https://cloud.google.com/router/docs/)'
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
- name: create a network
  gcp_compute_network:
    name: network-router
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: network

- name: create a router
  gcp_compute_router:
    name: test_object
    network: "{{ network }}"
    bgp:
      asn: 64514
      advertise_mode: CUSTOM
      advertised_groups:
      - ALL_SUBNETS
      advertised_ip_ranges:
      - range: 1.2.3.4
      - range: 6.7.0.0/16
    region: us-central1
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
id:
  description:
  - The unique identifier for the resource.
  returned: success
  type: int
creationTimestamp:
  description:
  - Creation timestamp in RFC3339 text format.
  returned: success
  type: str
name:
  description:
  - Name of the resource. The name must be 1-63 characters long, and comply with RFC1035.
    Specifically, the name must be 1-63 characters long and match the regular expression
    `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase
    letter, and all following characters must be a dash, lowercase letter, or digit,
    except the last character, which cannot be a dash.
  returned: success
  type: str
description:
  description:
  - An optional description of this resource.
  returned: success
  type: str
network:
  description:
  - A reference to the network to which this router belongs.
  returned: success
  type: dict
bgp:
  description:
  - BGP information specific to this router.
  returned: success
  type: complex
  contains:
    asn:
      description:
      - Local BGP Autonomous System Number (ASN). Must be an RFC6996 private ASN,
        either 16-bit or 32-bit. The value will be fixed for this router resource.
        All VPN tunnels that link to this router will have the same local ASN.
      returned: success
      type: int
    advertiseMode:
      description:
      - User-specified flag to indicate which mode to use for advertisement.
      - 'Valid values of this enum field are: DEFAULT, CUSTOM .'
      returned: success
      type: str
    advertisedGroups:
      description:
      - User-specified list of prefix groups to advertise in custom mode.
      - This field can only be populated if advertiseMode is CUSTOM and is advertised
        to all peers of the router. These groups will be advertised in addition to
        any specified prefixes. Leave this field blank to advertise no custom groups.
      - 'This enum field has the one valid value: ALL_SUBNETS .'
      returned: success
      type: list
    advertisedIpRanges:
      description:
      - User-specified list of individual IP ranges to advertise in custom mode. This
        field can only be populated if advertiseMode is CUSTOM and is advertised to
        all peers of the router. These IP ranges will be advertised in addition to
        any specified groups.
      - Leave this field blank to advertise no custom IP ranges.
      returned: success
      type: complex
      contains:
        range:
          description:
          - The IP range to advertise. The value must be a CIDR-formatted string.
          returned: success
          type: str
        description:
          description:
          - User-specified description for the IP range.
          returned: success
          type: str
region:
  description:
  - Region where the router resides.
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
import json
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            name=dict(required=True, type='str'),
            description=dict(type='str'),
            network=dict(required=True, type='dict'),
            bgp=dict(
                type='dict',
                options=dict(
                    asn=dict(required=True, type='int'),
                    advertise_mode=dict(default='DEFAULT', type='str'),
                    advertised_groups=dict(type='list', elements='str'),
                    advertised_ip_ranges=dict(type='list', elements='dict', options=dict(range=dict(required=True, type='str'), description=dict(type='str'))),
                ),
            ),
            region=dict(required=True, type='str'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#router'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), kind)
                fetch = fetch_resource(module, self_link(module), kind)
                changed = True
        else:
            delete(module, self_link(module), kind)
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module), kind)
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.patch(link, resource_to_request(module)))


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'compute#router',
        u'region': module.params.get('region'),
        u'name': module.params.get('name'),
        u'description': module.params.get('description'),
        u'network': replace_resource_dict(module.params.get(u'network', {}), 'selfLink'),
        u'bgp': RouterBgp(module.params.get('bgp', {}), module).to_request(),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/routers/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/routers".format(**module.params)


def return_if_object(module, response, kind, allow_not_found=False):
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
    return {
        u'id': response.get(u'id'),
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'name': module.params.get('name'),
        u'description': response.get(u'description'),
        u'network': replace_resource_dict(module.params.get(u'network', {}), 'selfLink'),
        u'bgp': RouterBgp(response.get(u'bgp', {}), module).from_response(),
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#router')


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, 'compute#operation', False)
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


class RouterBgp(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'asn': self.request.get('asn'),
                u'advertiseMode': self.request.get('advertise_mode'),
                u'advertisedGroups': self.request.get('advertised_groups'),
                u'advertisedIpRanges': RouterAdvertisediprangesArray(self.request.get('advertised_ip_ranges', []), self.module).to_request(),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'asn': self.request.get(u'asn'),
                u'advertiseMode': self.request.get(u'advertiseMode'),
                u'advertisedGroups': self.request.get(u'advertisedGroups'),
                u'advertisedIpRanges': RouterAdvertisediprangesArray(self.request.get(u'advertisedIpRanges', []), self.module).from_response(),
            }
        )


class RouterAdvertisediprangesArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict({u'range': item.get('range'), u'description': item.get('description')})

    def _response_from_item(self, item):
        return remove_nones_from_dict({u'range': item.get(u'range'), u'description': item.get(u'description')})


if __name__ == '__main__':
    main()
