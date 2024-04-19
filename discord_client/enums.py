from enum import IntEnum, StrEnum


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


class ConnectionServices(StrEnum):
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
