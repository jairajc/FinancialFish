#!/usr/bin/env python3
"""
Polymarket read-only smoke test.

Fetches the top 5 active events by 24h volume from the Gamma API
and prints a summary.  No wallet, no auth, no trading.

Usage:
    python -m wrapper.test_polymarket
"""

import json
import sys

import httpx

GAMMA_URL = "https://gamma-api.polymarket.com"


def fetch_top_events(limit: int = 5) -> list[dict]:
    resp = httpx.get(
        f"{GAMMA_URL}/events",
        params={
            "active": "true",
            "closed": "false",
            "order": "volume",
            "ascending": "false",
            "limit": str(limit),
        },
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json()


def fetch_tags() -> list[dict]:
    resp = httpx.get(f"{GAMMA_URL}/tags", timeout=15)
    resp.raise_for_status()
    return resp.json()


def print_event_summary(event: dict, idx: int) -> None:
    title = event.get("title") or event.get("slug", "???")
    markets = event.get("markets") or []

    print(f"\n{'='*60}")
    print(f"  [{idx}] {title}")
    print(f"{'='*60}")

    if not markets:
        print("  (no child markets)")
        return

    for m in markets[:3]:
        question = m.get("question", "???")

        raw_prices = m.get("outcomePrices", "[]")
        prices = json.loads(raw_prices) if isinstance(raw_prices, str) else raw_prices
        yes_price = prices[0] if prices else "?"

        raw_volume = m.get("volumeNum") or m.get("volume", 0)
        volume = float(raw_volume) if raw_volume else 0
        end_date = m.get("endDate", "?")

        print(f"  Q:      {question}")
        print(f"  YES:    {yes_price}")
        print(f"  Volume: ${volume:,.0f}")
        print(f"  Ends:   {end_date}")
        print()


def main() -> None:
    print("Fetching top 5 active Polymarket events by 24h volume ...\n")

    try:
        events = fetch_top_events(5)
    except httpx.HTTPStatusError as exc:
        print(f"HTTP error: {exc.response.status_code} {exc.response.text[:200]}")
        sys.exit(1)
    except httpx.ConnectError as exc:
        print(f"Connection error: {exc}")
        sys.exit(1)

    if not events:
        print("No active events returned.")
        sys.exit(1)

    for i, ev in enumerate(events, 1):
        print_event_summary(ev, i)

    print(f"\nFetching available tags ...")
    try:
        tags = fetch_tags()
        tag_names = [t.get("label") or t.get("name", "?") for t in tags[:15]]
        print(f"  Top tags: {', '.join(tag_names)}")
    except Exception as exc:
        print(f"  (could not fetch tags: {exc})")

    print(f"\n--- GATE PASSED: {len(events)} events fetched successfully ---")


if __name__ == "__main__":
    main()
