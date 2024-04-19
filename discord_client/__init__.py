import urllib
import urllib.parse
from enum import Enum
from typing import List

import requests

from .enums import *
from .flags import *
from .validation import *

BASE_URL = "https://discord.com/api"


class ApiVersionStatus(Enum):
    AVAILABLE = 0
    DEPRECATED = 1
    DISCONTINUED = 2


class ApiVersion:
    def __init__(
        self,
        version: int,
        status: ApiVersionStatus,
        default: bool,
    ) -> None:
        self.version = version
        self.status = ApiVersionStatus(status) if isinstance(status, int) else status
        self.default = default


class ApiVersionManager:
    _API_VERSIONS = {
        10: ApiVersion(10, ApiVersionStatus.AVAILABLE, False),
        9: ApiVersion(9, ApiVersionStatus.AVAILABLE, False),
        8: ApiVersion(8, ApiVersionStatus.DEPRECATED, False),
        7: ApiVersion(7, ApiVersionStatus.DEPRECATED, False),
        6: ApiVersion(6, ApiVersionStatus.DEPRECATED, True),
        5: ApiVersion(5, ApiVersionStatus.DISCONTINUED, False),
        4: ApiVersion(4, ApiVersionStatus.DISCONTINUED, False),
        3: ApiVersion(3, ApiVersionStatus.DISCONTINUED, False),
    }

    @classmethod
    def get_api_version(cls, version: int) -> ApiVersion:
        return cls._API_VERSIONS[version]

    @classmethod
    def get_default_api_version(cls) -> ApiVersion:
        for value in cls._API_VERSIONS.values():
            if value.default:
                return value

    @classmethod
    def get_latest_api_version(cls) -> ApiVersion:
        return cls._API_VERSIONS.keys().sort()[0]

    @classmethod
    def get_oldest_api_version(cls) -> ApiVersion:
        return cls._API_VERSIONS.keys().sort()[-1]


DISCORD_EPOCH = 1420070400000


class Snowflake:
    """Creates an object representing a Discord snowflake, providing an interface for accessing properties and performing other operations on these snowflakes."""

    def __init__(self, id: int | str):
        if not isinstance(id, (str, int)):
            raise TypeError("Only accepts integers or strings")

        self._id = int(id) if isinstance(id, str) else id

    @property
    def timestamp(self) -> int:
        """Get the timestamp from the snowflake."""
        return (self._id >> 22) + DISCORD_EPOCH

    @property
    def internal_worker_id(self) -> int:
        """Get the internal worker ID from the snowflake."""
        return (self._id & 0x3E0000) >> 17

    @property
    def internal_process_id(self) -> int:
        """Get the internal process ID from the snowflake."""
        return (self._id & 0x1F000) >> 12

    @property
    def increment(self) -> int:
        """Get the increment from the snowflake."""
        return self._id & 0xFFF

    @classmethod
    def from_timestamp(cls, timestamp_ms: int) -> "Snowflake":
        """Create a snowflake from a unix timestamp."""
        return cls((timestamp_ms - DISCORD_EPOCH) << 22)

    def __eq__(self, other):
        """Compare two snowflakes for equality."""
        if isinstance(other, Snowflake):
            return other._id == self._id
        elif isinstance(other, (int, str)):
            return int(other) == self._id
        return False

    def __ne__(self, other):
        """Compare two snowflakes for inequality."""
        if isinstance(other, Snowflake):
            return other._id != self._id
        elif isinstance(other, (int, str)):
            return int(other) != self._id
        return False

    def __repr__(self) -> str:
        return str(self._id)

    def __str__(self) -> str:
        """Return the string representation of the Snowflake."""
        return str(self._id)


class UserObject(Schema):
    """Note: We won't perform any additional validation on names for now, as we can assume Discord has already enforced their rules prior to sending it to us."""

    id: Snowflake | str
    """the user's id"""
    username: str
    """the user's username, not unique across the platform"""
    discriminator: str
    """the user's Discord-tag"""
    global_name: str = None
    """the user's display name, if it is set. For bots, this is the application name"""
    avatar: str = None
    """the user's avatar hash"""
    bot: bool | None
    """whether the user belongs to an OAuth2 application"""
    system: bool | None
    """whether the user is an Official Discord System user (part of the urgent message system)"""
    mfa_enabled: bool | None
    """whether the user has two factor enabled on their account"""
    banner: str | None = None
    """the user's banner hash"""
    accent_color: int | None = None
    """the user's banner color encoded as an integer representation of hexadecimal color code"""
    locale: str | None
    """the user's chosen language option"""
    verified: bool | None
    """whether the email on this account has been verified"""
    email: str | None = None
    """the user's email"""
    flags: UserFlags | int | None
    """the flags on a user's account"""
    premium_type: int | None
    """the type of Nitro subscription on a user's account"""
    public_flags: int | None
    """the public flags on a user's account"""
    avatar_decoration: int | None = None
    """the user's avatar decoration hash"""

    # NOTE The following members are undocumented, but have been observed
    # in the response data from client requests.
    avatar_decoration_data: dict | None = None
    banner_color: str | None = None
    bio: str | None = None
    clan: str | None = None


