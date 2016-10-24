# -*- encoding: utf-8 -*-
from plone.server.content import Item
from plone.server.interfaces import IItem
from zope.interface import implementer
from zope import schema
from pserver.zodbusers import _


class IGroupManager(IItem):
    pass


class IGroup(IItem):

    name = schema.TextLine(
        title=_('Group name'),
        required=False)


@implementer(IGroup)
class Group(Item):
    pass


@implementer(IGroupManager)
class GroupManager(Item):
    pass
