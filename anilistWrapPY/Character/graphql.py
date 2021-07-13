# The contents of this file is free and unencumbered software released into the
# public domain. For more information, please refer to <http://unlicense.org/>

character_query = '''query ($id: Int, $search: String) {
  	Page (perPage: 10) {
	    characters (id: $id, search: $search) {
    	  name {
      	  full
        	native
        	alternative
      	}
      	description
      	image {
          large
        }
        media {
            nodes {
                title {
                    romaji
                    english
                    native
                }
                type
                format
                siteUrl
            }
        }
      	siteUrl
      dateOfBirth {
        year
        month
        day
      }
      age
      favourites
      }
    }
}
'''