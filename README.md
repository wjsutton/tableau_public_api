<h1 style="font-weight:normal">
  Tableau Public API Documentation
</h1>

[![Status](https://img.shields.io/badge/status-active-success.svg)]() [![GitHub Issues](https://img.shields.io/github/issues/wjsutton/tableau_public_api.svg)](https://github.com/wjsutton/tableau_public_api/issues) [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/wjsutton/tableau_public_api.svg)](https://github.com/wjsutton/tableau_public_api/pulls) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

This repo for documenting Tableau Public's API and details of its various API calls. 

[Twitter][Twitter] :speech_balloon:&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[LinkedIn][LinkedIn] :necktie:&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[GitHub :octocat:][GitHub]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Website][Website] :link:

<!--
Quick Link 
-->

[Twitter]:https://twitter.com/WJSutton12
[LinkedIn]:https://www.linkedin.com/in/will-sutton-14711627/
[GitHub]:https://github.com/wjsutton
[Website]:https://wjsutton.github.io/

## :a: About

Tableau Public is the free version of Tableau's Desktop product, it allows for the creation and distribution of Tableau dashboards. The Tableau Public platform has an API for handling data relating to user profiles and workbooks (dashboards). This API can be accessed via a web browser or a programming language (R, Python, JavaScript).

Thanks to Jeffrey Shaffer's [blog post](https://www.dataplusscience.com/TableauPublicAPI.html) & Marc Reid's [blog post](https://datavis.blog/2019/05/13/tableau-public-api/) for sharing this information that acting as the starting point for this documentation.

## :inbox_tray: Known API calls
- [Profile](https://github.com/wjsutton/tableau_public_api#user-content-bust_in_silhouette-profile)
- [Workbooks](https://github.com/wjsutton/tableau_public_api#user-content-books-workbooks)
- [Followers](https://github.com/wjsutton/tableau_public_api#user-content-busts_in_silhouette-followers)
- [Following](https://github.com/wjsutton/tableau_public_api#user-content-busts_in_silhouette-following)
- [Favourites](https://github.com/wjsutton/tableau_public_api#user-content-star-favourites)
- [Workbook Image](https://github.com/wjsutton/tableau_public_api#user-content-books-workbook-image)
- [Workbook Thumbnail](https://github.com/wjsutton/tableau_public_api#user-content-books-workbook-thumbnail)
- [Workbook Details](https://github.com/wjsutton/tableau_public_api#user-content-books-workbook-details)
- [Workbook Contents](https://github.com/wjsutton/tableau_public_api#user-content-books-workbook-contents)
- [Related Workbooks](https://github.com/wjsutton/tableau_public_api#books-related-workbooks)
- [Shared Workbooks](https://github.com/wjsutton/tableau_public_api#books-shared-workbooks)
- [Featured Authors](https://github.com/wjsutton/tableau_public_api#user-content-notebook-featured-authors)
- [VOTD Dashboards](https://github.com/wjsutton/tableau_public_api#user-content-chart_with_upwards_trend-votd-dashboards)
- [Search Results](https://github.com/wjsutton/tableau_public_api#user-content-mag-search-results)

## :gift: Project Walkthroughs
- [2019-03-10, Jeffrey Shaffer's Using the Tableau Public API in 3 Easy Steps](https://www.dataplusscience.com/TableauPublicAPI.html)
- [2019-05-13, Mark Reid's Tableau Public API blog post](https://datavis.blog/2019/05/13/tableau-public-api/)
- [2020-08-24, Will Sutton's Assembling a Gallery of Iron Viz Submissions](https://wjsutton.github.io/data-viz/2020/08/24/Ironviz-2020-Gallery.html)
- [2020-10-31, Annabelle Rincon's Landing Page for Tableau Public](https://rativiz.wordpress.com/2020/10/31/landing-page-for-tableau-public-and-monitoring/)
- [2021-01-21, Curtis Harris Sending Tableau VOTD as a Slack Message](https://notnullisland.com/sending-data-driven-slack-messages-with-tableaus-viz-of-the-day/)
- [2021-05-16, Priyanka Dobhal's Design Your Tableau Portfolio](https://priyankadobhal.medium.com/tableau-design-your-tableau-portfolio-371932a3087a)

## :raised_hands: Community Services
- [Ken Flerage’s Tableau Public Stats Service](https://www.flerlagetwins.com/2021/03/stats-service.html)
- [Josh Tapley’s Cerebro Project, an overview of all Tableau Public Users Stats](https://public.tableau.com/profile/josh.tapley#!/vizhome/TheCerebroProject/Overview)
- [Nir Smilga’s Tableau Public Explorer, an alternative view built from Josh Tapley’s Cerebro Project](https://public.tableau.com/profile/nir.smilga#!/vizhome/TableauPublicExplorer/TableauPublicExplorer)
- [Andre de Vries’ Web data connector for Tableau Public](https://www.theinformationlab.co.uk/2019/05/31/web-data-connector-for-tableau-public/)
- [Jessica Moon's 2022 Iron Viz Qualifier Entries](https://public.tableau.com/app/profile/jessica.moon/viz/IronVizQualifierEntries2022/IronVizQualifierEntries2022)
- [Jessica Moon's 2023 Iron Viz Qualifier Entries](https://public.tableau.com/app/profile/jessica.moon/viz/IronVizQualifierEntries2023/IronVizQualifierEntries2023)

## :floppy_disk: Data sets
- Tableau Public's Viz of the Day : [Google Sheets](https://docs.google.com/spreadsheets/d/10Pm_1wnlUBwpWmLomY7U-yhL0wgLBdiQyeaaF3sV_J0/edit?usp=sharing)

## :inbox_tray: Tableau Public API Calls 

### :bust_in_silhouette: Profile

**API call output**
<br>Retrieve basic counts of workbooks, followers, following, favourites, details of websites, whether they have the "hire me" button on their profile (freelance), social media links and the last 21 workbooks associated to a Tableau Public username. Returned as a JSON.

**API call format**
<br>https://public.tableau.com/profile/api/ + **Tableau Public Username** 

**Example API call**
<br>[https://public.tableau.com/profile/api/wjsutton](https://public.tableau.com/profile/api/wjsutton)

Note a basic user profile description query is available via:
<br>[https://public.tableau.com/public/apis/authors?profileName=wjsutton](https://public.tableau.com/public/apis/authors?profileName=wjsutton)

### :books: Workbooks

**API call output**
<br>Retrieves details of the last 50 workbooks associated to a Tableau Public username. Returned as a JSON.

Note that the next 50 workbooks can be retrieved by changing the start section to `start=50` or `start=100`, `start=150`, etc. 

In Feb 2023 a visibility parameter has been added,'&visibility=NON_HIDDEN' which will only allow the API to reach visible workbooks on a user's profile. 


**API call format**
<br>First 50 workbooks: https://public.tableau.com/public/apis/workbooks?profileName= + **Tableau Public Username** + &start=0&count=50&visibility=NON_HIDDEN
<br><br>Next 50 workbooks: https://public.tableau.com/public/apis/workbooks?profileName= + **Tableau Public Username** + &start=50&count=50&visibility=NON_HIDDEN

**Example API call**
<br>[https://public.tableau.com/public/apis/workbooks?profileName=wjsutton&start=0&count=50&visibility=NON_HIDDEN](https://public.tableau.com/public/apis/workbooks?profileName=wjsutton&start=0&count=50&visibility=NON_HIDDEN)

### :busts_in_silhouette: Followers

**API call output**
<br>Retrieves a list of followers for a Tableau Public User, returns usernames, user metadata, details of their latest workbook. Note that the count of accounts appears to be now limited to 24 per call, i.e. `count=24` will return up to 24 accounts, `count=24&index=24` will return the next 24 accounts.

**API call format**
<br>Get 24 followers: https://public.tableau.com/profile/api/followers/ + **Tableau Public Username** + ?count=24&index=0
<br>Get next 24 followers: https://public.tableau.com/profile/api/followers/ + **Tableau Public Username** + ?count=24&index=24

**Example API call**
<br>[https://public.tableau.com/profile/api/followers/wjsutton?count=24&index=0](https://public.tableau.com/profile/api/followers/wjsutton?count=24&index=0)


### :busts_in_silhouette: Following

**API call output**
<br>Retrieves a list of accounts being followed by a Tableau Public User, returns usernames, user metadata, details of their latest workbook. Note that the count of accounts appears to be now limited to 24 per call, i.e. `count=24` will return up to 24 accounts, `count=24&index=24` will return the next 24 accounts.

**API call format**
<br>Get 24 following: https://public.tableau.com/profile/api/following/ + **Tableau Public Username** + ?count=24&index=0
<br>Get next 24 following: https://public.tableau.com/profile/api/following/ + **Tableau Public Username** + ?count=24&index=24

**Example API call**
<br>[https://public.tableau.com/profile/api/following/wjsutton?count=24&index=0](https://public.tableau.com/profile/api/following/wjsutton?count=24&index=0)


### :star: Favourites

**API call output**
<br>Returns a list of workbookRepoUrls favourited by a Tableau Public User, in JSON format.

**API call format**
<br>https://public.tableau.com/profile/api/favorite/ + **Tableau Public Username** + /workbook?

**Example API call**
<br>[https://public.tableau.com/profile/api/favorite/wjsutton/workbook?](https://public.tableau.com/profile/api/favorite/wjsutton/workbook?)


### :books: Workbook Image

**API call output**
<br>Returns a screenshot image of the entire dashboard.

**UPDATE**
<br>Thanks to [Kelly Gilbert](https://twitter.com/kelly_gilbert/status/1481495266448527363?s=20) there is a more reliable API call for a fullscreen image.
<br>"https://public.tableau.com/views/WORKBOOKNAME/VIEWNAME.png?%3Adisplay_static_image=y&:showVizHome=n"

**API call format**
<br>https://public.tableau.com/views/+ **Workbook Repo Url** + / + **Default View Name (Excluding spaces & fullstops)** + .png?%3Adisplay_static_image=y&:showVizHome=n
<br>OLD Version: https://public.tableau.com/static/images/ + **First 2 Letters of Workbook Repo Url** + / + **Workbook Repo Url** + / + **Default View Name (Excluding spaces & fullstops)** + /1.png

**Example API call**
<br>[https://public.tableau.com/views/RunningforOlympicGold/RunningforOlympicGold.png?%3Adisplay_static_image=y&:showVizHome=n](https://public.tableau.com/views/RunningforOlympicGold/RunningforOlympicGold.png?%3Adisplay_static_image=y&:showVizHome=n)
<br>OLD Version:[https://public.tableau.com/static/images/Ru/RunningforOlympicGold/RunningforOlympicGold/1.png](https://public.tableau.com/static/images/Ru/RunningforOlympicGold/RunningforOlympicGold/1.png)


### :books: Workbook Thumbnail

**API call output**
<br>Returns a thumbnail-sized image, typically found on a Tableau Public author's page. Note there are two different calls to produce a thumbnail image.

**API call format**
<br>https://public.tableau.com/thumb/views/ + **Workbook Repo Url** + / + **Default View Name (Excluding spaces & fullstops)** 
<br>Alternative Call: <br>https://public.tableau.com/static/images/ + **First 2 Letters of Workbook Repo Url** + / + **Workbook Repo Url** + / + **Default View Name (Excluding spaces & fullstops)** + /4_3.png

**Example API call**
<br>[https://public.tableau.com/thumb/views/RunningforOlympicGold/RunningforOlympicGold](https://public.tableau.com/thumb/views/RunningforOlympicGold/RunningforOlympicGold)
<br>Alternative Call: [https://public.tableau.com/static/images/Ru/RunningforOlympicGold/RunningforOlympicGold/4_3.png](https://public.tableau.com/static/images/Ru/RunningforOlympicGold/RunningforOlympicGold/4_3.png)

### :books: Workbook Details

**API call output**
<br>Returns a details of a single workbook based on WorkbookRepoUrl, used in the favourites section of the Tableau Public profile to look up details of a workbook e.g. views, titles, etc.

**API call format**
<br>https://public.tableau.com/profile/api/single_workbook/ + **Workbook Repo Url** + ?

**Example API call**
<br>[https://public.tableau.com/profile/api/single_workbook/RunningforOlympicGold?](https://public.tableau.com/profile/api/single_workbook/RunningforOlympicGold?)


### :books: Workbook Contents

**API call output**
<br>Returns details of a single workbook based on WorkbookRepoUrl, returns some metadata about the workbook (author, titles) and all visible sheets/dashboards/stories packaged with the workbook as found under the "Metadata" section when viewing a viz on Tableau Public. These are found under the `viewInfos` section, they list out a sheetRepoUrlwe can be modified to produce a URL to that sheet/dashboard/story, e.g. 
<br>sheetRepoUrl: VizConnect-SmallDesignChoicesThatMakeaBigDifference/sheets/IncreasingWhiteSpace-Borders
<br>URL: [https://public.tableau.com/profile/simon.beaumont#!/vizhome/VizConnect-SmallDesignChoicesThatMakeaBigDifference/IncreasingWhiteSpace-Borders](https://public.tableau.com/profile/simon.beaumont#!/vizhome/VizConnect-SmallDesignChoicesThatMakeaBigDifference/IncreasingWhiteSpace-Borders)

**API call format**
<br>https://public.tableau.com/profile/api/workbook/ + **Workbook Repo Url** + ?

**Example API call**
<br>[https://public.tableau.com/profile/api/workbook/VizConnect-SmallDesignChoicesThatMakeaBigDifference?](https://public.tableau.com/profile/api/workbook/VizConnect-SmallDesignChoicesThatMakeaBigDifference?)

### :books: Related Workbooks
*Discovered by Chris Meardon*

**API call output**
<br>Returns a list of workbooks (max 13) related to a queried workbook.

**API call format**
<br>https://public.tableau.com/public/apis/bff/workbooks/v1/ + **Workbook Repo Url** /recommended-workbooks? + count= **n**

**Example API call**
<br>https://public.tableau.com/public/apis/bff/workbooks/v1/RunningforOlympicGold/recommended-workbooks?count=13

### :books: Shared Workbooks
*Discovered by a "friend of the repo"*

**API call output**
<br>Returns source workbook details for a shared workbook url.

**API call format**
<br>https://public.tableau.com/profile/api/workbook/shared/ + **Share_id** 

**Example API call**
<br>[https://public.tableau.com/profile/api/workbook/shared/3QJBD7FYC](https://public.tableau.com/profile/api/workbook/shared/3QJBD7FYC)

### :notebook: Featured Authors 

**API call output**
<br>Returns a Tableau Public profile name and bio of their featured authors as JSON.

**API call format**
<br>https://public.tableau.com/s/authors/list/feed? 

**Example API call**
<br>[https://public.tableau.com/s/authors/list/feed?](https://public.tableau.com/s/authors/list/feed?)


### :chart_with_upwards_trend: VOTD Dashboards


**API call output**
<br>Returns a list of the most recent VOTD winners from the page [https://public.tableau.com/app/discover/viz-of-the-day](https://public.tableau.com/app/discover/viz-of-the-day)

**API call format**
<br>https://public.tableau.com/public/apis/bff/discover/v1/vizzes/viz-of-the-day?page= + **Page Number** + &limit= + **Number of VOTDs** (max 12)
<br>
<i>Note to get all VOTDs you will need to iterate through page numbers, increasing by one until no more results are returned.</i>

**Example API call**
<br>Get last 12 VOTDs: [https://public.tableau.com/public/apis/bff/discover/v1/vizzes/viz-of-the-day?page=0&limit=12
](https://public.tableau.com/public/apis/bff/discover/v1/vizzes/viz-of-the-day?page=0&limit=12)
<br>Get next 12 VOTDs: [https://public.tableau.com/public/apis/bff/discover/v1/vizzes/viz-of-the-day?page=1&limit=12
](https://public.tableau.com/public/apis/bff/discover/v1/vizzes/viz-of-the-day?page=1&limit=12
)

### :chart_with_upwards_trend: Historical VOTD Dashboards | DOES NOT WORK ANYMORE

**Historical API call output | DOES NOT WORK ANYMORE**
<br><br>Returns a list of the most recent VOTD winners from the page:
<br>[https://public.tableau.com/en-us/gallery/?tab=viz-of-the-day&type=viz-of-the-day](https://public.tableau.com/en-us/gallery/?tab=viz-of-the-day&type=viz-of-the-day)
<br><br>In addition there is a list of featured vizzes on the page 
<br>[https://public.tableau.com/en-us/gallery/?tab=featured&type=featured](https://public.tableau.com/en-us/gallery/?tab=featured&type=featured)

**Historical API call format | DOES NOT WORK ANYMORE**
<br>https://public.tableau.com/api/gallery?page=0&count= + **Number of VOTDs** + &galleryType=viz-of-the-day&language=en-us
<br>
<br>For featured vizzes:
<br>https://public.tableau.com/api/gallery?page=0&count= + **Number of Vizzes** + &galleryType=featured&language=en-us

**Historical Example API call | DOES NOT WORK ANYMORE**
<br>Get last 100 VOTDs: [https://public.tableau.com/api/gallery?page=0&count=100&galleryType=viz-of-the-day&language=en-us
](https://public.tableau.com/api/gallery?page=0&count=100&galleryType=viz-of-the-day&language=en-us
)
<br>Get last 100 featured vizzes: [https://public.tableau.com/api/gallery?page=0&count=100&galleryType=featured&language=en-us
](https://public.tableau.com/api/gallery?page=0&count=100&galleryType=featured&language=en-us
)

**:floppy_disk: Dataset | NO LONGER UPDATED DUE API CHANGE**
<br>Tableau Public's Viz of the Day : [Google Sheets](https://docs.google.com/spreadsheets/d/10Pm_1wnlUBwpWmLomY7U-yhL0wgLBdiQyeaaF3sV_J0/edit?usp=sharing)



### :mag: Search Results

**API call output**
<br>Returns a list of the top search results for a given query as per the search page  [https://public.tableau.com/en-us/search/vizzes/](https://public.tableau.com/en-us/search/vizzes/)

**API call format**
<br>https://public.tableau.com/api/search/query?count= + **Number of Results** + &language=en-us&query= + **Search Term** +&start= + **Start at Viz Number** + &type= + **vizzes/authors**

**Example API call**
<br>Get top 100 Maps Search Results: [https://public.tableau.com/api/search/query?count=20&language=en-us&query=maps&start=0&type=vizzes
](https://public.tableau.com/api/search/query?count=20&language=en-us&query=maps&start=0&type=vizzes
)

