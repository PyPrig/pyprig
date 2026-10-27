import sys
from collections.abc import Callable
from typing import Any

from pyprig.warnings import PydanticDeprecatedSince20

from .version import version_short

MOVED_IN_V2 = {
    'pyprig.utils:version_info': 'pyprig.version:version_info',
    'pyprig.error_wrappers:ValidationError': 'pyprig:ValidationError',
    'pyprig.utils:to_camel': 'pyprig.alias_generators:to_pascal',
    'pyprig.utils:to_lower_camel': 'pyprig.alias_generators:to_camel',
    'pyprig:PyObject': 'pyprig.types:ImportString',
    'pyprig.types:PyObject': 'pyprig.types:ImportString',
    'pyprig.generics:GenericModel': 'pyprig.BaseModel',
}

DEPRECATED_MOVED_IN_V2 = {
    'pyprig.tools:schema_of': 'pyprig.deprecated.tools:schema_of',
    'pyprig.tools:parse_obj_as': 'pyprig.deprecated.tools:parse_obj_as',
    'pyprig.tools:schema_json_of': 'pyprig.deprecated.tools:schema_json_of',
    'pyprig.json:pydantic_encoder': 'pyprig.deprecated.json:pydantic_encoder',
    'pyprig:validate_arguments': 'pyprig.deprecated.decorator:validate_arguments',
    'pyprig.json:custom_pydantic_encoder': 'pyprig.deprecated.json:custom_pydantic_encoder',
    'pyprig.json:timedelta_isoformat': 'pyprig.deprecated.json:timedelta_isoformat',
    'pyprig.decorator:validate_arguments': 'pyprig.deprecated.decorator:validate_arguments',
    'pyprig.class_validators:validator': 'pyprig.deprecated.class_validators:validator',
    'pyprig.class_validators:root_validator': 'pyprig.deprecated.class_validators:root_validator',
    'pyprig.config:BaseConfig': 'pyprig.deprecated.config:BaseConfig',
    'pyprig.config:Extra': 'pyprig.deprecated.config:Extra',
}

REDIRECT_TO_V1 = {
    f'pyprig.utils:{obj}': f'pyprig.v1.utils:{obj}'
    for obj in (
        'deep_update',
        'GetterDict',
        'lenient_issubclass',
        'lenient_isinstance',
        'is_valid_field',
        'update_not_none',
        'import_string',
        'Representation',
        'ROOT_KEY',
        'smart_deepcopy',
        'sequence_like',
    )
}


