# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

import httpx
import json

from anilistWrapPY.Anime.graphql import anime_query
from anilistWrapPY.Anime.types import AniListAnime, ani_list_anime_from_dict
from anilistWrapPY.errors import AniListException, ani_list_error_from_dict


def GetAnime(search: str, baseUrl: str) -> AniListAnime:
    variables = {"search": search}
    r = (httpx.post(baseUrl, json={"query": anime_query, "variables": variables})).json()
    try:
        return ani_list_anime_from_dict(r)
    except json.JSONDecodeError:
        raise AniListException("{]".format(ani_list_error_from_dict(r)))
