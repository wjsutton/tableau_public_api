
# Currently Excludes attributions as these are returned as a table withing the dataset

library(jsonlite)

get_workbook_details <- function(workbookRepoUrl){
  
  call <- paste0('https://public.tableau.com/profile/api/single_workbook/',workbookRepoUrl,'?')
  workbook <- jsonlite::fromJSON(call)
  
  workbook_df <- data.frame(
    category = ifelse(is.null(workbook$category),'NA',workbook$category),
    ownerId = workbook$ownerId,
    workbookRepoUrl = workbook$workbookRepoUrl,
    firstPublishDate = workbook$firstPublishDate,
    title = workbook$title,
    description = ifelse(is.null(workbook$description),'NA',workbook$description),
    lastPublishDate = workbook$lastPublishDate,
    permalink = ifelse(is.null(workbook$permalink),'NA',workbook$permalink),
    viewCount = workbook$viewCount,
    showTabs = workbook$showTabs,
    showToolbar = workbook$showToolbar,
    showByline = workbook$showByline,
    showShareOptions = workbook$showShareOptions,
    showWatermark = workbook$showWatermark,
    allowDataAccess = workbook$allowDataAccess,
    defaultViewName = workbook$defaultViewName,
    defaultViewRepoUrl = workbook$defaultViewRepoUrl,
    size = workbook$size,
    revision = workbook$revision,
    extractInfo = ifelse(is.null(workbook$extractInfo),'NA',workbook$extractInfo),
    lastUpdateDate = workbook$lastUpdateDate,
    warnDataAccess = workbook$warnDataAccess,
    authorProfileName = workbook$authorProfileName,
    numberOfFavorites = workbook$numberOfFavorites,
    #attributions = workbook$attributions,
    showInProfile = workbook$showInProfile,
    stringsAsFactors = F
  )
  
  return(workbook_df)
}