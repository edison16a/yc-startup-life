#!/usr/bin/env python3
"""Flatten data/raw/yc_all.json into data/companies.csv (base facts only; no enrichment)."""
import csv, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "yc_all.json"
OUT = ROOT / "data" / "companies.csv"

COLS = ["slug", "name", "batch", "batch_year", "status", "stage", "top_company", "nonprofit",
        "team_size", "industry", "subindustry", "tags", "one_liner", "long_description",
        "website", "all_locations", "regions", "launched_at", "yc_url"]


def batch_year(b):
    m = re.search(r"(19|20)\d{2}", b or "")
    return int(m.group(0)) if m else ""


def main():
    data = json.loads(RAW.read_text())
    rows = []
    for c in data:
        rows.append({
            "slug": c.get("slug"), "name": c.get("name"), "batch": c.get("batch"),
            "batch_year": batch_year(c.get("batch")), "status": c.get("status"),
            "stage": c.get("stage"), "top_company": c.get("top_company"),
            "nonprofit": c.get("nonprofit"), "team_size": c.get("team_size"),
            "industry": c.get("industry"), "subindustry": c.get("subindustry"),
            "tags": "; ".join(c.get("tags") or []),
            "one_liner": c.get("one_liner"), "long_description": c.get("long_description"),
            "website": c.get("website"), "all_locations": c.get("all_locations"),
            "regions": "; ".join(c.get("regions") or []),
            "launched_at": c.get("launched_at"), "yc_url": c.get("url"),
        })
    rows.sort(key=lambda r: (r["batch_year"] or 0, r["name"] or ""))
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows)} rows -> {OUT}")


if __name__ == "__main__":
    main()
