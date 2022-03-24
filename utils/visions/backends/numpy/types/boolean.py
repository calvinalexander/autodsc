from typing import Dict, List

import numpy as np

from autodsc.utils.visions.backends.numpy.array_utils import (
    all_type,
    array_handle_nulls,
    array_not_empty,
)
from autodsc.utils.visions.backends.numpy.test_utils import coercion_map, coercion_map_test
from autodsc.utils.visions.backends.python.types.boolean import get_boolean_coercions
from autodsc.utils.visions.backends.shared.nan_handling import nan_mask
from autodsc.utils.visions.types.boolean import Boolean
from autodsc.utils.visions.types.object import Object
from autodsc.utils.visions.types.string import String

string_coercions = get_boolean_coercions("en")


@Boolean.register_relationship(Object, np.ndarray)
@array_handle_nulls
def object_is_boolean(array: np.ndarray, state: dict) -> bool:
    return all_type(array, bool)


@Boolean.register_transformer(Object, np.ndarray)
def object_to_boolean(array: np.ndarray, state: dict) -> np.ndarray:
    return array


@Boolean.register_relationship(String, np.ndarray)
def string_is_boolean(array: np.ndarray, state: dict) -> bool:
    try:
        mask = nan_mask(array)
        # TODO: Nan handling not implemented for generators yet
        val_generator = np.array([val.lower() for val in array[mask]])
        return coercion_map_test(string_coercions)(val_generator, state)
    except (ValueError, TypeError, AttributeError):
        return False


@Boolean.register_transformer(String, np.ndarray)
def string_to_boolean(array: np.ndarray, state: dict) -> np.ndarray:
    array = array.copy()
    mask = nan_mask(array)
    # TODO: Nan handling not implemented for generators yet
    val_generator = np.array([val.lower() for val in array[mask]])
    array[mask] = object_to_boolean(
        coercion_map(string_coercions)(val_generator), state
    )
    return array


@Boolean.contains_op.register
@array_handle_nulls
@array_not_empty
def boolean_contains(array: np.ndarray, state: dict) -> bool:
    if np.issubdtype(array.dtype, np.bool_):
        return True

    return all_type(array, bool)
