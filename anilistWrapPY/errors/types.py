# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

from anilistWrapPY.utils.utils import from_int, from_list, from_none, from_str, from_union, to_class
from dataclasses import dataclass
from typing import Optional, Any, List
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
