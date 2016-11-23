# -*- coding: utf-8 -*-

from plone.server.testing import PloneBaseLayer, TESTING_SETTINGS
import unittest
import json


TESTING_SETTINGS["auth_user_identifiers"] = [
    "pserver.zodbusers.users.ZODBUserIdentifier"
]


class PserverZODBUsersTestCase(unittest.TestCase):
    ''' Adding the OAuth utility '''
    layer = PloneBaseLayer

    def setUp(self):
        self.layer.requester('POST', '/plone/plone/@addons', data=json.dumps({
            "id": "zodbusers"
        }))

    def get_portal(self):
        root = self.layer.new_root()
        return root['plone']
