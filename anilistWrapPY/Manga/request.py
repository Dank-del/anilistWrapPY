# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>
import json

import httpx

from anilistWrapPY.Manga.graphql import manga_query
from anilistWrapPY.Manga.types import AnilistManga, anilist_manga_from_dict
from anilistWrapPY.errors import ani_list_error_from_dict
from anilistWrapPY.errors.ex_class import AniListException


def GetManga(search: str, baseUrl: str) -> AnilistManga:
    variables = {"search": search}
    r = (httpx.post(baseUrl, json={"query": manga_query, "variables": variables})).json()
    try:
        return anilist_manga_from_dict(r)
    except json.JSONDecodeError:
        raise AniListException("{}".format(ani_list_error_from_dict(r)))
