# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

import httpx

from anilistWrapPY.Airing.graphql import airing_query
from anilistWrapPY.Airing.types import AnilistAiring
from anilistWrapPY.errors import AniListException


def GetAiring(search: str, baseUrl: str) -> AnilistAiring:
    variables = {"search": search}
    req = httpx.post(baseUrl, json={"query": airing_query, "variables": variables})
    if req.status_code != 200:
        raise AniListException("Status code isn't 200")
    r = req.json()
    
    try:
        return AnilistAiring.from_dict(r)
    except BaseException as e:
        raise AniListException("{}".format(e))
