# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

from anilistWrapPY.errors import Error
from dataclasses import dataclass
from typing import Optional, Any, List

from anilistWrapPY.utils import from_union, from_int, from_none, from_list, to_class, from_str, to_float, from_float, \
    from_bool


@dataclass
class Avatar:
    large: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Avatar':
        assert isinstance(obj, dict)
        large = from_union([from_str, from_none], obj.get("large"))
        return Avatar(large)

    def to_dict(self) -> dict:
        result: dict = {"large": from_union([from_str, from_none], self.large)}
        return result


@dataclass
class StartDate:
    year: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StartDate':
        assert isinstance(obj, dict)
        year = from_union([from_int, from_none], obj.get("year"))
        return StartDate(year)

    def to_dict(self) -> dict:
        result: dict = {"year": from_union([from_int, from_none], self.year)}
        return result


@dataclass
class Title:
    user_preferred: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Title':
        assert isinstance(obj, dict)
        user_preferred = from_union([from_str, from_none], obj.get("userPreferred"))
        return Title(user_preferred)

    def to_dict(self) -> dict:
        result: dict = {"userPreferred": from_union([from_str, from_none], self.user_preferred)}
        return result


@dataclass
class PurpleNode:
    id: Optional[int] = None
    type: Optional[str] = None
    status: Optional[str] = None
    format: Optional[str] = None
    is_adult: Optional[bool] = None
    banner_image: Optional[str] = None
    title: Optional[Title] = None
    cover_image: Optional[Avatar] = None
    start_date: Optional[StartDate] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleNode':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        type = from_union([from_str, from_none], obj.get("type"))
        status = from_union([from_str, from_none], obj.get("status"))
        format = from_union([from_str, from_none], obj.get("format"))
        is_adult = from_union([from_bool, from_none], obj.get("isAdult"))
        banner_image = from_union([from_str, from_none], obj.get("bannerImage"))
        title = from_union([Title.from_dict, from_none], obj.get("title"))
        cover_image = from_union([Avatar.from_dict, from_none], obj.get("coverImage"))
        start_date = from_union([StartDate.from_dict, from_none], obj.get("startDate"))
        return PurpleNode(id, type, status, format, is_adult, banner_image, title, cover_image, start_date)

    def to_dict(self) -> dict:
        result: dict = {"id": from_union([from_int, from_none], self.id),
                        "type": from_union([from_str, from_none], self.type),
                        "status": from_union([from_str, from_none], self.status),
                        "format": from_union([from_str, from_none], self.format),
                        "isAdult": from_union([from_bool, from_none], self.is_adult),
                        "bannerImage": from_union([from_str, from_none], self.banner_image),
                        "title": from_union([lambda x: to_class(Title, x), from_none], self.title),
                        "coverImage": from_union([lambda x: to_class(Avatar, x), from_none], self.cover_image),
                        "startDate": from_union([lambda x: to_class(StartDate, x), from_none], self.start_date)}
        return result


@dataclass
class AnimeEdge:
    favourite_order: Optional[int] = None
    node: Optional[PurpleNode] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AnimeEdge':
        assert isinstance(obj, dict)
        favourite_order = from_union([from_int, from_none], obj.get("favouriteOrder"))
        node = from_union([PurpleNode.from_dict, from_none], obj.get("node"))
        return AnimeEdge(favourite_order, node)

    def to_dict(self) -> dict:
        result: dict = {"favouriteOrder": from_union([from_int, from_none], self.favourite_order),
                        "node": from_union([lambda x: to_class(PurpleNode, x), from_none], self.node)}
        return result


