# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>


from anilistWrapPY.Anime.request import GetAnime
from anilistWrapPY.Character.request import GetCharacter
from anilistWrapPY.Media.request import GetMedia


class aniWrapPYClient:
    def __init__(self, *, baseUrl: str = "https://graphql.anilist.co") -> None:
        self.baseUrl = baseUrl

    def Anime(self, query: str):
        return GetAnime(search=query, baseUrl=self.baseUrl)

    def Media(self, query: str):
        return GetMedia(search=query, baseUrl=self.baseUrl)

    def Character(self, query: str):
        return GetCharacter(search=query, baseUrl=self.baseUrl)
