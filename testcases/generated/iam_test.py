# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

import unittest
import os
import json


class IamTest(unittest.TestCase):

    def test_create_permission(self):
        cmd = """python ../../main.py iam create-permission  --create-permission-info '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_permission_detail(self):
        cmd = """python ../../main.py iam describe-permission-detail  --permission-id '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_update_permission(self):
        cmd = """python ../../main.py iam update-permission  --permission-id '5' --update-permission-info '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_permissions(self):
        cmd = """python ../../main.py iam describe-permissions  --page-number '5' --page-size '5' --query-type '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_sub_user_permissions(self):
        cmd = """python ../../main.py iam describe-sub-user-permissions  --sub-user 'xxx' --page-number '5' --page-size '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_permissions_to_sub_user(self):
        cmd = """python ../../main.py iam add-permissions-to-sub-user  --sub-user 'xxx' --add-permissions-info '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_remove_permission_of_sub_user(self):
        cmd = """python ../../main.py iam remove-permission-of-sub-user  --permission-id '5' --sub-user 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_subuser(self):
        cmd = """python ../../main.py iam create-subuser  --create-sub-user-info '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_user_access_keys(self):
        cmd = """python ../../main.py iam describe-user-access-keys """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_user_access_key(self):
        cmd = """python ../../main.py iam create-user-access-key """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_enabled_user_access_key(self):
        cmd = """python ../../main.py iam enabled-user-access-key  --access-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disabled_user_access_key(self):
        cmd = """python ../../main.py iam disabled-user-access-key  --access-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_user_access_key(self):
        cmd = """python ../../main.py iam delete-user-access-key  --access-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

