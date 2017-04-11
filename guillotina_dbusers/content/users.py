# -*- encoding: utf-8 -*-
from BTrees.OOBTree import OOBTree
from guillotina.content import Folder
from guillotina.interfaces import IFolder
from guillotina_dbusers import _
from guillotina import schema
from guillotina import configure


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

    groups = schema.List(
        title=_('Groups'),
        value_type=schema.TextLine(),
        required=False
    )

    roles = schema.List(
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
    add_permission="guillotinaAddUser",
    behaviors=["guillotina.behaviors.dublincore.IDublinCore"])
class User(Folder):
    username = email = name = password = None
    disabled = False
    roles = ['guillotinaMember']
    groups = []

    @property
    def _roles(self):
        roles = {
            'guillotinaAuthenticated': 1
        }
        for role in getattr(self, 'roles', []) or []:
            roles[role] = 1
        return roles

    @property
    def _groups(self):
        return getattr(self, 'groups', []) or []

    @property
    def _properties(self):
        return {}


@configure.contenttype(
    type_name="UserManager",
    schema=IUserManager,
    behaviors=["guillotina.behaviors.dublincore.IDublinCore"],
    allowed_types=["User"])
class UserManager(Folder):
    def __init__(self, id_=None):
        super().__init__(id_)
        self.username_mapping = OOBTree()
