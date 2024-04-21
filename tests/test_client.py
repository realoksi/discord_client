import unittest

import discord_client

# WARNING
## For these tests to work, a proper Discord token is required.
## Without one, these will fail or at the very least behave in an unexpected manner.


class test_client(unittest.TestCase):
    def setUp(self):
        self.client = discord_client.Client("faketoken")

    def test_current_user_guilds(self):
        current_user_guilds = self.client.get_current_user_guilds()

        if not current_user_guilds:
            print("User is not in any guilds?")
        else:
            print(len(current_user_guilds))

    def test_discoverable_guilds(self):
        discoverable_guilds = self.client.get_discoverable_guilds()

        print(len(discoverable_guilds))


if __name__ == "__main__":
    unittest.main()
