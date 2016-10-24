# -*- coding: utf-8 -*-
from pserver.zodbusers.testing import PserverZODBUsersTestCase


class TestContent(PserverZODBUsersTestCase):

    def test_content(self):
        self.assertEqual(
            self.layer.portal['users'].portal_type, 'UserManager')
        self.assertEqual(
            self.layer.portal['groups'].portal_type, 'GroupManager')
