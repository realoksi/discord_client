import os
import unittest

import discord_client


class MissingEnvironmentVariable(Exception):
    pass


class test_client(unittest.TestCase):
    def setUp(self):
        DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

        if not DISCORD_TOKEN:
            raise MissingEnvironmentVariable

        self.client = discord_client.Client(DISCORD_TOKEN)

    def test_get_channel(self):
        channel = self.client.get_channel(305834181949390848)

        if not channel:
            print("Channel doesn't exist?")

    def test_get_channel_messages(self):
        channel = self.client.get_channel(305834181949390848)

        if channel:
            print(f"{len(channel.get_channel_messages())} messages")
        else:
            print("Channel doesn't exist?")

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
