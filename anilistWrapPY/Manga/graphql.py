manga_query = '''
query ($id: Int,$search: String) {
  Page (perPage: 10) {
      media (id: $id, type: MANGA,search: $search) {
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
          type
          format
          status
          siteUrl
          averageScore
          genres
          bannerImage
      }
  }
}
'''