@dataclass
class MangaClass:
    edges: Optional[List[AnimeEdge]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MangaClass':
        assert isinstance(obj, dict)
        edges = from_union([lambda x: from_list(AnimeEdge.from_dict, x), from_none], obj.get("edges"))
        return MangaClass(edges)

    def to_dict(self) -> dict:
        result: dict = {
            "edges": from_union([lambda x: from_list(lambda x: to_class(AnimeEdge, x), x), from_none], self.edges)}
        return result


@dataclass
class FluffyNode:
    id: Optional[int] = None
    name: Optional[Title] = None
    image: Optional[Avatar] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyNode':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        name = from_union([Title.from_dict, from_none], obj.get("name"))
        image = from_union([Avatar.from_dict, from_none], obj.get("image"))
        return FluffyNode(id, name, image)

    def to_dict(self) -> dict:
        result: dict = {"id": from_union([from_int, from_none], self.id),
                        "name": from_union([lambda x: to_class(Title, x), from_none], self.name),
                        "image": from_union([lambda x: to_class(Avatar, x), from_none], self.image)}
        return result


@dataclass
class CharactersEdge:
    favourite_order: Optional[int] = None
    node: Optional[FluffyNode] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CharactersEdge':
        assert isinstance(obj, dict)
        favourite_order = from_union([from_int, from_none], obj.get("favouriteOrder"))
        node = from_union([FluffyNode.from_dict, from_none], obj.get("node"))
        return CharactersEdge(favourite_order, node)

    def to_dict(self) -> dict:
        result: dict = {"favouriteOrder": from_union([from_int, from_none], self.favourite_order),
                        "node": from_union([lambda x: to_class(FluffyNode, x), from_none], self.node)}
        return result


@dataclass
class Characters:
    edges: Optional[List[CharactersEdge]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Characters':
        assert isinstance(obj, dict)
        edges = from_union([lambda x: from_list(CharactersEdge.from_dict, x), from_none], obj.get("edges"))
        return Characters(edges)

    def to_dict(self) -> dict:
        result: dict = {
            "edges": from_union([lambda x: from_list(lambda x: to_class(CharactersEdge, x), x), from_none], self.edges)}
        return result


@dataclass
class Favourites:
    anime: Optional[MangaClass] = None
    manga: Optional[MangaClass] = None
    characters: Optional[Characters] = None
    staff: Optional[MangaClass] = None
    studios: Optional[MangaClass] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Favourites':
        assert isinstance(obj, dict)
        anime = from_union([MangaClass.from_dict, from_none], obj.get("anime"))
        manga = from_union([MangaClass.from_dict, from_none], obj.get("manga"))
        characters = from_union([Characters.from_dict, from_none], obj.get("characters"))
        staff = from_union([MangaClass.from_dict, from_none], obj.get("staff"))
        studios = from_union([MangaClass.from_dict, from_none], obj.get("studios"))
        return Favourites(anime, manga, characters, staff, studios)

    def to_dict(self) -> dict:
        result: dict = {"anime": from_union([lambda x: to_class(MangaClass, x), from_none], self.anime),
                        "manga": from_union([lambda x: to_class(MangaClass, x), from_none], self.manga),
                        "characters": from_union([lambda x: to_class(Characters, x), from_none], self.characters),
                        "staff": from_union([lambda x: to_class(MangaClass, x), from_none], self.staff),
                        "studios": from_union([lambda x: to_class(MangaClass, x), from_none], self.studios)}
        return result


@dataclass
class MediaListOptions:
    score_format: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MediaListOptions':
        assert isinstance(obj, dict)
        score_format = from_union([from_str, from_none], obj.get("scoreFormat"))
        return MediaListOptions(score_format)

    def to_dict(self) -> dict:
        result: dict = {"scoreFormat": from_union([from_str, from_none], self.score_format)}
        return result


@dataclass
class Options:
    profile_color: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Options':
        assert isinstance(obj, dict)
        profile_color = from_union([from_str, from_none], obj.get("profileColor"))
        return Options(profile_color)

    def to_dict(self) -> dict:
        result: dict = {"profileColor": from_union([from_str, from_none], self.profile_color)}
        return result


@dataclass
class GenrePreview:
    genre: Optional[str] = None
    count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'GenrePreview':
        assert isinstance(obj, dict)
        genre = from_union([from_str, from_none], obj.get("genre"))
        count = from_union([from_int, from_none], obj.get("count"))
        return GenrePreview(genre, count)

    def to_dict(self) -> dict:
        result: dict = {"genre": from_union([from_str, from_none], self.genre),
                        "count": from_union([from_int, from_none], self.count)}
        return result


@dataclass
class StatisticsAnime:
    count: Optional[int] = None
    mean_score: Optional[float] = None
    standard_deviation: Optional[float] = None
    minutes_watched: Optional[int] = None
    episodes_watched: Optional[int] = None
    genre_preview: Optional[List[GenrePreview]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StatisticsAnime':
        assert isinstance(obj, dict)
        count = from_union([from_int, from_none], obj.get("count"))
        mean_score = from_union([from_float, from_none], obj.get("meanScore"))
        standard_deviation = from_union([from_float, from_none], obj.get("standardDeviation"))
        minutes_watched = from_union([from_int, from_none], obj.get("minutesWatched"))
        episodes_watched = from_union([from_int, from_none], obj.get("episodesWatched"))
        genre_preview = from_union([lambda x: from_list(GenrePreview.from_dict, x), from_none], obj.get("genrePreview"))
        return StatisticsAnime(count, mean_score, standard_deviation, minutes_watched, episodes_watched, genre_preview)

    def to_dict(self) -> dict:
        result: dict = {"count": from_union([from_int, from_none], self.count),
                        "meanScore": from_union([to_float, from_none], self.mean_score),
                        "standardDeviation": from_union([to_float, from_none], self.standard_deviation),
                        "minutesWatched": from_union([from_int, from_none], self.minutes_watched),
                        "episodesWatched": from_union([from_int, from_none], self.episodes_watched),
                        "genrePreview": from_union(
                            [lambda x: from_list(lambda x: to_class(GenrePreview, x), x), from_none],
                            self.genre_preview)}
        return result


@dataclass
class Manga:
    count: Optional[int] = None
    mean_score: Optional[float] = None
    standard_deviation: Optional[float] = None
    chapters_read: Optional[int] = None
    volumes_read: Optional[int] = None
    genre_preview: Optional[List[GenrePreview]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Manga':
        assert isinstance(obj, dict)
        count = from_union([from_int, from_none], obj.get("count"))
        mean_score = from_union([from_float, from_none], obj.get("meanScore"))
        standard_deviation = from_union([from_float, from_none], obj.get("standardDeviation"))
        chapters_read = from_union([from_int, from_none], obj.get("chaptersRead"))
        volumes_read = from_union([from_int, from_none], obj.get("volumesRead"))
        genre_preview = from_union([lambda x: from_list(GenrePreview.from_dict, x), from_none], obj.get("genrePreview"))
        return Manga(count, mean_score, standard_deviation, chapters_read, volumes_read, genre_preview)

    def to_dict(self) -> dict:
        result: dict = {"count": from_union([from_int, from_none], self.count),
                        "meanScore": from_union([to_float, from_none], self.mean_score),
                        "standardDeviation": from_union([to_float, from_none], self.standard_deviation),
                        "chaptersRead": from_union([from_int, from_none], self.chapters_read),
                        "volumesRead": from_union([from_int, from_none], self.volumes_read), "genrePreview": from_union(
                [lambda x: from_list(lambda x: to_class(GenrePreview, x), x), from_none], self.genre_preview)}
        return result


@dataclass
class Statistics:
    anime: Optional[StatisticsAnime] = None
    manga: Optional[Manga] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Statistics':
        assert isinstance(obj, dict)
        anime = from_union([StatisticsAnime.from_dict, from_none], obj.get("anime"))
        manga = from_union([Manga.from_dict, from_none], obj.get("manga"))
        return Statistics(anime, manga)

    def to_dict(self) -> dict:
        result: dict = {"anime": from_union([lambda x: to_class(StatisticsAnime, x), from_none], self.anime),
                        "manga": from_union([lambda x: to_class(Manga, x), from_none], self.manga)}
        return result


@dataclass
class ActivityHistory:
    date: Optional[int] = None
    amount: Optional[int] = None
    level: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ActivityHistory':
        assert isinstance(obj, dict)
        date = from_union([from_int, from_none], obj.get("date"))
        amount = from_union([from_int, from_none], obj.get("amount"))
        level = from_union([from_int, from_none], obj.get("level"))
        return ActivityHistory(date, amount, level)

    def to_dict(self) -> dict:
        result: dict = {"date": from_union([from_int, from_none], self.date),
                        "amount": from_union([from_int, from_none], self.amount),
                        "level": from_union([from_int, from_none], self.level)}
        return result


@dataclass
class Stats:
    activity_history: Optional[List[ActivityHistory]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Stats':
        assert isinstance(obj, dict)
        activity_history = from_union([lambda x: from_list(ActivityHistory.from_dict, x), from_none], obj.get("activityHistory"))
        return Stats(activity_history)

    def to_dict(self) -> dict:
        result: dict = {
            "activityHistory": from_union([lambda x: from_list(lambda x: to_class(ActivityHistory, x), x), from_none],
                                          self.activity_history)}
        return result


@dataclass
class User:
    moderator_roles: None
    id: Optional[int] = None
    name: Optional[str] = None
    previous_names: Optional[List[Any]] = None
    avatar: Optional[Avatar] = None
    banner_image: Optional[str] = None
    about: Optional[str] = None
    is_following: Optional[bool] = None
    is_follower: Optional[bool] = None
    donator_tier: Optional[int] = None
    donator_badge: Optional[str] = None
    created_at: Optional[int] = None
    is_blocked: Optional[bool] = None
    bans: Optional[List[Any]] = None
    options: Optional[Options] = None
    media_list_options: Optional[MediaListOptions] = None
    statistics: Optional[Statistics] = None
    stats: Optional[Stats] = None
    favourites: Optional[Favourites] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        moderator_roles = from_none(obj.get("moderatorRoles"))
        id = from_union([from_int, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        previous_names = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("previousNames"))
        avatar = from_union([Avatar.from_dict, from_none], obj.get("avatar"))
        banner_image = from_union([from_str, from_none], obj.get("bannerImage"))
        about = from_union([from_str, from_none], obj.get("about"))
        is_following = from_union([from_bool, from_none], obj.get("isFollowing"))
        is_follower = from_union([from_bool, from_none], obj.get("isFollower"))
        donator_tier = from_union([from_int, from_none], obj.get("donatorTier"))
        donator_badge = from_union([from_str, from_none], obj.get("donatorBadge"))
        created_at = from_union([from_int, from_none], obj.get("createdAt"))
        is_blocked = from_union([from_bool, from_none], obj.get("isBlocked"))
        bans = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("bans"))
        options = from_union([Options.from_dict, from_none], obj.get("options"))
        media_list_options = from_union([MediaListOptions.from_dict, from_none], obj.get("mediaListOptions"))
        statistics = from_union([Statistics.from_dict, from_none], obj.get("statistics"))
        stats = from_union([Stats.from_dict, from_none], obj.get("stats"))
        favourites = from_union([Favourites.from_dict, from_none], obj.get("favourites"))
        return User(moderator_roles, id, name, previous_names, avatar, banner_image, about, is_following, is_follower, donator_tier, donator_badge, created_at, is_blocked, bans, options, media_list_options, statistics, stats, favourites)

    def to_dict(self) -> dict:
        result: dict = {"moderatorRoles": from_none(self.moderator_roles),
                        "id": from_union([from_int, from_none], self.id),
                        "name": from_union([from_str, from_none], self.name),
                        "previousNames": from_union([lambda x: from_list(lambda x: x, x), from_none],
                                                    self.previous_names),
                        "avatar": from_union([lambda x: to_class(Avatar, x), from_none], self.avatar),
                        "bannerImage": from_union([from_str, from_none], self.banner_image),
                        "about": from_union([from_str, from_none], self.about),
                        "isFollowing": from_union([from_bool, from_none], self.is_following),
                        "isFollower": from_union([from_bool, from_none], self.is_follower),
                        "donatorTier": from_union([from_int, from_none], self.donator_tier),
                        "donatorBadge": from_union([from_str, from_none], self.donator_badge),
                        "createdAt": from_union([from_int, from_none], self.created_at),
                        "isBlocked": from_union([from_bool, from_none], self.is_blocked),
                        "bans": from_union([lambda x: from_list(lambda x: x, x), from_none], self.bans),
                        "options": from_union([lambda x: to_class(Options, x), from_none], self.options),
                        "mediaListOptions": from_union([lambda x: to_class(MediaListOptions, x), from_none],
                                                       self.media_list_options),
                        "statistics": from_union([lambda x: to_class(Statistics, x), from_none], self.statistics),
                        "stats": from_union([lambda x: to_class(Stats, x), from_none], self.stats),
                        "favourites": from_union([lambda x: to_class(Favourites, x), from_none], self.favourites)}
        return result


@dataclass
class Data:
    user: Optional[User] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        user = from_union([User.from_dict, from_none], obj.get("User"))
        return Data(user)

    def to_dict(self) -> dict:
        result: dict = {"User": from_union([lambda x: to_class(User, x), from_none], self.user)}
        return result


@dataclass
class AnilistUser:
    data: Optional[Data] = None
    errors: Optional[List[Error]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AnilistUser':
        assert isinstance(obj, dict)
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        return AnilistUser(data)

    def to_dict(self) -> dict:
        result: dict = {"data": from_union([lambda x: to_class(Data, x), from_none], self.data)}
        return result

