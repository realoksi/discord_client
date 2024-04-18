from enum import Enum, IntEnum
from typing import List

import requests

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


class UserFlags(IntFlag):
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


class User(Schema):
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
    flags: UserFlags | int | None
    premium_type: int | None
    public_flags: int | None
    avatar_decoration: int | None = None
    avatar_decoration_data: dict | None = None  # NOTE undocumented
    banner_color: str | None = None  # NOTE undocumented
    bio: str | None = None  # NOTE undocumented
    clan: str | None = None  # NOTE undocumented


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


class DefaultMessageNotificationLevel(IntEnum):
    ALL_MESSAGES = 0
    """members will receive notifications for all messages by default"""
    ONLY_MENTIONS = 1
    """members will receive notifications only for messages that @mention them by default"""


class ExplicitContentFilterLevel(IntEnum):
    DISABLED = 0
    """media content will not be scanned"""
    MEMBERS_WITHOUT_ROLES = 1
    """media content sent by members without roles will be scanned"""
    ALL_MEMBERS = 2
    """media content sent by all members will be scanned"""


class MFALevel(IntEnum):
    NONE = 0
    """guild has no MFA/2FA requirement for moderation actions"""
    ELEVATED = 1
    """guild has a 2FA requirement for moderation actions"""


class VerificationLevel(IntEnum):
    NONE = 0
    """unrestricted"""
    LOW = 1
    """must have verified email on account"""
    MEDIUM = 1
    """must be registered on Discord for longer than 5 minutes"""
    HIGH = 1
    """must be a member of the server for longer than 10 minutes"""
    VERY_HIGH = 1
    """must have a verified phone number"""


class GuildNSFWLevel(IntEnum):
    DEFAULT = 0
    EXPLICIT = 1
    SAFE = 1
    AGE_RESTRICTED = 1


class PremiumTier(IntEnum):
    NONE = 0
    """guild has not unlocked any Server Boost perks"""
    TIER_1 = 1
    """guild has unlocked Server Boost level 1 perks"""
    TIER_2 = 1
    """guild has unlocked Server Boost level 2 perks"""
    TIER_3 = 1
    """guild has unlocked Server Boost level 3 perks"""


class SystemChannelFlags(IntFlag):
    SUPPRESS_JOIN_NOTIFICATIONS = 1 << 0
    """Suppress member join notifications"""
    SUPPRESS_PREMIUM_SUBSCRIPTIONS = 1 << 1
    """Suppress server boost notifications"""
    SUPPRESS_GUILD_REMINDER_NOTIFICATIONS = 1 << 2
    """Suppress server setup tips"""
    SUPPRESS_JOIN_NOTIFICATION_REPLIES = 1 << 3
    """Hide member join sticker reply buttons"""
    SUPPRESS_ROLE_SUBSCRIPTION_PURCHASE_NOTIFICATIONS = 1 << 4
    """Suppress role subscription purchase and renewal notifications"""
    SUPPRESS_ROLE_SUBSCRIPTION_PURCHASE_NOTIFICATION_REPLIES = 1 << 5
    """Hide role subscription sticker reply buttons"""


class GuildMemberFlags(IntFlag):
    DID_REJOIN = 1 << 0
    COMPLETED_ONBOARDING = 1 << 1
    BYPASSES_VERIFICATION = 1 << 2
    STARTED_ONBOARDING = 1 << 3


class GuildMemberObject(Schema):
    user: User | dict | None
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


class Guild(Schema):
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

    def get_guild_member(self, user_id: Snowflake) -> GuildMemberObject:
        pass

    def get_guild_channels(self) -> List[Channel]:
        pass


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

    def get_guild(self, id: Snowflake = None, with_counts: bool = False) -> Guild:
        pass
