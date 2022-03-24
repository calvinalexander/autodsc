# import pandas as pd
#
# from autodsc.utils.visions.relations import InferenceRelation
# from autodsc.utils.visions.relations.relations_utils import values_are_consecutive
# from autodsc.utils.visions.types.ordinal import to_ordinal
#
#
# def is_ordinal_int(s: pd.Series, state: dict) -> bool:
#     initial_element = 1
#     distinct_values = list(s.unique())
#     return (
#         initial_element in distinct_values
#         and values_are_consecutive(distinct_values)
#         and 2 < len(distinct_values) < 10
#     )
#
#
# def integer_to_ordinal() -> InferenceRelation:
#     from autodsc.utils.visions.types import Integer
#
#     return InferenceRelation(
#         Integer, relationship=is_ordinal_int, transformer=to_ordinal
#     )
