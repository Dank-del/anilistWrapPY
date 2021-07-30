# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

import httpx

from anilistWrapPY.User.graphql import user_query
from anilistWrapPY.User.types import AnilistUser
from anilistWrapPY.errors.ex_class import AniListException
from anilistWrapPY.errors.types import AniListError


def GetUser(search: str, baseUrl: str) -> AnilistUser:
    variables = {"name": search}
    req = httpx.post(baseUrl, json={"query": user_query, "variables": variables})
    if req.status_code != 200:
        raise AniListException("Status code isn't 200")
    r = req.json()
    try:
        return AnilistUser.from_dict(r)
    except BaseException as e:
        raise AniListException("{}".format(e))
