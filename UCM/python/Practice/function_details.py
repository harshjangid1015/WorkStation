def len(p_object):  # real signature unknown; restored from __doc__
    """
    len(object) -> integer

    Return the number of items of a sequence or collection.
    """
    return 0


class Mapping(Iterable[_KT], Container[_KT], Sized, Generic[_KT, _VT_co]):
    # TODO: We wish the key type could also be covariant, but that doesn't work,
    # see discussion in https: //github.com/python/typing/pull/273.
    @abstractmethod
    def __getitem__(self, k: _KT) -> _VT_co:
        ...
    # Mixin methods
    @overload  # type: ignore
    def get(self, k: _KT) -> Optional[_VT_co]: ...
    @overload  # type: ignore
    def get(self, k: _KT, default: Union[_VT_co, _T]) -> Union[_VT_co, _T]: ...
    def keys(self) -> list[_KT]: ...
    def values(self) -> list[_VT_co]: ...
    def items(self) -> list[Tuple[_KT, _VT_co]]: ...
    def iterkeys(self) -> Iterator[_KT]: ...
    def itervalues(self) -> Iterator[_VT_co]: ...
    def iteritems(self) -> Iterator[Tuple[_KT, _VT_co]]: ...
    def __contains__(self, o: object) -> bool: ...


