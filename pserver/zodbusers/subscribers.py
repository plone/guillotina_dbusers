from plone.server.auth.validators import hash_password
from plone.server.events import NewUserAdded
from zope.event import notify


def user_created(user, event):
    user.password = hash_password(user.password)
    notify(NewUserAdded(user))
