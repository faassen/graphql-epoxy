from ..field import Field
from ..thunk import TypeThunk


def yank_potential_fields(attrs):
    field_attrs = {}

    for field_attr_name, obj in list(attrs.items()):
        if field_attr_name == 'T':
            continue

        if isinstance(obj, (Field, TypeThunk)):
            field_attrs[field_attr_name] = attrs.pop(field_attr_name)

    return field_attrs
