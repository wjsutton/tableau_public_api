# Sign in to Tableau Public and call the signed-in APIs
#
# Tableau Public has no sign-in API, so this opens a Chrome window and you sign in
# yourself (Tableau ID, MFA, captcha). API calls are then made from inside that
# browser, so your session cookie never leaves it.
#
# Setup:  pip install playwright   (uses your installed Google Chrome, no browser download)
# Run:    python tableau_public_sign_in.py
#
# The browser profile is kept in ~/.tableau-public-python so you only sign in once.
# Delete that folder to sign out on this computer. Treat it like a password.

import os
import time
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from playwright.sync_api import Page, sync_playwright

BASE_URL = 'https://public.tableau.com'
PROFILE_DIR = Path(os.environ.get('TABLEAU_PUBLIC_PROFILE_DIR', Path.home() / '.tableau-public-python'))

# Runs inside the browser: same-origin fetch with the XSRF header the web app sends
FETCH_JS = '''async ({path, method, body}) => {
  const xsrf = document.cookie.match(/(?:^|;\\s*)XSRF-TOKEN=([^;]+)/)?.[1];
  const headers = {'Accept': 'application/json', 'Content-Type': 'application/json'};
  if (xsrf) headers['X-XSRF-TOKEN'] = decodeURIComponent(xsrf);
  const res = await fetch(path, {method, headers, body});
  const text = await res.text();
  let data = text;
  try { data = JSON.parse(text); } catch (e) {}
  return {status: res.status, data: data};
}'''


def call_api(page: Page, path: str, method: str = 'GET', body: str | None = None) -> tuple[int, Any]:
    """Call a Tableau Public API path from the signed-in browser. Returns (status, data)."""
    result = page.evaluate(FETCH_JS, {'path': path, 'method': method, 'body': body})
    return result['status'], result['data']


@contextmanager
def tableau_public_session(timeout_minutes: int = 5) -> Iterator[Page]:
    """Opens Chrome, waits for you to sign in (skipped if already signed in), yields the page."""
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(PROFILE_DIR, channel='chrome', headless=False)
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(BASE_URL + '/app/discover')

        if call_api(page, '/profile/api/auth/author')[0] != 200:
            print('Sign in to Tableau Public in the Chrome window...')
            page.goto(BASE_URL + '/login')
            deadline = time.time() + timeout_minutes * 60
            while True:
                # Only check once the browser is back on public.tableau.com
                if page.url.startswith(BASE_URL) and call_api(page, '/profile/api/auth/author')[0] == 200:
                    break
                if time.time() > deadline:
                    context.close()
                    raise TimeoutError('Not signed in after %d minutes' % timeout_minutes)
                time.sleep(3)

        try:
            yield page
        finally:
            context.close()


if __name__ == '__main__':
    with tableau_public_session() as page:
        status, author = call_api(page, '/profile/api/auth/author')
        username = author['profileName']
        print('Signed in as', username)

        status, hidden = call_api(page, '/public/apis/workbooks?profileName=' + username +
                                  '&start=0&count=50&visibility=HIDDEN')
        print(len(hidden['contents']), 'hidden workbooks')
        for workbook in hidden['contents']:
            print('-', workbook['title'], '(' + workbook['workbookRepoUrl'] + ')')
