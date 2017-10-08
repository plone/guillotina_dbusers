.. contents::

guillotina_dbusers
==================

Store users/groups in the database for guillotina.


Installation
------------

- pip install guillotina_dbusers
- add `guillotina_dbusers` to list of applications in your guillotina configuration
- install into your container using the `@addons` endpoint


Available content types:
- User
- Group

Usage
-----

After installation, you will now have a `users` and `groups` folder inside
your container.


POST /db/container/users {
  "@type": "User",
  "username": "foobar",
  "email": "foo@bar.com",
  "password": "foobar"
}


You can now authenticate with the `foobar` user.



Login
-----

Besides using default authentication mechanisms, this package also provides
a `@login` so you can work with jwt tokens.

POST /db/container/@login {
  "username": "foobar",
  "password": "foobar"
}


And a `@refresh_token` endpoint:

    POST /db/container/@refresh_token
