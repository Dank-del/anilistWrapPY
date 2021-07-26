# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>


from anilistWrapPY.Airing.request import GetAiring
from anilistWrapPY.Manga.request import GetManga
from anilistWrapPY.Anime.request import GetAnime
from anilistWrapPY.Character.request import GetCharacter
from anilistWrapPY.Media.request import GetMedia
from anilistWrapPY.User.request import GetUser


class aniWrapPYClient:
    def __init__(self, *, baseUrl: str = "https://graphql.anilist.co") -> None:
        self.baseUrl = baseUrl

    def Anime(self, query: str):
        return GetAnime(search=query, baseUrl=self.baseUrl)

    def Media(self, query: str):
        return GetMedia(search=query, baseUrl=self.baseUrl)

    def Character(self, query: str):
        return GetCharacter(search=query, baseUrl=self.baseUrl)

    def Manga(self, query: str):
        return GetManga(search=query, baseUrl=self.baseUrl)

    def Airing(self, query: str):
        return GetAiring(search=query, baseUrl=self.baseUrl)

    def User(self, query: str):
        return GetUser(search=query, baseUrl=self.baseUrl)
