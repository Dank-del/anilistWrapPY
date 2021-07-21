# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Location:
    line: Optional[int] = None
    column: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Location':
        assert isinstance(obj, dict)
        line = from_union([from_int, from_none], obj.get("line"))
        column = from_union([from_int, from_none], obj.get("column"))
        return Location(line, column)

    def to_dict(self) -> dict:
        result: dict = {"line": from_union([from_int, from_none], self.line),
                        "column": from_union([from_int, from_none], self.column)}
        return result


@dataclass
class Error:
    message: Optional[str] = None
    status: Optional[int] = None
    locations: Optional[List[Location]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Error':
        assert isinstance(obj, dict)
        message = from_union([from_str, from_none], obj.get("message"))
        status = from_union([from_int, from_none], obj.get("status"))
        locations = from_union([lambda x: from_list(Location.from_dict, x), from_none], obj.get("locations"))
        return Error(message, status, locations)

    def to_dict(self) -> dict:
        result: dict = {"message": from_union([from_str, from_none], self.message),
                        "status": from_union([from_int, from_none], self.status),
                        "locations": from_union([lambda x: from_list(lambda x: to_class(Location, x), x), from_none],
                                                self.locations)}
        return result


@dataclass
class AniListError:
    data: None
    errors: Optional[List[Error]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AniListError':
        assert isinstance(obj, dict)
        data = from_none(obj.get("data"))
        errors = from_union([lambda x: from_list(Error.from_dict, x), from_none], obj.get("errors"))
        return AniListError(data, errors)

    def to_dict(self) -> dict:
        result: dict = {"data": from_none(self.data),
                        "errors": from_union([lambda x: from_list(lambda x: to_class(Error, x), x), from_none],
                                             self.errors)}
        return result


def ani_list_error_from_dict(s: Any) -> AniListError:
    return AniListError.from_dict(s)


def ani_list_error_to_dict(x: AniListError) -> Any:
    return to_class(AniListError, x)
