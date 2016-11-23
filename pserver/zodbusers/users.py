

class ZODBUserIdentifier(object):

    def __init__(self, request):
        self.request = request

    async def get_user(self, token):
        try:
            users = self.request.site['users']
        except (AttributeError, KeyError):
            return

        if token.get('id', '') in users:
            user = users[token.get('id', '')]
            if not user.disabled:
                return user
