from plone.server.testing import PloneBaseLayer
from plone.server.testing import TESTING_SETTINGS

import json
import unittest


TESTING_SETTINGS.update({
    "auth_user_identifiers": [
        "pserver.zodbusers.users.ZODBUserIdentifier",
    ],
    "applications": [
        "pserver.zodbusers"
    ]
})


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
