from datetime import timedelta
from typing import Sequence

from autodsc.utils.visions.backends.python.series_utils import sequence_not_empty
from autodsc.utils.visions.types.time_delta import TimeDelta


@TimeDelta.contains_op.register
@sequence_not_empty
def time_delta_contains(sequence: Sequence, state: dict) -> bool:
    return all(isinstance(value, timedelta) for value in sequence)
