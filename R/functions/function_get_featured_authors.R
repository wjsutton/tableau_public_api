library(jsonlite)

get_featured_authors <- function(){
  
  featured_authors_call <- 'https://public.tableau.com/public/apis/bff/discover/v3/authors/tableau-visionaries?startIndex=0&limit=12'
  featured_authors_data <- jsonlite::fromJSON(featured_authors_call)
  featured_authors_df <- featured_authors_data$contents
  featured_authors_df$profile_name <- featured_authors_df$profileName
  
  return(featured_authors_df)
}
