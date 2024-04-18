from enum import IntFlag


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
