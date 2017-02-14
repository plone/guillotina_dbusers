# -*- coding: utf-8 -*-
from plone.server import configure
from plone.server.addons import Addon
from plone.server.content import create_content_in_container
from plone.server.registry import ILayers
from plone.server.utils import get_authenticated_user_id


USERS_LAYER = 'pserver.zodbusers.interfaces.IZODBUsersLayer'


@configure.addon(
    name="zodbusers",
    title="Plone ZODB Users")
class ZODBUsersAddon(Addon):

    @classmethod
    def install(self, site, request):
        registry = request.site_settings
        registry.for_interface(ILayers).active_layers |= {
            USERS_LAYER
        }
        user = get_authenticated_user_id(request)
        create_content_in_container(
            site, 'UserManager', 'users',
            creators=(user,), title='Users')
        create_content_in_container(
            site, 'GroupManager', 'groups',
            creators=(user,), title='Groups')

    @classmethod
    def uninstall(self, site, request):
        registry = request.site_settings
        registry.for_interface(ILayers).active_layers -= {
            USERS_LAYER
        }
        if 'users' in site:
            del site['users']
        if 'groups' in site:
            del site['groups']
