# Build a simple HTML gallery page of a Tableau Public user's vizzes
# username -> workbooks -> thumbnail images -> gallery page

import html
import json
import urllib3

http = urllib3.PoolManager()

your_username = 'wjsutton'

# Get all visible workbooks, 50 at a time, until 'next' is -1
workbooks = []
start = 0
while start != -1:
    workbooks_call = ('https://public.tableau.com/public/apis/workbooks?profileName=' + your_username +
                      '&start=' + str(start) + '&count=50&visibility=NON_HIDDEN')
    response = json.loads(http.request('GET', workbooks_call).data)
    workbooks.extend(response['contents'])
    start = response['next']

print('Found ' + str(len(workbooks)) + ' workbooks')

# Build a card for each workbook with its thumbnail and a link to the viz
cards = []
for workbook in workbooks:
    view = workbook['defaultViewRepoUrl'].replace('/sheets/', '/')
    thumbnail = 'https://public.tableau.com/thumb/views/' + view
    viz_url = 'https://public.tableau.com/app/profile/' + your_username + '/viz/' + view
    title = html.escape(workbook['title'])
    cards.append('<a href="' + viz_url + '"><img src="' + thumbnail + '" alt="' + title + '" loading="lazy">'
                 '<p>' + title + '<br><small>' + str(workbook['viewCount']) + ' views</small></p></a>')

page = ('<!doctype html><html><head><meta charset="utf-8"><title>' + your_username + "'s vizzes</title>"
        '<style>body{font-family:sans-serif;margin:2em}'
        'main{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:1.5em}'
        'a{color:inherit;text-decoration:none}img{width:100%;border:1px solid #ddd}</style></head>'
        '<body><h1>' + your_username + "'s vizzes</h1><main>" + ''.join(cards) + '</main></body></html>')

with open(your_username + '_gallery.html', 'w', encoding='utf-8') as f:
    f.write(page)

print('Saved ' + your_username + '_gallery.html')
