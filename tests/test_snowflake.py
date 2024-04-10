import unittest

import discord_client


class test_snowflakes(unittest.TestCase):
    def test_snowflakes_all(self):
        raw_snowflake = 238831660550848513
        timestamp = 1477012305153

        snowflake = discord_client.Snowflake(raw_snowflake)

        self.assertIsNotNone(snowflake)
        self.assertRaises(TypeError, discord_client.Snowflake, [raw_snowflake])
        self.assertEqual(str(snowflake), str(raw_snowflake))

        self.assertEqual(snowflake.increment, 1)
        self.assertEqual(snowflake.internal_process_id, 0)
        self.assertEqual(snowflake.internal_worker_id, 0)
        self.assertEqual(snowflake.timestamp, timestamp)

        snowflake_from_timestamp = discord_client.Snowflake.from_timestamp(timestamp)

        self.assertIsNotNone(snowflake_from_timestamp)
        self.assertEqual(timestamp, snowflake_from_timestamp.timestamp)


if __name__ == "__main__":
    unittest.main()
