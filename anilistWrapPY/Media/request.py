# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

from anilistWrapPY.Media.types import AniListMedia
from anilistWrapPY.Media.graphql import media_query
import httpx


def GetMedia(search: str, baseUrl: str) -> AniListMedia:
    variables = {"search": search}
    r = (httpx.post(baseUrl, json={"query": media_query, "variables": variables})).json()
    return AniListMedia(**r)