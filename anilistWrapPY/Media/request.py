# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>
import json

import httpx

from anilistWrapPY.Media.graphql import media_query
from anilistWrapPY.Media.types import AniListMedia, ani_list_media_from_dict
from anilistWrapPY.errors.ex_class import AniListException
from anilistWrapPY.errors.types import ani_list_error_from_dict


def GetMedia(search: str, baseUrl: str) -> AniListMedia:
    variables = {"search": search}
    r = (httpx.post(baseUrl, json={"query": media_query, "variables": variables})).json()
    try:
        return ani_list_media_from_dict(r)
    except json.JSONDecodeError:
        raise AniListException("{]".format(ani_list_error_from_dict(r)))
