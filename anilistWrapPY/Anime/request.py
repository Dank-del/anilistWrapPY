# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

import httpx

from anilistWrapPY.Anime.graphql import anime_query
from anilistWrapPY.Anime.types import AniListAnime
from anilistWrapPY.errors import AniListException


def GetAnime(search: str, baseUrl: str) -> AniListAnime:
    variables = {"search": search}
    req = httpx.post(baseUrl, json={"query": anime_query, "variables": variables})
    if req.status_code != 200:
        raise AniListException("Status code isn't 200")
    r = req.json()
    try:
        return AniListAnime(**r)
    except BaseException as e:
        raise AniListException("{}".format(e))