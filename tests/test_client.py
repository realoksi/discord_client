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
        self.test_channel_id = 305834181949390848

    def test_get_channel(self):
        channel = self.client.get_channel(self.test_channel_id)

        self.assertIsNotNone(channel, f"Channel {self.test_channel_id} might not exist")

    def test_get_channel_messages(self):
        channel = self.client.get_channel(self.test_channel_id)

        self.assertIsNotNone(channel, f"Channel {self.test_channel_id} might not exist")

        messages = channel.get_channel_messages()

        self.assertIsNotNone(
            messages, f"Couldn't get messages from channel {self.test_channel_id}"
        )

        self.assertTrue(len(messages) > 0, "List of messages is empty")

        # TODO
        # Assert values returned fom messages

    def test_current_user_guilds(self):
        current_user_guilds = self.client.get_current_user_guilds()

        self.assertIsNotNone(current_user_guilds, "User may not be in any group")

    def test_discoverable_guilds(self):
        discoverable_guilds = self.client.get_discoverable_guilds()

        self.assertIsNotNone(discoverable_guilds, "Couldn't discover any guilds")
        self.assertTrue(
            len(discoverable_guilds) > 0, "List of discoverable guilds is empty"
        )

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
