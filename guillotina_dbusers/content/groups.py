# -*- encoding: utf-8 -*-
from guillotina import configure
from guillotina import schema
from guillotina.content import Folder
from guillotina.interfaces import IFolder
from guillotina_dbusers import _
from zope.interface import implementer


class IGroupManager(IFolder):
    pass


class IGroup(IFolder):

    name = schema.TextLine(
        title=_('Group name'),
        required=False)

    roles = schema.List(
        title=_('Roles'),
        value_type=schema.TextLine(),
        required=False
    )


@configure.contenttype(
    type_name="Group",
    schema=IGroup,
    add_permission="guillotinaAddGroup",
    behaviors=["guillotina.behaviors.dublincore.IDublinCore"])
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
    type_name="GroupManager",
    schema=IGroupManager,
    behaviors=["guillotina.behaviors.dublincore.IDublinCore"],
    allowed_types=["Group"])
class GroupManager(Folder):
    pass
