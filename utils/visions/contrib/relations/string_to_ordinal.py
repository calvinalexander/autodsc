# import pandas as pd
#
# from autodsc.utils.visions.relations.relations import InferenceRelation
# from autodsc.utils.visions.relations.relations_utils import values_are_consecutive
# from autodsc.utils.visions.types.ordinal import to_ordinal
#
#
# def is_ordinal_str(s: pd.Series, state: dict) -> bool:
#     if s.str.len().max() == 1:
#         unique_values = list(s[s.notna()].str.lower().unique())
#         return "a" in unique_values and values_are_consecutive(
#             list(map(ord, unique_values))
#         )
#     else:
#         return False
#
#
# def string_to_ordinal() -> InferenceRelation:
#     from autodsc.utils.visions.types import String
#
#     return InferenceRelation(
#         related_type=String,
#         relationship=is_ordinal_str,
#         transformer=to_ordinal,
#     )
