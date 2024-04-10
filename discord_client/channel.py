from typing import List

from discord_client.utils import Snowflake
from discord_client.validation import BaseValidator


class Channel(BaseValidator):
    id: Snowflake | str
    type: int
    guild_id: Snowflake | str | None
    position: int | None
    permission_overwrites: list | None
    name: str | None = None
    topic: str | None = None
    nsfw: bool | None
    last_message_id: Snowflake | str | None = None
    bitrate: int | None
    user_limit: int | None
    rate_limit_per_user: int | None
    recipients: list | None
    icon: str | None = None
    owner_id: Snowflake | str | None
    application_id: Snowflake | str | None
    managed: bool | None
    parent_id: Snowflake | str | None = None
    last_pin_timestamp: str | None = None
    rtc_region: str | None = None
    video_quality_mode: int | None
    message_count: int | None
    member_count: int | None
    # thread_metadata: ??? TODO
    # member: ??? TODO
    default_auto_archive_duration: int | None
    permissions: str | None
    flags: int | None
    total_message_sent: int | None
    available_tags: list | None
    applied_tags: list | None
    # default_reaction_emoji:  = None
    default_thread_rate_limit_per_user: int | None
    default_sort_order: int | None = None
    default_forum_layout: int | None
