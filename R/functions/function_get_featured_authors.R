library(jsonlite)

get_featured_authors <- function(){
  
  featured_authors_call <- 'https://public.tableau.com/s/authors/list/feed?'
  featured_authors_data <- jsonlite::fromJSON(featured_authors_call)
  featured_authors_df <- featured_authors_data$authors
  
  return(featured_authors_df)
}
