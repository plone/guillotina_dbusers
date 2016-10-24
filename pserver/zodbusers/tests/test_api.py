# -*- coding: utf-8 -*-
from pserver.zodbusers.testing import PserverZODBUsersTestCase
import json


class TestContent(PserverZODBUsersTestCase):

    def test_add_user(self):
        resp = self.layer.requester(
            'POST',
            '/plone/plone/users',
            data=json.dumps({
                "@type": "User",
                "name": "Foobar",
                "id": "foobar",
                "username": "foobar",
                "email": "foo@bar.com",
                "password": "password"
            })
        )
        self.assertEquals(resp.status_code, 201)
