from typing import Dict, NamedTuple, Tuple, Union, get_args


class _Field(NamedTuple):
    required: bool
    nullable: bool
    types: Tuple[Union[type, None]]


class BaseValidator:
    _fields: Dict[str, _Field] = {}

    def __init__(
        self,
        ignore_unexpected_keys=False,
        ignore_type_mismatch=False,
        ignore_missing_keys=False,
        ignore_type_casting=False,
        **kwargs,
    ):
        self.assign_fields()
        self.validate(
            ignore_unexpected_keys,
            ignore_type_mismatch,
            ignore_missing_keys,
            ignore_type_casting,
            **kwargs,
        )

    def assign_fields(self):
        for key, value in self.__annotations__.items():
            args = get_args(value)
            self._fields[key] = _Field(
                type(None) not in args,
                hasattr(self, key),
                args if args else (value,),
            )

    def validate(
        self,
        ignore_unexpected_keys,
        ignore_type_mismatch,
        ignore_missing_keys,
        ignore_type_casting,
        **kwargs,
    ):
        if not self._fields:
            raise Exception("Cannot validate because self._fields is empty")

        for key, value in kwargs.items():
            unexpected_key = False
            if key not in self._fields:
                if not ignore_unexpected_keys:
                    raise ValueError(f"Unexpected key '{key}' in arguments")
                unexpected_key = True

            if not ignore_type_mismatch and not unexpected_key:
                if type(value) not in self._fields[key].types and type(
                    value
                ) is not type(None):
                    raise ValueError(
                        f"Unexpected type '{type(value)}' for key '{key}', expected one of {self._fields[key].types}"
                    )

            cast = None
            if (ignore_type_casting or not value) or unexpected_key:
                cast = value
            else:
                for cast_type in self._fields[key].types:
                    try:
                        cast = cast_type(value)
                    except:
                        pass

                    if cast:
                        break

            if not unexpected_key:
                del self._fields[key]
            setattr(self, key, cast)

        for key in list(self._fields.keys()):
            if self._fields[key].required and not ignore_missing_keys:
                raise ValueError(f"Missing key '{key}'")

            del self._fields[key]
