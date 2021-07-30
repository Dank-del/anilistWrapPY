# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

import httpx

from anilistWrapPY.Media.graphql import media_query
from anilistWrapPY.Media.types import AnilistMedia
from anilistWrapPY.errors.ex_class import AniListException
from anilistWrapPY.errors.types import AniListError


def GetMedia(search: str, baseUrl: str) -> AnilistMedia:
    variables = {"search": search}
    req = httpx.post(baseUrl, json={"query": media_query, "variables": variables})
    if req.status_code != 200:
        raise AniListException("Status code isn't 200")
    r = req.json()
    try:
        return AnilistMedia(**r)
    except BaseException as e:
        raise AniListException("{}".format(e))