# Get Tableau Public profiles from featured authors URL:
# https://public.tableau.com/en-us/s/authors#!/

library(jsonlite)
source('functions/function_get_tableau_public_api_extract.R')
source('functions/function_get_last_n_tableau_vizs_extract.R')
source('functions/function_get_tableau_viz_screenshot_url.R')
source('functions/function_get_tableau_viz_thumbnail_url.R')
source('functions/function_get_workbook_details.R')
source('functions/function_get_profile_favourites.R')
source('functions/function_get_featured_authors.R')

featured_authors_df <- get_featured_authors()
featured_authors <- featured_authors_df$profile_name

# Get Feature Authors latest vizzes
for(i in 1:length(featured_authors)){
  featured_df <- get_last_n_tableau_vizs_extract(featured_authors[i],20)
  
  for(j in 1:length(featured_df$workbooks)){
    screenshot <- get_tableau_viz_screenshot_url(featured_df$workbooks[j])
    thumbnail <- get_tableau_viz_thumbnail_url(featured_df$workbooks[j])
    
    images <- data.frame(workbooks = featured_df$workbooks[j],
                         workbook_screenshot = screenshot, 
                         workbook_thumbnail = thumbnail, 
                         stringsAsFactors = F)
    
    if(j == 1){
      images_df <- images
    }
    if(j != 1){
      images_df <- rbind(images_df,images)
    }
  }
  
  featured_df <- inner_join(featured_df,images_df, by = ("workbooks" = "workbooks"))
  
  if(i == 1){
    featured_output <- featured_df 
  }
  if(i != 1){
    featured_output <- rbind(featured_output,featured_df)
  }
}

featured_output$last_publish_datetime <- as.POSIXct(featured_output$last_publish/1000, origin="1970-01-01")
featured_output <- arrange(featured_output,-last_publish)
write.csv(featured_output,"data/featured_authors_feed.csv",row.names = F)

for(i in 1:length(featured_authors)){
  favourited <- get_profile_favourites(featured_authors[i])[1:20,]
  
  if(i == 1){
    favourite_df <- favourited
  }
  if(i != 1){
    favourite_df <- c(favourite_df,favourited)
  }
}

favourite_workbooks <- unique(favourite_df[!is.na(favourite_df)])

for(i in 1:length(favourite_workbooks)){
  fav <- get_workbook_details(favourite_workbooks[i])
  
  if(i == 1){
    fav_df <- fav
  }
  if(i != 1){
    fav_df <- rbind(fav_df,fav)
  }
}
visible_favs <- filter(fav_df,showInProfile==TRUE)

fav_workbooks <- paste0('https://public.tableau.com/profile/',visible_favs$authorProfileName,'#!/vizhome/',gsub('/sheets/','/',visible_favs$defaultViewRepoUrl))
#workbooks_last_publish <- visible_workbooks$lastPublishDate



