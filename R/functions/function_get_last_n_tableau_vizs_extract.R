library(jsonlite)
library(dplyr)

get_last_n_tableau_vizs_extract <- function(profile_name,n){
  
  
  profile_call <- paste0('https://public.tableau.com/profile/api/',profile_name)
  profile_data <- jsonlite::fromJSON(profile_call)
  
  visible_workbooks <- filter(profile_data$workbooks,showInProfile==TRUE)
  
  profile_workbooks <- paste0('https://public.tableau.com/profile/',profile_name,'#!/vizhome/',gsub('/sheets/','/',visible_workbooks$defaultViewRepoUrl))
  workbooks_last_publish <- visible_workbooks$lastPublishDate
  
  profile_col <- rep(profile_name,length(profile_workbooks))
  
  workbook_df <- data.frame(profile_name=profile_col,workbooks=profile_workbooks,last_publish=workbooks_last_publish,stringsAsFactors = F)
  workbook_df <- dplyr::top_n(workbook_df,n,last_publish)
  
  return(workbook_df)
}