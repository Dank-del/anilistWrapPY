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