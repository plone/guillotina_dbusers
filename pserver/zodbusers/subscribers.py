from plone.server import configure
from plone.server.auth.validators import hash_password
from plone.server.events import NewUserAdded
from plone.server.interfaces import IObjectFinallyCreatedEvent
from pserver.zodbusers.content.users import IUser
from zope.event import notify


@configure.subscriber(for_=(IUser, IObjectFinallyCreatedEvent))
def user_created(user, event):
    user.password = hash_password(user.password)
    notify(NewUserAdded(user))
