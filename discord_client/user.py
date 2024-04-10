from enum import IntFlag

from discord_client.utils import Snowflake
from discord_client.validation import BaseValidator


class Flags(IntFlag):
    STAFF = 1 << 0
    PARTNER = 1 << 1
    HYPESQUAD = 1 << 2
    BUG_HUNTER_LEVEL_1 = 1 << 3
    HYPESQUAD_ONLINE_HOUSE_1 = 1 << 6
    HYPESQUAD_ONLINE_HOUSE_2 = 1 << 7
    HYPESQUAD_ONLINE_HOUSE_3 = 1 << 8
    PREMIUM_EARLY_SUPPORTER = 1 << 9
    TEAM_PSEUDO_USER = 1 << 10
    BUG_HUNTER_LEVEL_2 = 1 << 14
    VERIFIED_BOT = 1 << 16
    VERIFIED_DEVELOPER = 1 << 17
    CERTIFIED_MODERATOR = 1 << 18
    BOT_HTTP_INTERACTIONS = 1 << 19
    ACTIVE_DEVELOPER = 1 << 22


class User(BaseValidator):
    id: Snowflake | str
    username: str
    discriminator: str
    global_name: str = None
    avatar: str = None
    bot: bool | None
    system: bool | None
    mfa_enabled: bool | None
    banner: str | None = None
    accent_color: int | None = None
    locale: str | None
    verified: bool | None
    email: str | None = None
    flags: int | None
    premium_type: int | None
    public_flags: int | None
    avatar_decoration: int | None = None

    # NOTE below are undocumented members and
    # are likely to be innacurate

    avatar_decoration_data: dict | None = None
    banner_color: str | None = None
    bio: str = None
