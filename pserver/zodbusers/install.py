# -*- coding: utf-8 -*-
from plone.dexterity.utils import createContentInContainer
from plone.server.addons import Addon
from plone.server.registry import ILayers
from plone.server.utils import get_authenticated_user_id
from plone.server.registry import ACTIVE_AUTH_EXTRACTION_KEY


USERS_LAYER = 'pserver.zodbusers.interfaces.IZODBUsersLayer'
EXTRACTION_PLUGIN = 'pserver.zodbusers.participation.ExtractionPlugin'


class ZODBUsersAddon(Addon):

    @classmethod
    def install(self, request):
        registry = request.site_settings
        registry.forInterface(ILayers).active_layers |= {
            USERS_LAYER
        }
        user = get_authenticated_user_id(request)
        createContentInContainer(
            request.site, 'UserManager',
            id='users', creators=(user,), title='Users')
        createContentInContainer(
            request.site, 'GroupManager',
            id='groups', creators=(user,), title='Groups')

        plugins = list(registry.get(ACTIVE_AUTH_EXTRACTION_KEY, []))
        if EXTRACTION_PLUGIN not in plugins:
            plugins.append(EXTRACTION_PLUGIN)
            registry[ACTIVE_AUTH_EXTRACTION_KEY] = frozenset(plugins)

    @classmethod
    def uninstall(self, request):
        registry = request.site_settings
        registry.forInterface(ILayers).active_layers -= {
            USERS_LAYER
        }
        if 'users' in request.site:
            del request.site.__parent__['users']
        if 'groups' in self.context:
            del request.site.__parent__['groups']

        plugins = list(registry.get(ACTIVE_AUTH_EXTRACTION_KEY, []))
        if EXTRACTION_PLUGIN in plugins:
            plugins.remove(EXTRACTION_PLUGIN)
            registry[ACTIVE_AUTH_EXTRACTION_KEY] = frozenset(plugins)
