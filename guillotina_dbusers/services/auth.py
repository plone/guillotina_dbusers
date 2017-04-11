from datetime import datetime
from datetime import timedelta
from guillotina import app_settings
from guillotina import configure
from guillotina.api.service import Service
from guillotina.auth.validators import SaltedHashPasswordValidator
from guillotina.browser import UnauthorizedResponse
from guillotina.interfaces import IContainer
from guillotina.utils import get_authenticated_user

import jwt


@configure.service(
    context=IContainer,
    name="@login",
    method="POST",
    permission="guillotina.NotAuthenticated")
class Login(Service):
    token_timeout = 60 * 60 * 1

    async def __call__(self):
        data = await self.request.json()
        creds = {
            'token': data['password'],
            'id': data['username']
        }
        validator = SaltedHashPasswordValidator(self.request)
        user = await validator.validate(creds)
        if user is None:
            return UnauthorizedResponse('login failed')

        data = {
            'exp': datetime.utcnow() + timedelta(seconds=self.token_timeout),
            'id': user.id
        }
        jwt_token = jwt.encode(data, app_settings['jwt']['secret']).decode('utf-8')

        return {
            'exp': data['exp'],
            'token': jwt_token
        }


@configure.service(
    context=IContainer,
    name="@refresh_token",
    method="POST",
    permission="guillotina.Authenticated")
class Refresh(Login):
    async def __call__(self):
        user = get_authenticated_user(self.request)
        if user is None:
            return UnauthorizedResponse('user not authorized')

        data = {
            'exp': datetime.utcnow() + timedelta(seconds=self.token_timeout),
            'id': user.id
        }
        jwt_token = jwt.encode(data, app_settings['jwt']['secret']).decode('utf-8')
        return {
            'exp': data['exp'],
            'token': jwt_token
        }
