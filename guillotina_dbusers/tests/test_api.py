# -*- coding: utf-8 -*-
import json
import base64
from guillotina.tests.utils import get_container


async def test_add_user(dbusers_requester):
    async with await dbusers_requester as requester:
        resp, status_code = await requester('GET', '/db/guillotina/users')
        resp, status_code = await requester(
            'POST',
            '/db/guillotina/users',
            data=json.dumps({
                "@type": "User",
                "name": "Foobar",
                "id": "foobar",
                "username": "foobar",
                "email": "foo@bar.com",
                "password": "password"
            })
        )
        assert status_code == 201

        # required because portal object layer has is stale
        container = await get_container(requester)
        assert await container.async_contains('foobar')

# def test_user_auth(self):
#     self.layer.requester(
#         'POST',
#         '/db/guillotina/users',
#         data=json.dumps({
#             "@type": "User",
#             "name": "Foobar",
#             "id": "foobar",
#             "username": "foobar",
#             "email": "foo@bar.com",
#             "password": "password"
#         })
#     )
#     # user should be able to add content to object
#     self.layer.requester(
#         'POST',
#         '/db/guillotina/users/foobar',
#         data=json.dumps({
#             "@type": "Item",
#             "id": "foobar",
#             "title": "foobar"
#         }),
#         token=base64.b64encode(b'foobar:password').decode('ascii')
#     )
#     site = self.get_portal()
#     self.assertTrue('foobar' not in site['users']['foobar'])
#
# def test_login(self):
#     # add user...
#     self.layer.requester(
#         'POST',
#         '/db/guillotina/users',
#         data=json.dumps({
#             "@type": "User",
#             "name": "Foobar",
#             "id": "foobar",
#             "username": "foobar",
#             "email": "foo@bar.com",
#             "password": "password",
#             "groups": ["Managers"]
#         })
#     )
#
#     resp = self.layer.requester(
#         'POST',
#         '/db/guillotina/@login',
#         data=json.dumps({
#             "username": "foobar",
#             "password": "password"
#         })
#     )
#     self.assertEquals(resp.status_code, 200)
#
#     # test using new auth token
#     resp = self.layer.requester(
#         'GET', '/db/guillotina/@addons',
#         token=json.loads(resp.content.decode('utf-8'))['token'],
#         auth_type='Bearer'
#     )
#     assert resp.status_code == 200
#
# def test_refresh(self):
#     # add user...
#     self.layer.requester(
#         'POST',
#         '/db/guillotina/users',
#         data=json.dumps({
#             "@type": "User",
#             "name": "Foobar",
#             "id": "foobar",
#             "username": "foobar",
#             "email": "foo@bar.com",
#             "password": "password",
#             "groups": ["Managers"]
#         })
#     )
#
#     resp = self.layer.requester(
#         'POST',
#         '/db/guillotina/@login',
#         data=json.dumps({
#             "username": "foobar",
#             "password": "password"
#         })
#     )
#     self.assertEquals(resp.status_code, 200)
#
#     resp = self.layer.requester(
#         'POST', '/db/guillotina/@refresh_token',
#         token=json.loads(resp.content.decode('utf-8'))['token'],
#         auth_type='Bearer'
#     )
#     assert resp.status_code == 200
#     assert 'token' in json.loads(resp.content.decode('utf-8'))
