#!/usr/bin/env python3
"""Download the public YC company dataset (yc-oss/api, mirrors the YC directory) to data/raw/yc_all.json."""
import json, sys, urllib.request, pathlib

URLS = [
    "https://raw.githubusercontent.com/yc-oss/api/main/companies/all.json",
    "https://yc-oss.github.io/api/companies/all.json",
]
OUT = pathlib.Path(__file__).resolve().parent.parent / "data" / "raw" / "yc_all.json"


def main():
    last = None
    for url in URLS:
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                data = json.load(r)
            if not isinstance(data, list) or not data:
                raise ValueError("unexpected payload")
            OUT.parent.mkdir(parents=True, exist_ok=True)
            OUT.write_text(json.dumps(data, ensure_ascii=False))
            print(f"saved {len(data)} companies from {url} -> {OUT}")
            return 0
        except Exception as e:  # try next mirror
            last = e
            print(f"failed {url}: {e}", file=sys.stderr)
    print(f"all sources failed: {last}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
