# -*- coding: utf-8 -*-
from pserver.zodbusers.testing import PserverZODBUsersTestCase
import json
import base64


class TestContent(PserverZODBUsersTestCase):

    def test_add_user(self):
        self.layer.requester('GET', '/plone/plone/users').content
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
        self.assertTrue('foobar' in self.layer.portal['users'])

        # test auth
        resp = self.layer.requester(
            'DELETE',
            '/plone/plone/users/foobar',
            token=base64.b64encode(b'foobar:password').decode('ascii')
        )
        self.assertTrue('foobar' not in self.layer.portal['users'])
