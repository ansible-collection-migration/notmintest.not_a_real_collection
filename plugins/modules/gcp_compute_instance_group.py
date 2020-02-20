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
module: gcp_compute_instance_group
description:
- Represents an Instance Group resource. Instance groups are self-managed and can
  contain identical or different instances. Instance groups do not use an instance
  template. Unlike managed instance groups, you must create and add instances to an
  instance group manually.
short_description: Creates a GCP InstanceGroup
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
    - An optional description of this resource. Provide this property when you create
      the resource.
    required: false
    type: str
  name:
    description:
    - The name of the instance group.
    - The name must be 1-63 characters long, and comply with RFC1035.
    required: false
    type: str
  named_ports:
    description:
    - Assigns a name to a port number.
    - 'For example: {name: "http", port: 80}.'
    - This allows the system to reference ports by the assigned name instead of a
      port number. Named ports can also contain multiple ports.
    - 'For example: [{name: "http", port: 80},{name: "http", port: 8080}] Named ports
      apply to all instances in this instance group.'
    required: false
    type: list
    suboptions:
      name:
        description:
        - The name for this named port.
        - The name must be 1-63 characters long, and comply with RFC1035.
        required: false
        type: str
      port:
        description:
        - The port number, which can be a value between 1 and 65535.
        required: false
        type: int
  network:
    description:
    - The network to which all instances in the instance group belong.
    - 'This field represents a link to a Network resource in GCP. It can be specified
      in two ways. First, you can place a dictionary with key ''selfLink'' and value
      of your resource''s selfLink Alternatively, you can add `register: name-of-resource`
      to a gcp_compute_network task and then set this network field to "{{ name-of-resource
      }}"'
    required: false
    type: dict
  region:
    description:
    - The region where the instance group is located (for regional resources).
    required: false
    type: str
  subnetwork:
    description:
    - The subnetwork to which all instances in the instance group belong.
    - 'This field represents a link to a Subnetwork resource in GCP. It can be specified
      in two ways. First, you can place a dictionary with key ''selfLink'' and value
      of your resource''s selfLink Alternatively, you can add `register: name-of-resource`
      to a gcp_compute_subnetwork task and then set this subnetwork field to "{{ name-of-resource
      }}"'
    required: false
    type: dict
  zone:
    description:
    - A reference to the zone where the instance group resides.
    required: true
    type: str
  instances:
    description:
    - The list of instances associated with this InstanceGroup.
    - All instances must be created before being added to an InstanceGroup.
    - All instances not in this list will be removed from the InstanceGroup and will
      not be deleted.
    - Only the full identifier of the instance will be returned.
    required: false
    type: list
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
'''

EXAMPLES = '''
- name: create a network
  gcp_compute_network:
    name: network-instancegroup
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: network

- name: create a instance group
  gcp_compute_instance_group:
    name: test_object
    named_ports:
    - name: ansible
      port: 1234
    network: "{{ network }}"
    zone: us-central1-a
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
creationTimestamp:
  description:
  - Creation timestamp in RFC3339 text format.
  returned: success
  type: str
description:
  description:
  - An optional description of this resource. Provide this property when you create
    the resource.
  returned: success
  type: str
id:
  description:
  - A unique identifier for this instance group.
  returned: success
  type: int
name:
  description:
  - The name of the instance group.
  - The name must be 1-63 characters long, and comply with RFC1035.
  returned: success
  type: str
namedPorts:
  description:
  - Assigns a name to a port number.
  - 'For example: {name: "http", port: 80}.'
  - This allows the system to reference ports by the assigned name instead of a port
    number. Named ports can also contain multiple ports.
  - 'For example: [{name: "http", port: 80},{name: "http", port: 8080}] Named ports
    apply to all instances in this instance group.'
  returned: success
  type: complex
  contains:
    name:
      description:
      - The name for this named port.
      - The name must be 1-63 characters long, and comply with RFC1035.
      returned: success
      type: str
    port:
      description:
      - The port number, which can be a value between 1 and 65535.
      returned: success
      type: int
network:
  description:
  - The network to which all instances in the instance group belong.
  returned: success
  type: dict
region:
  description:
  - The region where the instance group is located (for regional resources).
  returned: success
  type: str
subnetwork:
  description:
  - The subnetwork to which all instances in the instance group belong.
  returned: success
  type: dict
zone:
  description:
  - A reference to the zone where the instance group resides.
  returned: success
  type: str
