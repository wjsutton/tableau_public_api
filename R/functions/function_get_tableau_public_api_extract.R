# Note workbooks includes invisible_workbooks, determined by the 'showInProfile' TRUE/FALSE flag

library(jsonlite)

get_tableau_profile_api_extract <- function(profile_name){
  
  
  profile_call <- paste0('https://public.tableau.com/profile/api/',profile_name)
  
  profile_data <- jsonlite::fromJSON(profile_call)
  
  profile_following <- profile_data$totalNumberOfFollowing
  profile_followers <- profile_data$totalNumberOfFollowers
  
  profile_twitter <- profile_data$websites$url[grepl('twitter',profile_data$websites$url)]
  profile_linkedin <- profile_data$websites$url[grepl('linkedin',profile_data$websites$url)]
  
  profile_last_publish <- profile_data$lastPublishDate
  profile_visible_workbooks <- profile_data$visibleWorkbookCount
  
  profile_following <- ifelse(length(profile_following)==1,profile_following,0)
  profile_followers <- ifelse(length(profile_followers)==1,profile_followers,0)
  
  profile_twitter <- ifelse(length(profile_twitter)==1,profile_twitter,'')
  profile_linkedin <- ifelse(length(profile_linkedin)==1,profile_linkedin,'')
  
  profile_last_publish <- ifelse(length(profile_last_publish)==1,profile_last_publish,0)
  profile_visible_workbooks <- ifelse(length(profile_visible_workbooks)==1,profile_visible_workbooks,0)
  
  profile_df <- data.frame(name=profile_name,
                           profile_url=paste0('https://public.tableau.com/profile/',profile_name,'#!/'),
                           api_call=profile_call,
                           followers=profile_followers,
                           following=profile_following,
                           twitter=profile_twitter,
                           linkedin=profile_linkedin,
                           last_publish=profile_last_publish,
                           visible_workbooks=profile_visible_workbooks,
                           stringsAsFactors = F)
  return(profile_df)
}