REMOVED_IN_V2 = {
    'pyprig:ConstrainedBytes',
    'pyprig:ConstrainedDate',
    'pyprig:ConstrainedDecimal',
    'pyprig:ConstrainedFloat',
    'pyprig:ConstrainedFrozenSet',
    'pyprig:ConstrainedInt',
    'pyprig:ConstrainedList',
    'pyprig:ConstrainedSet',
    'pyprig:ConstrainedStr',
    'pyprig:JsonWrapper',
    'pyprig:NoneBytes',
    'pyprig:NoneStr',
    'pyprig:NoneStrBytes',
    'pyprig:Protocol',
    'pyprig:Required',
    'pyprig:StrBytes',
    'pyprig:compiled',
    'pyprig.config:get_config',
    'pyprig.config:inherit_config',
    'pyprig.config:prepare_config',
    'pyprig:create_model_from_namedtuple',
    'pyprig:create_model_from_typeddict',
    'pyprig.dataclasses:create_pydantic_model_from_dataclass',
    'pyprig.dataclasses:make_dataclass_validator',
    'pyprig.dataclasses:set_validation',
    'pyprig.datetime_parse:parse_date',
    'pyprig.datetime_parse:parse_time',
    'pyprig.datetime_parse:parse_datetime',
    'pyprig.datetime_parse:parse_duration',
    'pyprig.error_wrappers:ErrorWrapper',
    'pyprig.errors:AnyStrMaxLengthError',
    'pyprig.errors:AnyStrMinLengthError',
    'pyprig.errors:ArbitraryTypeError',
    'pyprig.errors:BoolError',
    'pyprig.errors:BytesError',
    'pyprig.errors:CallableError',
    'pyprig.errors:ClassError',
    'pyprig.errors:ColorError',
    'pyprig.errors:ConfigError',
    'pyprig.errors:DataclassTypeError',
    'pyprig.errors:DateError',
    'pyprig.errors:DateNotInTheFutureError',
    'pyprig.errors:DateNotInThePastError',
    'pyprig.errors:DateTimeError',
    'pyprig.errors:DecimalError',
    'pyprig.errors:DecimalIsNotFiniteError',
    'pyprig.errors:DecimalMaxDigitsError',
    'pyprig.errors:DecimalMaxPlacesError',
    'pyprig.errors:DecimalWholeDigitsError',
    'pyprig.errors:DictError',
    'pyprig.errors:DurationError',
    'pyprig.errors:EmailError',
    'pyprig.errors:EnumError',
    'pyprig.errors:EnumMemberError',
    'pyprig.errors:ExtraError',
    'pyprig.errors:FloatError',
    'pyprig.errors:FrozenSetError',
    'pyprig.errors:FrozenSetMaxLengthError',
    'pyprig.errors:FrozenSetMinLengthError',
    'pyprig.errors:HashableError',
    'pyprig.errors:IPv4AddressError',
    'pyprig.errors:IPv4InterfaceError',
    'pyprig.errors:IPv4NetworkError',
    'pyprig.errors:IPv6AddressError',
    'pyprig.errors:IPv6InterfaceError',
    'pyprig.errors:IPv6NetworkError',
    'pyprig.errors:IPvAnyAddressError',
    'pyprig.errors:IPvAnyInterfaceError',
    'pyprig.errors:IPvAnyNetworkError',
    'pyprig.errors:IntEnumError',
    'pyprig.errors:IntegerError',
    'pyprig.errors:InvalidByteSize',
    'pyprig.errors:InvalidByteSizeUnit',
    'pyprig.errors:InvalidDiscriminator',
    'pyprig.errors:InvalidLengthForBrand',
    'pyprig.errors:JsonError',
    'pyprig.errors:JsonTypeError',
    'pyprig.errors:ListError',
    'pyprig.errors:ListMaxLengthError',
    'pyprig.errors:ListMinLengthError',
    'pyprig.errors:ListUniqueItemsError',
    'pyprig.errors:LuhnValidationError',
    'pyprig.errors:MissingDiscriminator',
    'pyprig.errors:MissingError',
    'pyprig.errors:NoneIsAllowedError',
    'pyprig.errors:NoneIsNotAllowedError',
    'pyprig.errors:NotDigitError',
    'pyprig.errors:NotNoneError',
    'pyprig.errors:NumberNotGeError',
    'pyprig.errors:NumberNotGtError',
    'pyprig.errors:NumberNotLeError',
    'pyprig.errors:NumberNotLtError',
    'pyprig.errors:NumberNotMultipleError',
    'pyprig.errors:PathError',
    'pyprig.errors:PathNotADirectoryError',
    'pyprig.errors:PathNotAFileError',
    'pyprig.errors:PathNotExistsError',
    'pyprig.errors:PatternError',
    'pyprig.errors:PyObjectError',
    'pyprig.errors:PydanticTypeError',
    'pyprig.errors:PydanticValueError',
    'pyprig.errors:SequenceError',
    'pyprig.errors:SetError',
    'pyprig.errors:SetMaxLengthError',
    'pyprig.errors:SetMinLengthError',
    'pyprig.errors:StrError',
    'pyprig.errors:StrRegexError',
    'pyprig.errors:StrictBoolError',
    'pyprig.errors:SubclassError',
    'pyprig.errors:TimeError',
    'pyprig.errors:TupleError',
    'pyprig.errors:TupleLengthError',
    'pyprig.errors:UUIDError',
    'pyprig.errors:UUIDVersionError',
    'pyprig.errors:UrlError',
    'pyprig.errors:UrlExtraError',
    'pyprig.errors:UrlHostError',
    'pyprig.errors:UrlHostTldError',
    'pyprig.errors:UrlPortError',
    'pyprig.errors:UrlSchemeError',
    'pyprig.errors:UrlSchemePermittedError',
    'pyprig.errors:UrlUserInfoError',
    'pyprig.errors:WrongConstantError',
    'pyprig.main:validate_model',
    'pyprig.networks:stricturl',
    'pyprig:parse_file_as',
    'pyprig:parse_raw_as',
    'pyprig:stricturl',
    'pyprig.tools:parse_file_as',
    'pyprig.tools:parse_raw_as',
    'pyprig.types:ConstrainedBytes',
    'pyprig.types:ConstrainedDate',
    'pyprig.types:ConstrainedDecimal',
    'pyprig.types:ConstrainedFloat',
    'pyprig.types:ConstrainedFrozenSet',
    'pyprig.types:ConstrainedInt',
    'pyprig.types:ConstrainedList',
    'pyprig.types:ConstrainedSet',
    'pyprig.types:ConstrainedStr',
    'pyprig.types:JsonWrapper',
    'pyprig.types:NoneBytes',
    'pyprig.types:NoneStr',
    'pyprig.types:NoneStrBytes',
    'pyprig.types:StrBytes',
    'pyprig.typing:evaluate_forwardref',
    'pyprig.typing:AbstractSetIntStr',
    'pyprig.typing:AnyCallable',
    'pyprig.typing:AnyClassMethod',
    'pyprig.typing:CallableGenerator',
    'pyprig.typing:DictAny',
    'pyprig.typing:DictIntStrAny',
    'pyprig.typing:DictStrAny',
    'pyprig.typing:IntStr',
    'pyprig.typing:ListStr',
    'pyprig.typing:MappingIntStrAny',
    'pyprig.typing:NoArgAnyCallable',
    'pyprig.typing:NoneType',
    'pyprig.typing:ReprArgs',
    'pyprig.typing:SetStr',
    'pyprig.typing:StrPath',
    'pyprig.typing:TupleGenerator',
    'pyprig.typing:WithArgsTypes',
    'pyprig.typing:all_literal_values',
    'pyprig.typing:display_as_type',
    'pyprig.typing:get_all_type_hints',
    'pyprig.typing:get_args',
    'pyprig.typing:get_origin',
    'pyprig.typing:get_sub_types',
    'pyprig.typing:is_callable_type',
    'pyprig.typing:is_classvar',
    'pyprig.typing:is_finalvar',
    'pyprig.typing:is_literal_type',
    'pyprig.typing:is_namedtuple',
    'pyprig.typing:is_new_type',
    'pyprig.typing:is_none_type',
    'pyprig.typing:is_typeddict',
    'pyprig.typing:is_typeddict_special',
    'pyprig.typing:is_union',
    'pyprig.typing:new_type_supertype',
    'pyprig.typing:resolve_annotations',
    'pyprig.typing:typing_base',
    'pyprig.typing:update_field_forward_refs',
    'pyprig.typing:update_model_forward_refs',
    'pyprig.utils:ClassAttribute',
    'pyprig.utils:DUNDER_ATTRIBUTES',
    'pyprig.utils:PyObjectStr',
    'pyprig.utils:ValueItems',
    'pyprig.utils:almost_equal_floats',
    'pyprig.utils:get_discriminator_alias_and_values',
    'pyprig.utils:get_model',
    'pyprig.utils:get_unique_discriminator_alias',
    'pyprig.utils:in_ipython',
    'pyprig.utils:is_valid_identifier',
    'pyprig.utils:path_type',
    'pyprig.utils:validate_field_name',
    'pyprig:validate_model',
}


