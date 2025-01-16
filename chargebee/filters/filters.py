from typing import List, NotRequired, TypedDict


class Filters:
    class StringFilter(TypedDict):
        IS: NotRequired[str]
        IS_NOT: NotRequired[str]
        STARTS_WITH: NotRequired[str]
        IN: NotRequired[List[str]]
        NOT_IN: NotRequired[List[str]]
        IS_PRESENT: NotRequired[bool]

    class BooleanFilter(TypedDict):
        IS: NotRequired[bool]
        IS_PRESENT: NotRequired[bool]

    class EnumFilter(TypedDict):
        IS: NotRequired[str]
        IS_NOT: NotRequired[str]
        IS_PRESENT: NotRequired[bool]
        IN: NotRequired[List[str]]
        NOT_IN: NotRequired[List[str]]

    class NumberFilter(TypedDict):
        IS: NotRequired[int]
        IS_NOT: NotRequired[int]
        LT: NotRequired[int]
        LTE: NotRequired[int]
        GT: NotRequired[int]
        GTE: NotRequired[int]
        BETWEEN: NotRequired[List[int]]
        IS_PRESENT: NotRequired[bool]

    class SortFilter(TypedDict):
        ASC: NotRequired[str]
        DESC: NotRequired[str]

    class TimestampFilter(TypedDict):
        AFTER: NotRequired[int]
        BEFORE: NotRequired[int]
        ON: NotRequired[int]
        BETWEEN: NotRequired[List[int]]
        IS_PRESENT: NotRequired[bool]
