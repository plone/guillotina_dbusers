# -*- encoding: utf-8 -*-
from plone.server.content import Folder
from plone.server.interfaces import IContainer
from zope.interface import implementer
from zope import schema
from pserver.zodbusers import _


class IGroupManager(IContainer):
    pass


class IGroup(IContainer):

    name = schema.TextLine(
        title=_('Group name'),
        required=False)

    roles = schema.List(
        title=_('Roles'),
        value_type=schema.TextLine(),
        required=False
    )


@implementer(IGroup)
class Group(Folder):
    name = None
    roles = None

    @property
    def roles(self):
        roles = {}
        for role in getattr(self, 'roles', []) or []:
            roles[role] = 1
        return roles

    @property
    def groups(self):
        return []

    @property
    def properties(self):
        return {}


@implementer(IGroupManager)
class GroupManager(Folder):
    pass
