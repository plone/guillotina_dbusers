

class DBUserIdentifier(object):

    def __init__(self, request):
        self.request = request

    async def get_user(self, token):
        try:
            users = await self.request.container.async_get('users')
        except (AttributeError, KeyError):
            return

        if token.get('id', '') in await users.async_keys():
            user = await users.async_get(token.get('id', ''))
            if not user.disabled:
                return user
