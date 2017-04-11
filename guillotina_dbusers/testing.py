from guillotina.testing import PloneBaseLayer
from guillotina.testing import TESTING_SETTINGS

import json
import unittest


TESTING_SETTINGS.update({
    "auth_user_identifiers": [
        "guillotina_dbusers.users.DBUserIdentifier",
    ],
    "applications": [
        "guillotina_dbusers"
    ]
})

#
# class PserverZODBUsersTestCase(unittest.TestCase):
#     ''' Adding the OAuth utility '''
#     layer = PloneBaseLayer
#
#     def setUp(self):
#         self.layer.requester('POST', '/db/guillotina/@addons', data=json.dumps({
#             "id": "zodbusers"
#         }))
#
#     def get_portal(self):
#         root = self.layer.new_root()
#         return root['plone']
