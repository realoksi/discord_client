from typing import NamedTuple, Set, Tuple, Union, get_args
from enum import IntFlag


class ValidationFlags(IntFlag):
    IGNORE_UNEXPECTED_KEYS = 1
    IGNORE_TYPE_MISMATCH = 2
    IGNORE_MISSING_KEYS = 4
    IGNORE_TYPE_CASTING = 8


class FieldFlags(IntFlag):
    OPTIONAL = 1
    NULLABLE = 2


class Field(NamedTuple):
    name: str
    flags: FieldFlags
    types: Tuple[Union[type, None]]


class BaseValidator:
    fields: Set[Field] = None

    def __init__(
        self, validation_flags: ValidationFlags = ValidationFlags(0), **kwargs
    ) -> None:
        if self.fields is None:
            raise Exception(
                f"Cannot validate because {self.__class__.__name__}.fields is empty"
            )

        for name, value in kwargs.items():
            unexpected_name = False
            field = self.get_field(name)

            if field is None:
                if not validation_flags & ValidationFlags.IGNORE_UNEXPECTED_KEYS:
                    raise ValueError(f'Unexpected field "{name}" in kwargs')
                else:
                    unexpected_name = True

            value_type = type(value)
            if (
                not validation_flags & ValidationFlags.IGNORE_TYPE_MISMATCH
                and not unexpected_name
            ):
                if value_type not in field.types and value_type is not None:
                    raise ValueError(
                        f'Unexpected type "{value_type}" for key "{name}", expected one of {field.types}'
                    )

            cast = None
            if (
                validation_flags & ValidationFlags.IGNORE_TYPE_CASTING or not value
            ) or unexpected_name:
                cast = value
            else:
                for cast_type in field.types:
                    try:
                        cast = cast_type(value)

                        if cast:
                            break

                    except:
                        pass

            setattr(self, name, cast)

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)

        if not cls.fields:
            cls.fields = set()

            for key, value in cls.__annotations__.items():
                args = get_args(value) or (value,)

                flags = FieldFlags(0)

                if type(None) in args:
                    flags |= FieldFlags.OPTIONAL

                if hasattr(cls, key):
                    flags |= FieldFlags.NULLABLE

                field = Field(key, flags, args)

                cls.fields.add(field)

    def get_field(self, name) -> Field | None:
        for field in self.fields:
            if field.name == name:
                return field
        return None
