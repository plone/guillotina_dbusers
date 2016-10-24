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
    pass


@implementer(IUserManager)
class UserManager(Item):
    pass