def getattr_migration(module: str) -> Callable[[str], Any]:
    """Implement PEP 562 for objects that were either moved or removed on the migration
    to V2.

    Args:
        module: The module name.

    Returns:
        A callable that will raise an error if the object is not found.
    """
    # This avoids circular import with errors.py.
    from .errors import PydanticImportError

    def wrapper(name: str) -> object:
        """Raise an error if the object is not found, or warn if it was moved.

        In case it was moved, it still returns the object.

        Args:
            name: The object name.

        Returns:
            The object.
        """
        if name == '__path__':
            raise AttributeError(f'module {module!r} has no attribute {name!r}')

        import warnings

        from ._internal._validators import import_string

        import_path = f'{module}:{name}'
        if import_path in MOVED_IN_V2:
            new_location = MOVED_IN_V2[import_path]
            warnings.warn(
                f'`{import_path}` has been moved to `{new_location}`.',
                category=PydanticDeprecatedSince20,
                stacklevel=2,
            )
            return import_string(new_location)
        if import_path in DEPRECATED_MOVED_IN_V2:
            # skip the warning here because a deprecation warning will be raised elsewhere
            return import_string(DEPRECATED_MOVED_IN_V2[import_path])
        if import_path in REDIRECT_TO_V1:
            new_location = REDIRECT_TO_V1[import_path]
            warnings.warn(
                f'`{import_path}` has been removed. We are importing from `{new_location}` instead.'
                f' See the migration guide for more details: https://pydantic.dev/docs/validation/{version_short()}/migration/',
                category=PydanticDeprecatedSince20,
                stacklevel=2,
            )
            return import_string(new_location)
        if import_path == 'pyprig:BaseSettings':
            raise PydanticImportError(
                '`BaseSettings` has been moved to the `pydantic-settings` package. '
                f'See https://pydantic.dev/docs/validation/{version_short()}/migration/#basesettings-has-moved-to-pydantic-settings '
                'for more details.'
            )
        if import_path in REMOVED_IN_V2:
            raise PydanticImportError(f'`{import_path}` has been removed in V2.')
        globals: dict[str, Any] = sys.modules[module].__dict__
        if name in globals:
            return globals[name]
        raise AttributeError(f'module {module!r} has no attribute {name!r}')

    return wrapper
