# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

airing_query = '''
query ($id: Int,$search: String) {
   Page (perPage: 10) {
      media (id: $id, type: ANIME,search: $search) {
        id
        bannerImage
        episodes
        title {
          romaji
          english
          native
        }
        siteUrl
        nextAiringEpisode {
           airingAt
           timeUntilAiring
           episode
        }
      }
    }
}
'''