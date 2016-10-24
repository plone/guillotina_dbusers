# -*- coding: utf-8 -*-

from plone.server.testing import PloneBaseLayer
import unittest
import json


class PserverZODBUsersLayer(PloneBaseLayer):

    @classmethod
    def setUp(cls):
        cls.requester('POST', '/plone/plone/@addons', data=json.dumps({
            "id": "zodbusers"
        }))


class PserverZODBUsersTestCase(unittest.TestCase):
    ''' Adding the OAuth utility '''
    layer = PserverZODBUsersLayer
