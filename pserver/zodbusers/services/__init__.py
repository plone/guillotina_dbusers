from . import auth  # noqa
from . import users  # noqa
from plone.server import configure
from plone.server.api.content import DefaultPOST
from pserver.zodbusers.content.users import IUserManager
from pserver.zodbusers.content.groups import IGroupManager

# override some views...
configure.service(
    context=IUserManager, method='POST', permission='plone.AddUser'
)(DefaultPOST)
configure.service(
    context=IGroupManager, method='POST', permission='plone.AddGroup'
)(DefaultPOST)
