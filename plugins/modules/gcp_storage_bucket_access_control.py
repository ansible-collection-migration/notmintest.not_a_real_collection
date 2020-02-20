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
module: gcp_storage_bucket_access_control
description:
- The BucketAccessControls resource represents the Access Control Lists (ACLs) for
  buckets within Google Cloud Storage. ACLs let you specify who has access to your
  data and to what extent.
- 'There are three roles that can be assigned to an entity: READERs can get the bucket,
  though no acl property will be returned, and list the bucket''s objects. WRITERs
  are READERs, and they can insert objects into the bucket and delete the bucket''s
  objects. OWNERs are WRITERs, and they can get the acl property of a bucket, update
  a bucket, and call all BucketAccessControls methods on the bucket. For more information,
  see Access Control, with the caveat that this API uses READER, WRITER, and OWNER
  instead of READ, WRITE, and FULL_CONTROL.'
short_description: Creates a GCP BucketAccessControl
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
  bucket:
    description:
    - The name of the bucket.
    - 'This field represents a link to a Bucket resource in GCP. It can be specified
      in two ways. First, you can place a dictionary with key ''name'' and value of
      your resource''s name Alternatively, you can add `register: name-of-resource`
      to a gcp_storage_bucket task and then set this bucket field to "{{ name-of-resource
      }}"'
    required: true
    type: dict
  entity:
    description:
    - 'The entity holding the permission, in one of the following forms: user-userId
      user-email group-groupId group-email domain-domain project-team-projectId allUsers
      allAuthenticatedUsers Examples: The user liz@example.com would be user-liz@example.com.'
    - The group example@googlegroups.com would be group-example@googlegroups.com.
    - To refer to all members of the Google Apps for Business domain example.com,
      the entity would be domain-example.com.
    required: true
    type: str
  role:
    description:
    - The access permission for the entity.
    - 'Some valid choices include: "OWNER", "READER", "WRITER"'
    required: false
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
'''

EXAMPLES = '''
- name: create a bucket
  gcp_storage_bucket:
    name: "{{ resource_name }}"
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: bucket

- name: create a bucket access control
  gcp_storage_bucket_access_control:
    bucket: "{{ bucket }}"
    entity: user-alexstephen@google.com
    role: WRITER
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
bucket:
  description:
  - The name of the bucket.
  returned: success
  type: dict
domain:
  description:
  - The domain associated with the entity.
  returned: success
  type: str
email:
  description:
  - The email address associated with the entity.
  returned: success
  type: str
entity:
  description:
  - 'The entity holding the permission, in one of the following forms: user-userId
    user-email group-groupId group-email domain-domain project-team-projectId allUsers
    allAuthenticatedUsers Examples: The user liz@example.com would be user-liz@example.com.'
  - The group example@googlegroups.com would be group-example@googlegroups.com.
  - To refer to all members of the Google Apps for Business domain example.com, the
    entity would be domain-example.com.
  returned: success
  type: str
entityId:
  description:
  - The ID for the entity.
  returned: success
  type: str
id:
  description:
  - The ID of the access-control entry.
  returned: success
  type: str
projectTeam:
  description:
  - The project team associated with the entity.
  returned: success
  type: complex
  contains:
    projectNumber:
      description:
      - The project team associated with the entity.
      returned: success
      type: str
    team:
      description:
      - The team.
      returned: success
      type: str
role:
  description:
  - The access permission for the entity.
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from ansible_collections.notmintest.not_a_real_collection.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
import json

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            bucket=dict(required=True, type='dict'),
            entity=dict(required=True, type='str'),
            role=dict(type='str'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/devstorage.full_control']

    state = module.params['state']
    kind = 'storage#bucketAccessControl'

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
    auth = GcpSession(module, 'storage')
    return return_if_object(module, auth.post(link, resource_to_request(module)), kind)


def update(module, link, kind):
    auth = GcpSession(module, 'storage')
    return return_if_object(module, auth.put(link, resource_to_request(module)), kind)


def delete(module, link, kind):
    auth = GcpSession(module, 'storage')
    return return_if_object(module, auth.delete(link), kind)


def resource_to_request(module):
    request = {
        u'kind': 'storage#bucketAccessControl',
        u'bucket': replace_resource_dict(module.params.get(u'bucket', {}), 'name'),
        u'entity': module.params.get('entity'),
        u'role': module.params.get('role'),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'storage')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    res = {'bucket': replace_resource_dict(module.params['bucket'], 'name'), 'entity': module.params['entity']}
    return "https://www.googleapis.com/storage/v1/b/{bucket}/acl/{entity}".format(**res)


def collection(module):
    res = {'bucket': replace_resource_dict(module.params['bucket'], 'name')}
    return "https://www.googleapis.com/storage/v1/b/{bucket}/acl".format(**res)


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
        u'bucket': replace_resource_dict(module.params.get(u'bucket', {}), 'name'),
        u'domain': response.get(u'domain'),
        u'email': response.get(u'email'),
        u'entity': module.params.get('entity'),
        u'entityId': response.get(u'entityId'),
        u'id': response.get(u'id'),
        u'projectTeam': BucketAccessControlProjectteam(response.get(u'projectTeam', {}), module).from_response(),
        u'role': response.get(u'role'),
    }


class BucketAccessControlProjectteam(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'projectNumber': self.request.get('project_number'), u'team': self.request.get('team')})

    def from_response(self):
        return remove_nones_from_dict({u'projectNumber': self.request.get(u'projectNumber'), u'team': self.request.get(u'team')})


if __name__ == '__main__':
    main()
