c <- 'https://public.tableau.com/vizql/w/CurriculumVitae-Resume/v/CVResume/sessions/13A3BC18D4AF49F48F2790C96100B700-0:0/commands/tabsrv/render-tooltip-server'
try <- jsonlite::fromJSON(c)

t <- 'https://public.tableau.com/vizportal/api/web/v1/getSessionInfo'
try <- jsonlite::fromJSON(t)

# Lineage?
'https://public.tableau.com/public/apis/workbook/CurriculumVitae-Resume/lineage?no_cache=1605112691645'

# Search for All, Vizzes, Blogs, Resources
'https://public.tableau.com/api/search/query?count=20&language=en-us&query=maps&start=0'
'https://public.tableau.com/api/search/query?count=20&language=en-us&query=maps&start=0&type=vizzes'
'https://public.tableau.com/api/search/query?count=20&language=en-us&query=maps&start=0&type=authors'
'https://public.tableau.com/api/search/query?count=20&language=en-us&query=maps&start=0&type=blogs'
'https://public.tableau.com/api/search/query?count=20&language=en-us&query=maps&start=0&type=resources'


lots_of_sheets <- 'https://public.tableau.com/profile/api/workbook/VizConnect-SmallDesignChoicesThatMakeaBigDifference?'
try <- jsonlite::fromJSON(lots_of_sheets)

less_sheets <- 'https://public.tableau.com/profile/api/workbook/RunningforOlympicGold?'
try <- jsonlite::fromJSON(less_sheets)

t <- 'https://public.tableau.com/profile/api/workbook/ChildMarriage_16014531003290?'
try <- jsonlite::fromJSON(t)