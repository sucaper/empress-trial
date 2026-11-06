#!/usr/bin/env python3
"""Submit every URL in sitemap.xml to IndexNow (Bing, Yandex, Naver, Seznam, ...).

Run after a deployment has finished so the key file is publicly reachable.
Output is ASCII only to stay safe on Windows consoles with GBK code page.
"""

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEY = "734b6caf8f93eddf535b1ba6dabf7c15"
HOST = "empress-trial.pages.dev"
SITEMAP = ROOT / "sitemap-empress.xml"
ENDPOINT = "https://api.indexnow.org/indexnow"


def main() -> int:
    text = SITEMAP.read_text(encoding="utf-8")
    urls = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", text)
    if not urls:
        print("[FAIL] No URLs found in sitemap.xml")
        return 1

    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": "https://{}/{}.txt".format(HOST, KEY),
        "urlList": urls,
    }
    request = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=40) as response:
            print("[OK] {} URLs submitted, HTTP {}".format(len(urls), response.status))
            return 0
    except urllib.error.HTTPError as exc:
        print("[FAIL] HTTP {} - {}".format(exc.code, exc.reason))
        print("       Check that https://{}/{}.txt is reachable and contains the key.".format(HOST, KEY))
        return 1
    except urllib.error.URLError as exc:
        print("[FAIL] Network error: {}".format(exc.reason))
        return 1


if __name__ == "__main__":
    sys.exit(main())
