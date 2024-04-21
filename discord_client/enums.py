from enum import Enum, IntEnum


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


class PremiumTypes(IntEnum):
    NONE = 0
    NITRO_CLASSIC = 1
    NITRO = 2
    NITRO_BASIC = 3


class PremiumTier(IntEnum):
    NONE = 0
    """guild has not unlocked any Server Boost perks"""
    TIER_1 = 1
    """guild has unlocked Server Boost level 1 perks"""
    TIER_2 = 1
    """guild has unlocked Server Boost level 2 perks"""
    TIER_3 = 1
    """guild has unlocked Server Boost level 3 perks"""


class ConnectionServices(Enum):
    battlenet = "Battle.net"
    bungie = "Bungie.net"
    ebay = "eBay"
    epicgames = "Epic Games"
    facebook = "Facebook"
    github = "GitHub"
    instagram = "Instagram"
    leagueoflegends = "League of Legends"
    paypal = "PayPal"
    playstation = "PlayStation Network"
    reddit = "Reddit"
    riotgames = "Riot Games"
    spotify = "Spotify"
    skype = "Skype"
    steam = "Steam"
    tiktok = "TikTok"
    twitch = "Twitch"
    twitter = "Twitter"
    xbox = "Xbox"
    youtube = "YouTube"


class ConnectionVisibilityTypes(IntEnum):
    NONE = 0
    """invisible to everyone except the user themselves"""
    EVERYONE = 1
    """visible to everyone"""


class MessageTypes(IntEnum):
    DEFAULT = 0
    RECIPIENT_ADD = 1
    RECIPIENT_REMOVE = 2
    CALL = 3
    CHANNEL_NAME_CHANGE = 4
    CHANNEL_ICON_CHANGE = 5
    CHANNEL_PINNED_MESSAGE = 6
    USER_JOIN = 7
    GUILD_BOOST = 8
    GUILD_BOOST_TIER_1 = 9
    GUILD_BOOST_TIER_2 = 10
    GUILD_BOOST_TIER_3 = 11
    CHANNEL_FOLLOW_ADD = 12
    GUILD_DISCOVERY_DISQUALIFIED = 14
    GUILD_DISCOVERY_REQUALIFIED = 15
    GUILD_DISCOVERY_GRACE_PERIOD_INITIAL_WARNING = 16
    GUILD_DISCOVERY_GRACE_PERIOD_FINAL_WARNING = 17
    THREAD_CREATED = 18
    REPLY = 19
    CHAT_INPUT_COMMAND = 20
    THREAD_STARTER_MESSAGE = 21
    GUILD_INVITE_REMINDER = 22
    CONTEXT_MENU_COMMAND = 23
    AUTO_MODERATION_ACTION = 24
    ROLE_SUBSCRIPTION_PURCHASE = 25
    INTERACTION_PREMIUM_UPSELL = 26
    STAGE_START = 27
    STAGE_END = 28
    STAGE_SPEAKER = 29
    STAGE_TOPIC = 31
    GUILD_APPLICATION_PREMIUM_SUBSCRIPTION = 32
