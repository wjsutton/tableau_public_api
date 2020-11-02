<h1 style="font-weight:normal">
  Tableau Public API Documentation
</h1>

[![Status](https://img.shields.io/badge/status-active-success.svg)]() [![GitHub Issues](https://img.shields.io/github/issues/wjsutton/tableau_public_api.svg)](https://github.com/wjsutton/tableau_public_api/issues) [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/wjsutton/tableau_public_api.svg)](https://github.com/wjsutton/tableau_public_api/pulls) [![License](https://img.shields.io/badge/license-GNU-blue.svg)](/LICENSE)

This repo for documenting Tableau Public's API and details of its various API calls. 

[Twitter][Twitter] :speech_balloon:&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[LinkedIn][LinkedIn] :necktie:&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[GitHub :octocat:][GitHub]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Website][Website] :link:

<!--
Quick Link 
-->

[Twitter]:https://twitter.com/WJSutton12
[LinkedIn]:https://www.linkedin.com/in/will-sutton-14711627/
[GitHub]:https://github.com/wjsutton
[Website]:https://wjsutton.github.io/

### :a: About

Tableau Public is the free version of Tableau's Desktop product, it allows for the creation and distribution of Tableau dashboards. The Tableau Public platform has an API for handling data relating to user profiles and workbooks (dashboards). This API can be accessed via a web browser or a programming language (R, Python, JavaScript).

Thanks to Jeffrey Shaffer's [blog post](https://www.dataplusscience.com/TableauPublicAPI.html) & Marc Reid's [blog post](https://datavis.blog/2019/05/13/tableau-public-api/) for sharing this information that acting as the starting point for this documentation.

### :inbox_tray: Known API calls
- [Profile](https://github.com/wjsutton/tableau_public_api#profile)
- [Workbooks](https://github.com/wjsutton/tableau_public_api#workbooks)
- [Followers](https://github.com/wjsutton/tableau_public_api#followers)
- [Following](https://github.com/wjsutton/tableau_public_api#following)
- [Favourites](https://github.com/wjsutton/tableau_public_api#favourites)
- [Workbook Image](https://github.com/wjsutton/tableau_public_api#workbook-image)
- [Workbook Thumbnail](https://github.com/wjsutton/tableau_public_api#workbook-thumbnail)

### :bust_in_silhouette: Profile

**API call output**
<br>Retrieve basic counts of a workbooks, followers, following, favourites, details of websites, social media links and the last 30 workbooks associated to a Tableau Public username. Returned as a JSON.

**API call format**
<br>https://public.tableau.com/profile/api/ + **Tableau Public Username** 

**Example API call**
<br>[https://public.tableau.com/profile/api/will7508](https://public.tableau.com/profile/api/will7508)

### :books: Workbooks

**API call output**
<br>Retrieves details of the last 300 workbooks associated to a Tableau Public username. Note that the next 300 workbooks can be retrieved by changing index section to `index=1` or `index=2`, `index=3`, etc. Returned as a JSON.

**API call format**
<br>First 300 workbooks: https://public.tableau.com/profile/api/ + **Tableau Public Username** + /workbooks?count=300&index=0
<br>Next 300 workbooks: https://public.tableau.com/profile/api/ + **Tableau Public Username** + /workbooks?count=300&index=1

**Example API call**
<br>[https://public.tableau.com/profile/api/will7508/workbooks?count=300&index=0](https://public.tableau.com/profile/api/will7508/workbooks?count=300&index=0)

### :busts_in_silhouette: Followers

**API call output**
<br>

**API call format**
<br>https://public.tableau.com/profile/api/followers/ + **Tableau Public Username** + ?count=300&index=0

**Example API call**
<br>[https://public.tableau.com/profile/api/followers/will7508?count=300&index=0](https://public.tableau.com/profile/api/followers/will7508?count=300&index=0)

### :busts_in_silhouette: Following

**API call output**
<br>

**API call format**
<br>https://public.tableau.com/profile/api/following/ + **Tableau Public Username** + ?count=300&index=0

**Example API call**
<br>[https://public.tableau.com/profile/api/following/will7508?count=300&index=0](https://public.tableau.com/profile/api/following/will7508?count=300&index=0)

### :star: Favourites

**API call output**
<br>

**API call format**
<br>https://public.tableau.com/profile/api/favorite/ + **Tableau Public Username** + /workbook?

**Example API call**
<br>[https://public.tableau.com/profile/api/favorite/will7508/workbook?](https://public.tableau.com/profile/api/favorite/will7508/workbook?)

### :chart_with_upwards_trend: Workbook Image

**API call output**
<br>

**API call format**
<br>https://public.tableau.com/static/images/ + **First 2 Letters of Workbook Repo Url** + / + **Workbook Repo Url** + / + **Default View Name (Excluding spaces & fullstops)** + /1.png

**Example API call**
<br>[https://public.tableau.com/static/images/Ru/RunningforOlympicGold/RunningforOlympicGold/1.png](https://public.tableau.com/static/images/Ru/RunningforOlympicGold/RunningforOlympicGold/1.png)

### :chart_with_upwards_trend: Workbook Thumbnail

**API call output**
<br>

**API call format**
<br>https://public.tableau.com/thumb/views/ + **Workbook Repo Url** + / + **Default View Name (Excluding spaces & fullstops)** 

**Example API call**
<br>[https://public.tableau.com/thumb/views/RunningforOlympicGold/RunningforOlympicGold](https://public.tableau.com/thumb/views/RunningforOlympicGold/RunningforOlympicGold)
