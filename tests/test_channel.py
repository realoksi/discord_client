import unittest
import os
import json

import discord_client


class test_channel(unittest.TestCase):
    def load_case(self, filename):
        case_json = None
        with open(f"./tests/channel_cases/{filename}", "r") as fp:
            case_json = json.load(fp)

        if not case_json:
            self.fail(
                f"couldn't load the json for this case. check the validity of case file {filename}"
            )

        return case_json

    def test_ok_1(self):
        case_json = self.load_case("ok_1.json")

        case_channel = discord_client.Channel(**case_json)

    def test_minimal_1(self):
        case_json = self.load_case("minimal_1.json")

        case_channel = discord_client.Channel(**case_json)

    def test_minimal_2(self):
        case_json = self.load_case("minimal_2.json")

        case_channel = discord_client.Channel(**case_json)

    def test_minimal_3(self):
        case_json = self.load_case("minimal_3.json")

        case_channel = discord_client.Channel(**case_json)


if __name__ == "__main__":
    unittest.main()
