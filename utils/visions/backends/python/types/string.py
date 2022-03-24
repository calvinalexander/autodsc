from typing import Sequence

from autodsc.utils.visions.backends.python.series_utils import (
    sequence_handle_none,
    sequence_not_empty,
)
from autodsc.utils.visions.types.string import String


@String.contains_op.register
@sequence_not_empty
@sequence_handle_none
def string_contains(sequence: Sequence, state: dict) -> bool:
    return all(isinstance(v, str) for v in sequence)
