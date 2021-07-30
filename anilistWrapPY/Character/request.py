# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

import httpx

from anilistWrapPY.Character.graphql import character_query
from anilistWrapPY.Character.types import AnilistCharacter
from anilistWrapPY.errors.ex_class import AniListException


def GetCharacter(search: str, baseUrl: str) -> AnilistCharacter:
    variables = {"search": search}
    req = httpx.post(baseUrl, json={"query": character_query, "variables": variables})
    if req.status_code != 200:
        raise AniListException("Status code isn't 200")
    r = req.json()
    try:
        return AnilistCharacter(**r)
    except BaseException as e:
        raise AniListException("{}".format(e))
