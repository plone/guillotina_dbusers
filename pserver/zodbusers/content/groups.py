# -*- encoding: utf-8 -*-
from plone.server.content import Folder
from plone.server.interfaces import IContainer
from zope.interface import implementer
from zope import schema
from pserver.zodbusers import _
from plone.server import configure


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


@configure.contenttype(
    portal_type="Group",
    schema=IGroup,
    add_permission="plone.AddGroup",
    behaviors=["plone.server.behaviors.dublincore.IDublinCore"])
class Group(Folder):
    name = None
    roles = []

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
@configure.contenttype(
    portal_type="GroupManager",
    schema=IGroupManager,
    behaviors=["plone.server.behaviors.dublincore.IDublinCore"],
    allowed_types=["Group"])
class GroupManager(Folder):
    pass
