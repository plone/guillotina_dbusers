from plone.server.api.service import Service
from plone.server.browser import Response
from plone.server.utils import get_authenticated_user


class Info(Service):

    async def __call__(self):
        user = get_authenticated_user(self.request)
        return Response({
            'id': user.id,
            'roles': user._roles,
            'groups': user._groups
        })
