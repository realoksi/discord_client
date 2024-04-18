import unittest

import discord_client


class test_snowflakes(unittest.TestCase):
    def setUp(self):
        self.snowflake_1 = discord_client.Snowflake(238831660550848513) # me
        self.snowflake_2 = discord_client.Snowflake(575880665913098250) # my gen-voice channel

    def test_constructor(self):
        with self.assertRaises(TypeError):
            discord_client.Snowflake(None)
        with self.assertRaises(ValueError):
            discord_client.Snowflake("peanut butter")
    
    def test_timestamp(self):
        self.assertEqual(self.snowflake_1.timestamp, 1477012305153)
        self.assertEqual(self.snowflake_2.timestamp, 1557371050099)

    def test_internal_worker_id(self):
        self.assertEqual(self.snowflake_1.internal_worker_id, 0)
        self.assertEqual(self.snowflake_2.internal_worker_id, 2)

    def test_internal_process_id(self):
        self.assertEqual(self.snowflake_1.internal_process_id, 0)
        self.assertEqual(self.snowflake_2.internal_process_id, 0)

    def test_increment(self):
        self.assertEqual(self.snowflake_1.increment, 1)
        self.assertEqual(self.snowflake_2.increment, 10)

if __name__ == "__main__":
    unittest.main()
