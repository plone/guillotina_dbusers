# -*- coding: utf-8 -*-
from zope.i18nmessageid import MessageFactory
from plone.server import configure

_ = MessageFactory('pserver.zodbusers')


configure.permission("plone.NotAuthenticated", "")
configure.permission("plone.Authenticated", "")
configure.permission("plone.AddUser", title="Add plone user")
configure.permission("plone.AddGroup", title="Add plone group")
configure.grant(permission="plone.AccessContent",
                role="plone.Anonymous")
configure.grant(permission="plone.NotAuthenticated",
                role="plone.Anonymous")
configure.grant(permission="plone.Authenticated",
                role="plone.Authenticated")
configure.grant(permission="plone.AddUser",
                role="plone.SiteAdmin")
configure.grant(permission="plone.AddGroup",
                role="plone.SiteAdmin")


def includeme(root, settings):
    configure.scan('pserver.zodbusers.content.users')
    configure.scan('pserver.zodbusers.content.groups')
    configure.scan('pserver.zodbusers.install')
    configure.scan('pserver.zodbusers.services')
