from typing import Sequence

from autodsc.utils.visions.backends.python.series_utils import (
    sequence_handle_none,
    sequence_not_empty,
)
from autodsc.utils.visions.types.object import Object


@Object.contains_op.register
@sequence_not_empty
@sequence_handle_none
def object_contains(sequence: Sequence, state: dict) -> bool:
    return any(not isinstance(value, (float, bool, int, complex)) for value in sequence)
