# -*- encoding: utf-8 -*-
from plone.server.content import Item
from plone.server.interfaces import IItem
from zope.interface import implementer
from zope import schema
from pserver.zodbusers import _


class IUserManager(IItem):
    pass


class IUser(IItem):

    username = schema.TextLine(
        title=_('Username'),
        required=False)

    email = schema.TextLine(
        title=_('Email'),
        required=False)

    name = schema.TextLine(
        title=_('Username'),
        required=False)

    password = schema.TextLine(
        title=_('Username'),
        required=False)


@implementer(IUser)
class User(Item):

    @property
    def _roles(self):
        # XXX needs implementation...
        return {
            'plone.SiteAdmin': 1,
            'plone.SiteDeleter': 1,
            'plone.Owner': 1,
            'plone.Anonymous': 0
        }

    @property
    def _groups(self):
        return []

    @property
    def _properties(self):
        return {}


@implementer(IUserManager)
class UserManager(Item):
    pass
