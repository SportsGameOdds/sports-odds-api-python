#!/usr/bin/env python3

"""
Sports Odds API Python SDK - Basic Usage Example

This example demonstrates:
- Initializing the client with an API key
- Fetching events with pagination
- Auto-pagination to iterate through all results
- Basic error handling
"""

import os

import sports_odds_api
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

print("Sports Odds API Python SDK - Basic Usage Examples\n")

# Example 1: Fetch recent events
print("=== Fetching Events ===")
page = client.events.get(limit=10)

if not page.data:
    print("No events found")
else:
    print(f"Found {len(page.data)} events:")
    for event in page.data[:3]:
        print(f"  - {event.event_id}: {event.activity}")

# Example 2: Auto-pagination
print("\n=== Auto-Pagination Example ===")
count = 0

# The SDK automatically handles pagination when iterating
for event in client.events.get(limit=5):
    count += 1
    if count <= 10:
        print(f"  Event {count}: {event.event_id}")
    if count >= 15:  # Limit for demo purposes
        break

print(f"Processed {count} events across multiple pages")

# Example 3: Error handling
print("\n=== Error Handling Example ===")
try:
    client.events.get(eventIDs="invalid-id")
except sports_odds_api.NotFoundError as e:
    print(f"Caught NotFoundError: {e.message}")
except sports_odds_api.APIError as e:
    print(f"Caught APIError: {e.__class__.__name__}")

print("\nExamples completed successfully!")
