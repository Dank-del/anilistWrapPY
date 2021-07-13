# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

anime_query = '''query ($id: Int,$search: String) {
    Page (perPage: 10) {
      media (id: $id, type: ANIME,search: $search) { 
        id
        title {
          romaji
          english
          native
        }
        description (asHtml: false)
        startDate{
            year
          }
          episodes
          season
          type
          format
          status
          duration
          siteUrl
          studios{
              nodes{
                   name
              }
          }
          trailer{
               id
               site 
               thumbnail
          }
          externalLinks{
            url
          }
          averageScore
          genres
          bannerImage
      }
    }
    }'''