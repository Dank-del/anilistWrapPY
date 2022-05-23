# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

import httpx

from anilistWrapPY.Manga.graphql import manga_query
from anilistWrapPY.Manga.types import AnilistManga
from anilistWrapPY.errors.ex_class import AniListException


def GetManga(search: str, baseUrl: str) -> AnilistManga:
    variables = {"search": search}
    req = httpx.post(baseUrl, json={"query": manga_query, "variables": variables})
    if req.status_code != 200:
        raise AniListException("Status code isn't 200")
    r = req.json()
    try:
        return AnilistManga(**r)
    except BaseException as e:
        raise AniListException(f"{e}") from e
