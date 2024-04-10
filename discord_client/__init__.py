import requests

from enum import Enum

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

    def get_channel_messages(channel_id, around, before, after, limit):
        pass


from .utils import *
from .user import *
from .channel import *
from .validation import *
