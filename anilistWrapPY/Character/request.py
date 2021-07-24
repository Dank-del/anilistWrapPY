# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>
import json

import httpx

from anilistWrapPY.Character.graphql import character_query
from anilistWrapPY.Character.types import AniListCharacter, ani_list_character_from_dict
from anilistWrapPY.errors import ani_list_error_from_dict
from anilistWrapPY.errors.ex_class import AniListException


def GetCharacter(search: str, baseUrl: str) -> AniListCharacter:
    variables = {"search": search}
    r = (httpx.post(baseUrl, json={"query": character_query, "variables": variables})).json()
    try:
        return ani_list_character_from_dict(r)
    except json.JSONDecodeError:
        raise AniListException("{}".format(ani_list_error_from_dict(r)))
