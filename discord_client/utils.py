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
