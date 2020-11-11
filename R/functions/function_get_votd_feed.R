library(jsonlite)

get_votd_feed <- function(n){

  votd <- paste0('https://public.tableau.com/api/gallery?count=',n)
  votd_df <- jsonlite::fromJSON(votd)
  
  return(votd_df$items)
}