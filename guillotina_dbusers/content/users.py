# -*- encoding: utf-8 -*-
from guillotina.content import Folder
from guillotina.interfaces import IFolder
from guillotina_dbusers import _
from guillotina import schema
from guillotina import configure
from guillotina.interfaces import Allow


class IUserManager(IFolder):
    pass


class IUser(IFolder):

    username = schema.TextLine(
        title=_('Username'),
        required=False)

    email = schema.TextLine(
        title=_('Email'),
        required=False)

    name = schema.TextLine(
        title=_('Name'),
        required=False)

    password = schema.TextLine(
        title=_('Password'),
        required=False)

    user_groups = schema.List(
        title=_('Groups'),
        value_type=schema.TextLine(),
        required=False
    )

    user_roles = schema.List(
        title=_('Roles'),
        value_type=schema.TextLine(),
        required=False
    )

    disabled = schema.Bool(
        title=_('Disabled'),
        default=False
    )


@configure.contenttype(
    type_name="User",
    schema=IUser,
    add_permission="guillotina.AddUser",
    behaviors=["guillotina.behaviors.dublincore.IDublinCore"])
class User(Folder):
    username = email = name = password = None
    disabled = False
    user_roles = ['guillotinaMember']
    user_groups = []

    @property
    def roles(self):
        roles = {
            'guillotina.Authenticated': 1
        }
        for role in getattr(self, 'user_roles', []) or []:
            roles[role] = Allow
        return roles

    @property
    def groups(self):
        return getattr(self, 'user_groups', []) or []

    @property
    def _properties(self):
        return {}


@configure.contenttype(
    type_name="UserManager",
    schema=IUserManager,
    behaviors=["guillotina.behaviors.dublincore.IDublinCore"],
    allowed_types=["User"])
class UserManager(Folder):
    pass
