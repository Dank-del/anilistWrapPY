# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

from anilistWrapPY.errors.types import AniListError
from anilistWrapPY.errors.ex_class import AniListException
from anilistWrapPY.Anime.types import AniListAnime
from anilistWrapPY.Anime.graphql import anime_query
import httpx

def GetAnime(search: str, baseUrl: str) -> AniListAnime:
    variables = {"search": search}
    r = (httpx.post(baseUrl, json={"query": anime_query, "variables": variables})).json()
    try:
        return AniListAnime(**r)
    except AniListException:
        return AniListError(**r)