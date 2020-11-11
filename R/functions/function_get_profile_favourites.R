
library(jsonlite)

get_profile_favourites <- function(profile_name){
    
    call <- paste0('https://public.tableau.com/profile/api/favorite/',profile_name,'/workbook?')
    favourites <- jsonlite::fromJSON(call)
    return(favourites)
    
}