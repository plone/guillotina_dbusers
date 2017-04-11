# -*- coding: utf-8 -*-
from guillotina_dbusers.testing import PserverZODBUsersTestCase


class TestContent(PserverZODBUsersTestCase):

    def test_content(self):
        site = self.get_portal()
        self.assertEqual(
            site['users'].type_name, 'UserManager')
        self.assertEqual(
            site['groups'].type_name, 'GroupManager')
