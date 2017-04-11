from guillotina import configure
from guillotina.api.service import Service
from guillotina.browser import Response
from guillotina.interfaces import IContainer
from guillotina.interfaces import IResourceSerializeToJson
from guillotina.utils import get_authenticated_user
from guillotina.component import queryMultiAdapter


@configure.service(
    context=IContainer,
    name="@user_info",
    method="GET",
    permission="guillotina.Authenticated")
class Info(Service):

    async def __call__(self):
        user = get_authenticated_user(self.request)
        serializer = queryMultiAdapter((user, self.request), IResourceSerializeToJson)
        if serializer:
            data = serializer()
        else:
            data = {}
        data.update({
            'id': user.id,
            'roles': user.roles,
            'groups': getattr(user, 'groups', [])
        })
        return Response(data)
