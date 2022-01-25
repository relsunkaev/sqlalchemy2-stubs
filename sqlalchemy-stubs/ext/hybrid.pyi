from typing import (
    Any,
    Callable,
    Generic,
    Optional,
    overload,
    Sequence,
    Tuple,
    Type,
    TypeVar,
)
from typing_extensions import Self

from .. import util as util
from ..orm import attributes as attributes
from ..orm import interfaces as interfaces
from ..sql import elements as elements

HYBRID_METHOD: util.langhelpers._symbol
HYBRID_PROPERTY: util.langhelpers._symbol

_T = TypeVar("_T")
_V = TypeVar("_V")

class hybrid_method(Generic[_T, _V], interfaces.InspectionAttrInfo):
    is_attribute: bool
    extension_type: util.langhelpers._symbol
    func: Callable[..., Any] = ...
    expr: Optional[Callable[..., elements.ClauseElement]] = ...
    def __init__(
        self,
        func: Callable[..., Any],
        expr: Optional[Callable[..., elements.ClauseElement]] = ...,
    ) -> None: ...
    @overload
    def __get__(self, instance: _T, owner: Type[_T]) -> Any: ...
    @overload
    def __get__(
        self, instance: None, owner: Type[_T]
    ) -> elements.ClauseElement: ...
    def expression(
        self, expr: Callable[..., elements.ClauseElement]
    ) -> Self: ...

class hybrid_property(Generic[_T, _V], interfaces.InspectionAttrInfo):
    is_attribute: bool
    extension_type: util.langhelpers._symbol
    fget: Callable[[_T], _V] = ...
    fset: Optional[Callable[[_T, _V], None]] = ...
    fdel: Optional[Callable[[_T], None]] = ...
    expr: Optional[Callable[[Type[_T]], elements.ClauseElement]] = ...
    custom_comparator: Optional[Callable[[type[_T]], Comparator]] = ...

    update_expr: Optional[
        Callable[
            [Type[_T], _V],
            Sequence[Tuple[attributes.InstrumentedAttribute, Any]],
        ]
    ] = ...
    def __init__(
        self,
        fget: Callable[[_T], _V],
        fset: Optional[Callable[[_T, _V], None]] = ...,
        fdel: Optional[Callable[[_T], None]] = ...,
        expr: Optional[Any] = ...,
        custom_comparator: Optional[Callable[[type[_T]], Comparator]] = ...,
        update_expr: Optional[Any] = ...,
    ) -> None: ...
    @overload
    def __get__(self, instance: _T, owner: Type[_T]) -> _V: ...
    @overload
    def __get__(self, instance: None, owner: Type[_T]) -> Comparator: ...
    def __set__(self, instance: _T, value: _V) -> None: ...
    def __delete__(self, instance: _T) -> None: ...
    @property
    def overrides(self): ...
    def getter(self, fget: Callable[[_T], _V]) -> Self: ...
    def setter(self, fset: Callable[[_T, _V], None]) -> Self: ...
    def deleter(self, fdel: Callable[[_T], None]) -> Self: ...
    def expression(
        self, expr: Callable[[Type[_T]], elements.ClauseElement]
    ) -> Self: ...
    def comparator(
        self, comparator: Callable[[type[_T]], Comparator]
    ) -> Self: ...
    def update_expression(
        self,
        meth: Callable[
            [Type[_T], _V],
            Sequence[Tuple[attributes.InstrumentedAttribute, Any]],
        ],
    ) -> Self: ...

class Comparator(interfaces.PropComparator):
    property: Any = ...
    expression: Any = ...
    def __init__(self, expression: Any) -> None: ...
    def __clause_element__(self): ...
    def adapt_to_entity(self, adapt_to_entity: Any) -> Self: ...
