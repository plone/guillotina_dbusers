import base64
from plone.server.utils import strings_differ


class ExtractionPlugin(object):
    def __init__(self, request):
        self.request = request

    def auth_user(self, user):
        self.request._cache_user = user

    async def extract_user(self):

        req = self.request
        try:
            users = req.site['users']
        except (AttributeError, KeyError):
            return

        header_auth = req.headers.get('AUTHORIZATION')
        token = None
        if header_auth is not None:
            schema, _, encoded_token = header_auth.partition(' ')
            if schema.lower() == 'basic' or schema.lower() == 'bearer':
                token = base64.b64decode(encoded_token.encode('utf8')).decode('utf8')
                username, _, password = token.partition(':')
                if username in users:
                    user = users[username]
                    if not strings_differ(password, user.password):
                        return self.auth_user(user)