class Channel(Schema):
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
    # thread_metadata: None # TODO
    # member: None # TODO
    default_auto_archive_duration: int | None
    permissions: str | None
    flags: int | None
    total_message_sent: int | None
    available_tags: list | None
    applied_tags: list | None
    # default_reaction_emoji: None # TODO
    default_thread_rate_limit_per_user: int | None
    default_sort_order: int | None = None
    default_forum_layout: int | None


class GuildMemberObject(Schema):
    user: UserObject | dict | None
    nick: str | None = None
    avatar: str | None = None
    roles: list  # TODO
    joined_at: str
    premium_since: str | None = None
    deaf: bool
    mute: bool
    flags: GuildMemberFlags | int
    pending: bool | None
    permissions: str | None
    communication_disabled_until: str | None = None
    unusual_dm_activity_until: str | None = None  # NOTE undocumented


class GuildObject(Schema):
    id: Snowflake | str
    name: str
    icon: str = None
    icon_hash: str | None = None
    splash: str = None
    discover_splash: str = None
    owner: bool = False
    owner_id: Snowflake | str
    permissions: str | None
    region: str | None = None
    afk_channel_id: Snowflake | str = None
    afk_timeout: int
    widget_enabled: bool | None
    widget_channel_id: Snowflake | None = None
    verification_level: VerificationLevel | int
    default_message_notifications: DefaultMessageNotificationLevel | int
    explicit_content_filter: ExplicitContentFilterLevel | int
    # roles: None # TODO
    # emojis: None # TODO
    # features: None # TODO
    mfa_level: MFALevel | int
    application_id: Snowflake | str = None
    system_channel_id: Snowflake | str = None
    system_channel_flags: SystemChannelFlags | int
    rules_channel_id: Snowflake | str = None
    max_presences: int | None = None
    max_members: int | None
    vanity_url_code: str = None
    description: str = None
    banner: str = None
    premium_tier: PremiumTier | int
    premium_subscription_count: int | None
    preferred_locale: str
    public_updates_channel_id: Snowflake | str = None
    max_video_channel_users: int | None
    max_stage_video_channel_users: int | None
    approximate_member_count: int | None
    approximate_presence_count: int | None
    # welcome_screen: None # TODO
    nsfw_level: GuildNSFWLevel | int
    # stickers: None # TODO
    premium_progress_bar_enabled: bool
    safety_alerts_channel_id: Snowflake | str = None


class ConnectionObject(Schema):
    id: Snowflake | str
    name: str
    type: ConnectionServices | str
    revoked: bool | None
    intergations: list  # TODO
    verified: bool
    friend_sync: bool
    show_activity: bool
    two_way_link: bool
    visibility: int


def create_endpoint_url(path: str, params: dict) -> str:
    query_string = urllib.parse.urlencode(params)
    endpoint_parts = urllib.parse.ParseResult(
        scheme="https",
        netloc="discord.com",
        path=path,
        params="",
        query=query_string,
        fragment="",
    )

    endpoint_url = urllib.parse.urljoin(BASE_URL, endpoint_parts.geturl())
    return endpoint_url


class Client:
    def __init__(self, token, api_version: ApiVersion | int | None = None):
        self.requests_session = requests.Session()

        version_number = api_version if isinstance(api_version, int) else 9

        self.api_version = (
            api_version
            if api_version
            else ApiVersionManager.get_api_version(version_number)
        )

        self.token = token

    def get_current_user_connections(self) -> ConnectionObject:
        """GET /users/@me/connections"""
        pass

    def get_current_user_guild_member(self):
        pass

    def get_current_user_guilds(
        self,
        before: Snowflake = None,
        after: Snowflake = None,
        limit: int = 200,
        with_counts: bool = False,
    ) -> List[GuildObject]:
        params_dict = {"limit": limit, "with_counts": with_counts}

        if before:
            params_dict["before"] = before
        if after:
            params_dict["after"] = after

        endpoint_url = create_endpoint_url("/users/@me/guilds", params_dict)

    def get_current_user(self) -> UserObject:
        pass

    def get_user(self, id: Snowflake) -> UserObject:
        pass
