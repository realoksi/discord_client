from enum import IntFlag


class UserFlags(IntFlag):
    """See https://discord.com/developers/docs/resources/user#user-object-user-flags"""

    STAFF = 1 << 0
    """Discord Employee"""
    PARTNER = 1 << 1
    """Partnered Server Owner"""
    HYPESQUAD = 1 << 2
    """HypeSquad Events Member"""
    BUG_HUNTER_LEVEL_1 = 1 << 3
    """Bug Hunter Level 1"""
    HYPESQUAD_ONLINE_HOUSE_1 = 1 << 6
    """House Bravery Member"""
    HYPESQUAD_ONLINE_HOUSE_2 = 1 << 7
    """House Brilliance Member"""
    HYPESQUAD_ONLINE_HOUSE_3 = 1 << 8
    """House Balance Member"""
    PREMIUM_EARLY_SUPPORTER = 1 << 9
    """Early Nitro Supporter"""
    TEAM_PSEUDO_USER = 1 << 10
    """User is a team"""
    BUG_HUNTER_LEVEL_2 = 1 << 14
    """Bug Hunter Level 2"""
    VERIFIED_BOT = 1 << 16
    """Verified Bot"""
    VERIFIED_DEVELOPER = 1 << 17
    """Early Verified Bot Developer"""
    CERTIFIED_MODERATOR = 1 << 18
    """Moderator Programs Alumni"""
    BOT_HTTP_INTERACTIONS = 1 << 19
    """Bot uses only HTTP interactions and is shown in the online member list"""
    ACTIVE_DEVELOPER = 1 << 22
    """User is an Active Developer"""


class SystemChannelFlags(IntFlag):
    """See https://discord.com/developers/docs/resources/guild#guild-object-system-channel-flags"""

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
    """See https://discord.com/developers/docs/resources/guild#guild-member-object-guild-member-flags"""

    DID_REJOIN = 1 << 0
    """Member has left and rejoined the guild"""
    COMPLETED_ONBOARDING = 1 << 1
    """Member has completed onboarding"""
    BYPASSES_VERIFICATION = 1 << 2
    """Member is exempt from guild verification requirements"""
    STARTED_ONBOARDING = 1 << 3
    """Member has started onboarding"""
