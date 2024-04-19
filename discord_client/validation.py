from enum import IntFlag, auto
from types import NoneType
from typing import Any, Dict, get_args


class SchemaIgnoreFlags(IntFlag):
    DEFAULT = 0
    UNEXPECTED_KEY = auto()
    TYPE_MISMATCH = auto()
    MISSING_KEYS = auto()
    TYPE_CASTING = auto()


class Schema:
    def __init__(
        self,
        fields: Dict[str, Any],
        flags: SchemaIgnoreFlags = SchemaIgnoreFlags.UNEXPECTED_KEY,
    ) -> None:
        self._validate_fields(fields, flags)

        self.extra()

    def __init_subclass__(cls, **kwargs) -> None:
        cls._fields: Dict[str, tuple] = dict()

        for key, value in cls.__annotations__.items():
            cls._fields[key] = (get_args(value) or (value,), hasattr(cls, key))
            # args list, is nullable

        super().__init_subclass__(**kwargs)

    def _validate_fields(
        self,
        fields: Dict[str, Any],
        flags: SchemaIgnoreFlags = SchemaIgnoreFlags.UNEXPECTED_KEY,
    ):
        """Validates all fields described by the class."""
        for name, value in fields.items():
            validation_result = self._validate_field(name, value)

            if validation_result == 0:
                cast_value = value
                for cast_type in self._fields[name][0]:
                    if type(value) is cast_type or type(value) is NoneType:
                        break
                    try:
                        if isinstance(cast_type, Schema):
                            cast_value = cast_type(value, flags)
                        else:
                            cast_value = cast_type(value)
                        if cast_value:
                            break
                    except (TypeError, ValueError):
                        pass
                setattr(self, name, cast_value)
            elif (
                validation_result == 1 and not flags & SchemaIgnoreFlags.UNEXPECTED_KEY
            ):
                raise ValueError(f"Unexpected field {name}")
            elif (
                validation_result == 2
                and not self._fields[name][1]
                and type(value) is not NoneType
            ):
                raise TypeError(
                    f"Unexpected type {type(value)} for field '{name}', expected one of {self._fields[name][0]}"
                )
            else:
                setattr(self, name, value)

        for name, value in self._fields.items():
            if name in fields:
                continue

            if NoneType not in value[0] and not value[1]:
                raise ValueError(f"Missing required field '{name}'")

    def _validate_field(
        self,
        name,
        value,
    ):
        """Only validates a single field described by the class."""
        if name not in self._fields:
            return 1  # unexpected key
        if not any(isinstance(value, cast_type) for cast_type in self._fields[name][0]):
            return 2  # type mismatch
        return 0

    def extra(self):
        """
        Any additional validation logic may be implemented using this method under an inheriting class.
        """
        pass
