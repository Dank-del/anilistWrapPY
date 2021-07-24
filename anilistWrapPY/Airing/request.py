# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

import httpx
import json

from anilistWrapPY.Airing.graphql import airing_query
from anilistWrapPY.Airing.types import AnilistAiring, anilist_airing_from_dict
from anilistWrapPY.errors import AniListException, ani_list_error_from_dict


def GetAiring(search: str, baseUrl: str) -> AnilistAiring:
    variables = {"search": search}
    r = (httpx.post(baseUrl, json={"query": airing_query, "variables": variables})).json()
    try:
        return anilist_airing_from_dict(r)
    except json.JSONDecodeError:
        raise AniListException("{}".format(ani_list_error_from_dict(r)))
