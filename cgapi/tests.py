# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import subprocess
from django.test import TestCase, Client



class CgroupsTestCase(TestCase):

    def assert_cgroup_struct(self, cgroup_dict):
        """Ensure cgroup dict has a right structure """
        self.assertIn('name', cgroup_dict)
        self.assertIn('cpu_limit', cgroup_dict)
        self.assertIn('memory_limit', cgroup_dict)
        self.assertIn('pids', cgroup_dict)
        self.assertIsInstance(cgroup_dict['pids'], list)

    def setUp(self):
        self.group_name = 'group1'
        # Start a process which will work 60 sec
        self.process1 = subprocess.Popen(['sleep', '60'])
        self.process2 = subprocess.Popen(['sleep', '60'])

    def test_cgroup_create(self):
        """Test cgroup creation"""

        c = Client()
        response = c.get('/cgapi/cgroups/%s' % self.group_name)
        self.assertEqual(response.status_code, 200)
        self.assert_cgroup_struct(response.json())
        self.assertEqual(response.json()['name'], self.group_name)

    def Test_cgroup_list_pids(self):
        """Test pids listing. Should be run after pids added into the group"""
        c = Client()
        response = c.get('/cgapi/cgroups/%s' % self.group_name)
        self.assertEqual(response.status_code, 200)
        self.assert_cgroup_struct(response.json())
        self.assertIn(self.process1.pid, response.json()['pids'])
        self.assertIn(self.process2.pid, response.json()['pids'])

    def test_cgroup_add_pid(self):
        """Test adding pid to the cgroup and listing pids"""

        c = Client()
        print('/cgapi/cgroups/%s/pids/%s' % (self.group_name, self.process1.pid))
        # Add first process to the group
        response = c.put('/cgapi/cgroups/%s/pids/%s' % (self.group_name, self.process1.pid))
        self.assertEqual(response.status_code, 200)
        self.assert_cgroup_struct(response.json())
        self.assertIn(self.process1.pid, response.json()['pids'])

        # Add second process to the group
        response = c.put('/cgapi/cgroups/%s/pids/%s' % (self.group_name, self.process2.pid))
        self.assertEqual(response.status_code, 200)
        self.assert_cgroup_struct(response.json())
        self.assertIn(self.process1.pid, response.json()['pids'])
        self.assertIn(self.process2.pid, response.json()['pids'])

        self.Test_cgroup_list_pids()