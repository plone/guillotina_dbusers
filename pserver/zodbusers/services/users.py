from plone.server.api.dexterity import DefaultPOST


class POSTUser(DefaultPOST):

    async def get_data(self):
        """
        creating a user means they are going to provide a password.

        The password comes in as plain text and needs to be transformed
        with a password storage policy to the hashed representation of it
        """
        data = await self.request.json()
        # data['password'] =
        return data
