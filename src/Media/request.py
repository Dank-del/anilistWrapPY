from anilistWrapPY.Media.types import AniListMedia
from anilistWrapPY.Media.graphql import media_query
import httpx

baseUrl = "https://graphql.anilist.co"

def GetMedia(search: str) -> AniListMedia:
    variables = {"search": search}
    r = (httpx.post(baseUrl, json={"query": media_query, "variables": variables})).json()
    return AniListMedia(**r)