import json

_group = {
    "name": "foo",
    "description": "foo description",
    "@type": "Group",
    "id": "foo",
}


async def test_ensure_crud_groups(dbusers_requester):
    async with dbusers_requester as requester:
        resp, status_code = await requester(
            "POST", "/db/guillotina/groups", data=json.dumps(_group)
        )
        assert status_code == 201
        resp, status_code = await requester("GET", "/db/guillotina/@groups")
        assert status_code == 200
        assert len(resp) == 1
        assert resp[0]["groupname"] == "foo"

        data = {
            "roles": {
                "guillotina.Manager": True,
                "guillotina.Tester": True,
                "guillotina.Bad": False,
            }
        }

        resp, status = await requester(
            "PATCH", "/db/guillotina/@groups/foo", data=json.dumps(data)
        )
        assert status == 204
        resp, status = await requester("GET", "/db/guillotina/@groups/foo")
        assert set(resp["roles"]) == set(["guillotina.Manager", "guillotina.Tester"])

        data = {
            "roles": {
                "guillotina.Manager": False
            }
        }
        resp, status = await requester(
            "PATCH", "/db/guillotina/@groups/foo", data=json.dumps(data)
        )
        assert status == 204
        resp, status = await requester("GET", "/db/guillotina/@groups/foo")
        assert set(resp["roles"]) == set(["guillotina.Tester"])

        data = {
            "users": {
                "foo": True,
                "var": False,
                "xxx": True
            }
        }
        resp, status = await requester(
            "PATCH", "/db/guillotina/@groups/foo", data=json.dumps(data)
        )
        assert status == 204
        resp, status = await requester("GET", "/db/guillotina/@groups/foo")
        assert set(resp["users"]["items"]) == set(["foo", "xxx"])
        data = {
            "users": {
                "xxx": False
            }
        }
        resp, status = await requester(
            "PATCH", "/db/guillotina/@groups/foo", data=json.dumps(data)
        )
        assert status == 204
        resp, status = await requester("GET", "/db/guillotina/@groups/foo")
        assert set(resp["users"]["items"]) == set(["foo"])













