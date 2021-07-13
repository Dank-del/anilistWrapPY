# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

media_query = '''query ($search: String) {
  Page (perPage: 10) {
    media (search: $search) {
      id
      title {
        romaji
        english
        native
      }
      type
      format
      status
      description
      episodes
      bannerImage
      externalLinks {
        url
      }
      duration
      chapters
      volumes
      genres
      synonyms
      averageScore
      airingSchedule(notYetAired: true) {
        nodes {
          airingAt
          timeUntilAiring
          episode
        }
      }
      siteUrl
    }
  }
}
'''