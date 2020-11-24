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
- [Featured Authors](https://github.com/wjsutton/tableau_public_api#user-content-notebook-featured-authors)
- [VOTD Dashboards](https://github.com/wjsutton/tableau_public_api#user-content-chart_with_upwards_trend-votd-dashboards)

## :gift: Projects
- [2020-08-24 Will Sutton's Assembling a Gallery of Iron Viz Submissions](https://wjsutton.github.io/data-viz/2020/08/24/Ironviz-2020-Gallery.html)
- [2020-10-31 Annabelle Rincon's Landing Page for Tableau Public](https://rativiz.wordpress.com/2020/10/31/landing-page-for-tableau-public-and-monitoring/)


### :bust_in_silhouette: Profile

**API call output**
<br>Retrieve basic counts of workbooks, followers, following, favourites, details of websites, social media links and the last 21 workbooks associated to a Tableau Public username. Returned as a JSON.

**API call format**
<br>https://public.tableau.com/profile/api/ + **Tableau Public Username** 

**Example API call**
<br>[https://public.tableau.com/profile/api/will7508](https://public.tableau.com/profile/api/will7508)


### :books: Workbooks

**API call output**
<br>Retrieves details of the last 300 workbooks associated to a Tableau Public username. Note that the next 300 workbooks can be retrieved by changing the index section to `index=1` or `index=2`, `index=3`, etc. Returned as a JSON.

**API call format**
<br>First 300 workbooks: https://public.tableau.com/profile/api/ + **Tableau Public Username** + /workbooks?count=300&index=0
<br>Next 300 workbooks: https://public.tableau.com/profile/api/ + **Tableau Public Username** + /workbooks?count=300&index=1

**Example API call**
<br>[https://public.tableau.com/profile/api/will7508/workbooks?count=300&index=0](https://public.tableau.com/profile/api/will7508/workbooks?count=300&index=0)


### :busts_in_silhouette: Followers

**API call output**
<br>Retrieves a list of followers for a Tableau Public User, returns usernames, user metadata, details of their latest workbook. Note that the count of accounts appears to be unlimited, i.e. `count=300` will return up to 300 accounts, `count=1000` will return up to 1,000 accounts.

**API call format**
<br>Get 300 followers: https://public.tableau.com/profile/api/followers/ + **Tableau Public Username** + ?count=300&index=0
<br>Get 1,000 followers: https://public.tableau.com/profile/api/followers/ + **Tableau Public Username** + ?count=1000&index=0

**Example API call**
<br>[https://public.tableau.com/profile/api/followers/will7508?count=300&index=0](https://public.tableau.com/profile/api/followers/will7508?count=300&index=0)


### :busts_in_silhouette: Following

**API call output**
<br>Retrieves a list of accounts being followed by a Tableau Public User, returns usernames, user metadata, details of their latest workbook. Note that the count of accounts appears to be unlimited, i.e. `count=300` will return up to 300 accounts, `count=1000` will return up to 1,000 accounts.

**API call format**
<br>Get 300 following: https://public.tableau.com/profile/api/following/ + **Tableau Public Username** + ?count=300&index=0
<br>Get 1,000 following: https://public.tableau.com/profile/api/following/ + **Tableau Public Username** + ?count=1000&index=0

**Example API call**
<br>[https://public.tableau.com/profile/api/following/will7508?count=300&index=0](https://public.tableau.com/profile/api/following/will7508?count=300&index=0)


### :star: Favourites

**API call output**
<br>Returns a list of workbookRepoUrls favourited by a Tableau Public User, in JSON format.

**API call format**
<br>https://public.tableau.com/profile/api/favorite/ + **Tableau Public Username** + /workbook?

**Example API call**
<br>[https://public.tableau.com/profile/api/favorite/will7508/workbook?](https://public.tableau.com/profile/api/favorite/will7508/workbook?)


### :books: Workbook Image

**API call output**
<br>Returns a screenshot image of the entire dashboard.

**API call format**
<br>https://public.tableau.com/static/images/ + **First 2 Letters of Workbook Repo Url** + / + **Workbook Repo Url** + / + **Default View Name (Excluding spaces & fullstops)** + /1.png

**Example API call**
<br>[https://public.tableau.com/static/images/Ru/RunningforOlympicGold/RunningforOlympicGold/1.png](https://public.tableau.com/static/images/Ru/RunningforOlympicGold/RunningforOlympicGold/1.png)


### :books: Workbook Thumbnail

**API call output**
<br>Returns a thumbnail-sized image, typically found on a Tableau Public author's page.

**API call format**
<br>https://public.tableau.com/thumb/views/ + **Workbook Repo Url** + / + **Default View Name (Excluding spaces & fullstops)** 

**Example API call**
<br>[https://public.tableau.com/thumb/views/RunningforOlympicGold/RunningforOlympicGold](https://public.tableau.com/thumb/views/RunningforOlympicGold/RunningforOlympicGold)


### :books: Workbook Details

**API call output**
<br>Returns a details of a single workbook based on WorkbookRepoUrl, used in the favourites section of the Tableau Public profile to look up details of a workbook e.g. views, titles, etc.

**API call format**
<br>https://public.tableau.com/profile/api/single_workbook/ + **Workbook Repo Url** + ?

**Example API call**
<br>[https://public.tableau.com/profile/api/single_workbook/RunningforOlympicGold?](https://public.tableau.com/profile/api/single_workbook/RunningforOlympicGold?)


### :books: Workbook Contents

**API call output**
<br>Returns a details of a single workbook based on WorkbookRepoUrl, returns some metadata about the workbook (author, titles) and all visible sheets/dashboards/stories packaged with the workbook as found under the "Metadata" section when viewing a viz on Tableau Public. These are found under the `viewInfos` section, they list out a sheetRepoUrlwe can be modified to produce a URL to that sheet/dashboard/story, e.g. 
<br>sheetRepoUrl: VizConnect-SmallDesignChoicesThatMakeaBigDifference/sheets/IncreasingWhiteSpace-Borders
<br>URL: [https://public.tableau.com/profile/simon.beaumont#!/vizhome/VizConnect-SmallDesignChoicesThatMakeaBigDifference/IncreasingWhiteSpace-Borders](https://public.tableau.com/profile/simon.beaumont#!/vizhome/VizConnect-SmallDesignChoicesThatMakeaBigDifference/IncreasingWhiteSpace-Borders)

**API call format**
<br>https://public.tableau.com/profile/api/workbook/ + **Workbook Repo Url** + ?

**Example API call**
<br>[https://public.tableau.com/profile/api/workbook/VizConnect-SmallDesignChoicesThatMakeaBigDifference?](https://public.tableau.com/profile/api/workbook/VizConnect-SmallDesignChoicesThatMakeaBigDifference?)


### :notebook: Featured Authors 

**API call output**
<br>Returns a Tableau Public profile name and bio of their featured authors as JSON.

**API call format**
<br>https://public.tableau.com/s/authors/list/feed? 

**Example API call**
<br>[https://public.tableau.com/s/authors/list/feed?](https://public.tableau.com/s/authors/list/feed?)


### :chart_with_upwards_trend: VOTD Dashboards

**API call output**
<br>Returns a list of the most recent VOTD winners from the page [https://public.tableau.com/en-us/gallery/?tab=viz-of-the-day&type=viz-of-the-day](https://public.tableau.com/en-us/gallery/?tab=viz-of-the-day&type=viz-of-the-day)

**API call format**
<br>https://public.tableau.com/api/gallery?page=0&count= + **Number of VOTD** + &galleryType=viz-of-the-day&language=en-us

**Example API call**
<br>Get last 100 VOTDs: [https://public.tableau.com/api/gallery?page=0&count=100&galleryType=viz-of-the-day&language=en-us
](https://public.tableau.com/api/gallery?page=0&count=100&galleryType=viz-of-the-day&language=en-us
)

