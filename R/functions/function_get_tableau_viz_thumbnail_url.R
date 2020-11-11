library(longurl)
library(stringr)
library(rvest)
library(httr)
library(dplyr)

# Case A: 'https://public.tableau.com/views/TheBeerMileWorldRecords/TheTop1000BeerMilePerformances?:language=en&:display_count=y&:origin=viz_share_link'
# Case B: 'https://public.tableau.com/profile/will7508#!/vizhome/TheBeerMileWorldRecords/TheTop1000BeerMilePerformances'
# After: 'https://public.tableau.com/thumb/views/TheBeerMileWorldRecords/TheTop1000BeerMilePerformances'

get_tableau_viz_thumbnail_url <- function(urls){
  
  df <- data.frame(original_url=urls, stringsAsFactors = FALSE)
  
  # Case A: https://public.tableau.com/views/IronViz2020EveryMotherCounts-ExploringMaternalHealth/EveryMotherCounts?:language=en-GB&:display_count=y&:origin=viz_share_link
  pattern_a <- "https://public\\.tableau\\.com/views(?:/.*)?"
  
  df$case_a_urls <- ifelse(grepl(pattern_a,df$original_url),df$original_url,NA)
  
  for(i in 1:length(df$case_a_urls)){
    
    viz_a <- df$case_a_urls[i]
    
    # Type A1: views with a ? clause
    if(!is.na(str_locate(pattern="views",viz_a))[1]){
      
      if(!is.na(str_locate(pattern="\\?:|\\?%|\\?&",viz_a))[1]){
        
        # Start of "?:"
        position <- (str_locate_all(pattern="\\?:|\\?%|\\?&",viz_a))[[1]][1,1]
        viz_a <- substr(viz_a,1,position-1)
        
      }
      
      # End of "views"
      views_end_pos <- str_locate_all(pattern="views",viz_a)[[1]][1,2]
      #two_letters_of_dash <- substr(viz_a,views_end_pos+2,views_end_pos+3)
      
      # Start of "views"
      views_start_pos <- str_locate_all(pattern="views",viz_a)[[1]][1,1]
      
      knit <- paste0(substr(viz_a,1,views_start_pos-1),'thumb/views/'
                     ,substr(viz_a,views_end_pos+2,nchar(viz_a)))
    }
    
    if(is.na(str_locate(pattern="views",viz_a))[1]){
      knit <- NA
    }
    
    img <- knit
    
    if(i == 1){
      img_list_a <- img
    }
    
    if(i > 1){
      img_list_a <- c(img_list_a,img)
    }
  }
  
  df$case_a_imgs <- img_list_a
  
  # Case B: https://public.tableau.com/profile/agata1619#!/vizhome/Whattimearebabiesborn/Whattimearebabiesborn?publish=yes
  pattern_b <- 'https://public\\.tableau\\.com/profile/[A-z|0-9|\\.|-]*'
  
  df$case_b_urls <- ifelse(grepl(pattern_b,df$original_url),df$original_url,NA)
  
  # Two types of Tableau links
  # 1. 'views'
  # 2. 'profile vizhome'
  
  for(i in 1:length(df$case_b_urls)){
    
    viz_b <- df$case_b_urls[i]
    
    # Case 2 'profile vizhome'
    if(!is.na(str_locate(pattern="vizhome",viz_b)[1])){
      
      # Start of "?"
      viz_b <- gsub("\\?publish=yes","",viz_b)
      
      # Start of profile
      profile_start_pos <- str_locate_all(pattern="profile",viz_b)[[1]][1,1]
      
      # End of "vizhome"
      vizhome_end_pos <- str_locate_all(pattern="vizhome",viz_b)[[1]][1,2]
      #two_letters_of_dash <- substr(viz_b,vizhome_end_pos+2,vizhome_end_pos+3)
      
      knit <- paste0(substr(viz_b,1,profile_start_pos-1),'thumb/views/'
                     ,substr(viz_b,vizhome_end_pos+2,nchar(viz_b)))
    }
    
    if(is.na(str_locate(pattern="vizhome",viz_b)[1])){
      
      knit <- NA
      
    }
    
    img <- knit
    
    if(i == 1){
      img_list_b <- img
    }
    
    if(i > 1){
      img_list_b <- c(img_list_b,img)
    }
  }
  df$case_b_imgs <- img_list_b
  
  df$viz_img <- ifelse(is.na(df$case_a_imgs),df$case_b_imgs,df$case_a_imgs)
  
  output <- df[,c('original_url','viz_img')]
  return(output)
  
}