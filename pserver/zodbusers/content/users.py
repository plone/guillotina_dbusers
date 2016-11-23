# -*- encoding: utf-8 -*-
from BTrees.OOBTree import OOBTree
from plone.server.content import Folder
from plone.server.interfaces import IContainer
from pserver.zodbusers import _
from zope import schema
from zope.interface import implementer


class IUserManager(IContainer):
    pass


class IUser(IContainer):

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


@implementer(IUser)
class User(Folder):
    username = email = name = password = None
    disabled = False
    roles = ['plone.Member']
    groups = []

    # @property
    # def password(self):
    #     return self._password
    #
    # @password.setter
    # def set_password(self, value):
    #     # this is going to be a raw password...
    #     self._password = value

    @property
    def _roles(self):
        roles = {}
        for role in getattr(self, 'roles', []) or []:
            roles[role] = 1
        return roles

    @property
    def _groups(self):
        return getattr(self, 'groups', []) or []

    @property
    def _properties(self):
        return {}


@implementer(IUserManager)
class UserManager(Folder):
    def __init__(self, id_=None):
        super().__init__(id_)
        self.username_mapping = OOBTree()
