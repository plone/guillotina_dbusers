# -*- coding: utf-8 -*-
from plone.server.addons import Addon
from plone.server.content import createContentInContainer
from plone.server import AUTH_EXTRACTION_PLUGINS
from plone.server.registry import ILayers
from plone.server.utils import get_authenticated_user_id
from pserver.zodbusers.participation import ExtractionPlugin


AUTH_EXTRACTION_PLUGINS.append(ExtractionPlugin)
USERS_LAYER = 'pserver.zodbusers.interfaces.IZODBUsersLayer'


class ZODBUsersAddon(Addon):

    @classmethod
    def install(self, request):
        registry = request.site_settings
        registry.forInterface(ILayers).active_layers |= {
            USERS_LAYER
        }
        user = get_authenticated_user_id(request)
        createContentInContainer(
            request.site, 'UserManager', 'users',
            creators=(user,), title='Users')
        createContentInContainer(
            request.site, 'GroupManager', 'groups',
            creators=(user,), title='Groups')

    @classmethod
    def uninstall(self, request):
        registry = request.site_settings
        registry.forInterface(ILayers).active_layers -= {
            USERS_LAYER
        }
        if 'users' in request.site:
            del request.site['users']
        if 'groups' in self.context:
            del request.site['groups']
