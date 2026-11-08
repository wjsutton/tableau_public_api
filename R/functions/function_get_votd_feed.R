library(jsonlite)

get_votd_feed <- function(n){

  votd <- paste0('https://public.tableau.com/public/apis/bff/discover/v2/vizzes/viz-of-the-day?startIndex=0&limit=',n)  # n must be 1 or 12
  votd_df <- jsonlite::fromJSON(votd)
  
  return(votd_df$contents)
}