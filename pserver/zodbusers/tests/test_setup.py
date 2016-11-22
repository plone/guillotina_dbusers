# -*- coding: utf-8 -*-
from pserver.zodbusers.testing import PserverZODBUsersTestCase


class TestContent(PserverZODBUsersTestCase):

    def test_content(self):
        site = self.get_portal()
        self.assertEqual(
            site['users'].portal_type, 'UserManager')
        self.assertEqual(
            site['groups'].portal_type, 'GroupManager')
