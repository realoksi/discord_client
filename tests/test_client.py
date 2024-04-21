import datetime
import unittest

import discord_client


class test_client(unittest.TestCase):
    def setUp(self):
        self.client = discord_client.Client("faketoken")

    def test_current_user_guilds(self):
        pass

    def test_discoverable_guilds(self):
        discoverable_guilds = self.client.get_discoverable_guilds()

        print(len(discoverable_guilds))


if __name__ == "__main__":
    unittest.main()
