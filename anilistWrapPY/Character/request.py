# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>
from anilistWrapPY.errors.types import AniListError
from anilistWrapPY.errors.ex_class import AniListException
from anilistWrapPY.Character.types import AniListCharacter
from anilistWrapPY.Character.graphql import character_query
import httpx


def GetCharacter(search: str, baseUrl: str) -> AniListCharacter:
    variables = {"search": search}
    r = (httpx.post(baseUrl, json={"query": character_query, "variables": variables})).json()
    try:
        return AniListCharacter(**r)
    except AniListException:
        return AniListError(**r)