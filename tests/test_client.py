import logging
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
            print("Channel doesn't exist")

        print(f'Channel name is "{channel.name}", and is a', end="")
        match channel.type:
            case discord_client.ChannelTypes.GUILD_TEXT:
                print(" text channel")
            case discord_client.ChannelTypes.GUILD_VOICE:
                print(" voice channel")
            case discord_client.ChannelTypes.GUILD_CATEGORY:
                print(" category")
            case discord_client.ChannelTypes.GUILD_STAGE_VOICE:
                print(" voice stage")
            case _:
                print("n other type of channel")

    def test_get_channel_messages(self):
        channel = self.client.get_channel(305834181949390848)

        if channel:
            messages = channel.get_channel_messages()
            print(f'Got {len(messages)} messages from channel "{channel.name}"')
        else:
            print("Channel doesn't exist")

    def test_current_user_guilds(self):
        current_user_guilds = self.client.get_current_user_guilds()

        if not current_user_guilds:
            print("User is not in any guilds")
        else:
            print(f"Current user is in {len(current_user_guilds)} guild(s)")

    def test_discoverable_guilds(self):
        discoverable_guilds = self.client.get_discoverable_guilds()

        print(f"Got {len(discoverable_guilds)} discoverable guild(s)")

    def test_get_current_user(self):
        current_user = self.client.get_current_user()

        if not current_user:
            print("Couldn't get the current user")
        else:
            print(f'Got current user with name "{current_user.global_name}"')

    def test_get_user(self):
        user = self.client.get_user(788441080676220968)

        if not user:
            print("Couldn't get the user")
        else:
            print(f"Got user with an accent color of {user.accent_color}")


if __name__ == "__main__":
    unittest.main()
