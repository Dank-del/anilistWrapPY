# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>
import json

import httpx

from anilistWrapPY.User.graphql import user_query
from anilistWrapPY.User.types import AnilistUser, anilist_user_from_dict
from anilistWrapPY.errors.ex_class import AniListException
from anilistWrapPY.errors.types import ani_list_error_from_dict


def GetUser(search: str, baseUrl: str) -> AnilistUser:
    variables = {"name": search}
    r = (httpx.post(baseUrl, json={"query": user_query, "variables": variables})).json()
    try:
        return anilist_user_from_dict(r)
    except json.JSONDecodeError:
        raise AniListException("{}".format(ani_list_error_from_dict(r)))
