#!/usr/bin/env python3

"""
Sports Odds API Python SDK - Odds Query Example

This example demonstrates:
- Querying for specific events (NFL, not finalized, with odds)
- Parsing odds data into a structured format
- Grouping odds by bet type
- Displaying summary statistics
"""

import os

from sports_odds_api import SportsGameOdds

# Get your API key from https://sportsgameodds.com/pricing
API_KEY = os.environ.get("SPORTS_ODDS_API_KEY_HEADER")

if not API_KEY:
    print("Error: SPORTS_ODDS_API_KEY_HEADER environment variable not set")
    print("Usage: export SPORTS_ODDS_API_KEY_HEADER='your-api-key-here'")
    exit(1)

# Initialize the client
client = SportsGameOdds(
    api_key_param=API_KEY,
    timeout=30.0,
    max_retries=2
)

print("Sports Odds API Python SDK - Odds Query Example\n")

# Query for NFL events that are not finalized and have odds available
print("=== Querying NFL Events with Odds ===")
print("Filters: leagueID=NFL, finalized=False, oddsAvailable=True\n")

page = client.events.get(
    league_id="NFL",
    finalized=False,
    odds_available=True,
    limit=10
)

if not page.data:
    print("No NFL events with odds found")
    exit(0)

print(f"Found {len(page.data)} NFL events with odds\n")

# Parse all odds markets into a map
# Structure: { eventID: { betTypeID: [markets] } }
odds_map = {}

for event in page.data:
    event_id = event.event_id
    odds_map[event_id] = {}

    print(f"Event: {event_id}")
    print(f"  {event.teams.away.names.long} @ {event.teams.home.names.long}")

    # Check if odds exist
    if not hasattr(event, 'odds') or not event.odds:
        print("  No odds markets available\n")
        continue

    # Group odds by betTypeID
    # IMPORTANT: event.odds is a dict/object keyed by oddID, NOT a list!
    for _odd_id, odd in event.odds.items():
        bet_type_id = odd.bet_type_id
        if bet_type_id not in odds_map[event_id]:
            odds_map[event_id][bet_type_id] = []
        odds_map[event_id][bet_type_id].append(odd)

    # Display summary of odds markets for this event
    if odds_map[event_id]:
        print("  Odds Markets:")
        for bet_type_id, markets in odds_map[event_id].items():
            print(f"    betTypeID {bet_type_id}: {len(markets)} markets")
    else:
        print("  No odds markets available")

    print()

# Display summary
print("\n=== Summary ===")
total_events = len(odds_map)
total_bet_types = sum(len(markets) for markets in odds_map.values())
total_markets = sum(
    len(markets_list)
    for markets in odds_map.values()
    for markets_list in markets.values()
)

print(f"Total events processed: {total_events}")
print(f"Total unique bet types: {total_bet_types}")
print(f"Total odds markets: {total_markets}")

# Show example of accessing the odds map
if odds_map:
    first_event_id = next(iter(odds_map.keys()))
    print(f"\nExample - Accessing odds for event {first_event_id}:")
    for bet_type_id, markets in odds_map[first_event_id].items():
        print(f"  betTypeID {bet_type_id}: {len(markets)} markets")
        if markets:
            first_market = markets[0]
            print(f"    Sample market: bookmakerID={first_market.bookmaker_id}, price={first_market.price}")

print("\nOdds query example completed successfully!")
