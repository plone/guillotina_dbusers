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

        # required because portal object layer has is stale
        site = self.get_portal()
        self.assertTrue('foobar' in site['users'])

    def test_user_auth(self):
        self.layer.requester(
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
        # user should be able to add content to object
        self.layer.requester(
            'POST',
            '/plone/plone/users/foobar',
            data=json.dumps({
                "@type": "Item",
                "id": "foobar",
                "title": "foobar"
            }),
            token=base64.b64encode(b'foobar:password').decode('ascii')
        )
        site = self.get_portal()
        self.assertTrue('foobar' not in site['users']['foobar'])
