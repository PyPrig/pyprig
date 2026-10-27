from functools import cache
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyprig import BaseModel
    from pyprig.fields import FieldInfo


@cache
def import_cached_base_model() -> type['BaseModel']:
    from pyprig import BaseModel

    return BaseModel


@cache
def import_cached_field_info() -> type['FieldInfo']:
    from pyprig.fields import FieldInfo

    return FieldInfo