instances:
  description:
  - The list of instances associated with this InstanceGroup.
  - All instances must be created before being added to an InstanceGroup.
  - All instances not in this list will be removed from the InstanceGroup and will
    not be deleted.
  - Only the full identifier of the instance will be returned.
  returned: success
  type: list
'''

################################################################################
# Imports
################################################################################

from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
import json
import re
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            description=dict(type='str'),
            name=dict(type='str'),
            named_ports=dict(type='list', elements='dict', options=dict(name=dict(type='str'), port=dict(type='int'))),
            network=dict(type='dict'),
            region=dict(type='str'),
            subnetwork=dict(type='dict'),
            zone=dict(required=True, type='str'),
            instances=dict(type='list', elements='dict'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#instanceGroup'

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

    if fetch:
        instance = InstanceLogic(module)
        instance.run()
        fetch.update({'instances': instance.list_instances()})
    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, kind):
    instance = InstanceLogic(module)
    instance.run()


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'compute#instanceGroup',
        u'description': module.params.get('description'),
        u'name': module.params.get('name'),
        u'namedPorts': InstanceGroupNamedportsArray(module.params.get('named_ports', []), module).to_request(),
        u'network': replace_resource_dict(module.params.get(u'network', {}), 'selfLink'),
        u'region': region_selflink(module.params.get('region'), module.params),
        u'subnetwork': replace_resource_dict(module.params.get(u'subnetwork', {}), 'selfLink'),
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
    return "https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/instanceGroups/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/instanceGroups".format(**module.params)


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
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'description': response.get(u'description'),
        u'id': response.get(u'id'),
        u'name': response.get(u'name'),
        u'namedPorts': InstanceGroupNamedportsArray(response.get(u'namedPorts', []), module).from_response(),
        u'network': response.get(u'network'),
        u'region': response.get(u'region'),
        u'subnetwork': response.get(u'subnetwork'),
    }


def region_selflink(name, params):
    if name is None:
        return
    url = r"https://www.googleapis.com/compute/v1/projects/.*/regions/.*"
    if not re.match(url, name):
        name = "https://www.googleapis.com/compute/v1/projects/{project}/regions/%s".format(**params) % name
    return name


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#instanceGroup')


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


class InstanceLogic(object):
    def __init__(self, module):
        self.module = module
        self.current_instances = self.list_instances()
        self.module_instances = []

        # Transform module list of instances (dicts of instance responses) into a list of selfLinks.
        instances = self.module.params.get('instances')
        if instances:
            for instance in instances:
                self.module_instances.append(replace_resource_dict(instance, 'selfLink'))

    def run(self):
        # Find all instances to add and add them
        instances_to_add = list(set(self.module_instances) - set(self.current_instances))
        if instances_to_add:
            self.add_instances(instances_to_add)

        # Find all instances to remove and remove them
        instances_to_remove = list(set(self.current_instances) - set(self.module_instances))
        if instances_to_remove:
            self.remove_instances(instances_to_remove)

    def list_instances(self):
        auth = GcpSession(self.module, 'compute')
        response = return_if_object(self.module, auth.post(self._list_instances_url(), {'instanceState': 'ALL'}), 'compute#instanceGroupsListInstances')

        # Transform instance list into a list of selfLinks for diffing with module parameters
        instances = []
        for instance in response.get('items', []):
            instances.append(instance['instance'])
        return instances

    def add_instances(self, instances):
        auth = GcpSession(self.module, 'compute')
        wait_for_operation(self.module, auth.post(self._add_instances_url(), self._build_request(instances)))

    def remove_instances(self, instances):
        auth = GcpSession(self.module, 'compute')
        wait_for_operation(self.module, auth.post(self._remove_instances_url(), self._build_request(instances)))

    def _list_instances_url(self):
        return "https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/instanceGroups/{name}/listInstances".format(**self.module.params)

    def _remove_instances_url(self):
        return "https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/instanceGroups/{name}/removeInstances".format(**self.module.params)

    def _add_instances_url(self):
        return "https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/instanceGroups/{name}/addInstances".format(**self.module.params)

    def _build_request(self, instances):
        request = {'instances': []}
        for instance in instances:
            request['instances'].append({'instance': instance})
        return request


class InstanceGroupNamedportsArray(object):
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
        return remove_nones_from_dict({u'name': item.get('name'), u'port': item.get('port')})

    def _response_from_item(self, item):
        return remove_nones_from_dict({u'name': item.get(u'name'), u'port': item.get(u'port')})


if __name__ == '__main__':
    main()
