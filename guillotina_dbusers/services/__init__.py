from . import auth  # noqa
from . import users  # noqa
from guillotina import configure
from guillotina.api.content import DefaultPOST
from guillotina_dbusers.content.users import IUserManager
from guillotina_dbusers.content.groups import IGroupManager

# override some views...
configure.service(
    context=IUserManager, method='POST', permission='guillotina.AddUser'
)(DefaultPOST)
configure.service(
    context=IGroupManager, method='POST', permission='guillotina.AddGroup'
)(DefaultPOST)
