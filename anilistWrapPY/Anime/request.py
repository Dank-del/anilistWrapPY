from anilistWrapPY.Anime.types import AniListAnime
from anilistWrapPY.Anime.graphql import anime_query
import httpx

baseUrl = "https://graphql.anilist.co"

def GetAnime(search: str) -> AniListAnime:
    variables = {"search": search}
    r = (httpx.post(baseUrl, json={"query": anime_query, "variables": variables})).json()
    return AniListAnime(**r)