#!/usr/bin/env python3

"""
Sports Odds API Python SDK - Streaming Example

This example demonstrates:
- Setting up real-time event streaming via WebSocket
- Connecting to Pusher for live updates
- Handling event changes as they occur
- Maintaining local event state
- Graceful shutdown

Note: Streaming requires an AllStar plan subscription
"""

# Standard Library Imports
import os
import sys
import time
import signal
import traceback
from datetime import datetime

# Third-Party Imports
import pusher

import sports_odds_api
from sports_odds_api import SportsGameOdds

# Get your API key from https://sportsgameodds.com/pricing
# Note: Streaming requires an AllStar plan subscription
API_KEY = os.environ.get("SPORTS_ODDS_API_KEY_HEADER")

if not API_KEY:
    print("Error: SPORTS_ODDS_API_KEY_HEADER environment variable not set")
    print("Usage: export SPORTS_ODDS_API_KEY_HEADER='your-api-key-here'")
    exit(1)

# Initialize the client
client = SportsGameOdds(
    api_key_param=API_KEY,
    timeout=30.0,
    max_retries=2,
)

print("Sports Odds API Python SDK - Streaming Example")
print("Note: Streaming requires an AllStar plan subscription\n")

# Global state for events
events = {}
pusher_client = None


def handle_shutdown(_signum, _frame):
    """Handle graceful shutdown on Ctrl+C"""
    print("\n\nDisconnecting...")
    if pusher_client:
        pusher_client.disconnect()
    print("✓ Disconnected from stream")
    sys.exit(0)


# Register signal handler for Ctrl+C
signal.signal(signal.SIGINT, handle_shutdown)

try:
    STREAM_FEED = "events:live"  # Options: events:upcoming, events:byid, events:live

    print("=== Setting up Event Stream ===")
    print(f"Feed: {STREAM_FEED}\n")

    # Initialize events dictionary
    events = {}

    # Call this endpoint to get initial data and connection parameters
    print("Fetching stream info and initial data...")
    stream_info = client.stream.events(feed=STREAM_FEED)

    # Seed initial data
    for event in stream_info.data:
        events[event.event_id] = event

    print(f"✓ Loaded {len(events)} initial events")
    print("✓ Connecting to WebSocket...")

    # Connect to WebSocket server
    pusher_client = pusher.Pusher(
        app_id=stream_info.pusher_key,
        **stream_info.pusher_options,
    )

    # Subscribe to the channel
    channel = pusher_client.subscribe(stream_info.channel)

    # Bind to the 'data' event
    def handle_event(changed_events):
        """Handle incoming event updates"""
        print(
            f"\n[{datetime.now().strftime('%H:%M:%S')}] Received update for {len(changed_events)} event(s)"
        )

        # Get the eventIDs that changed
        event_ids = ",".join([e["eventID"] for e in changed_events])

        # Get the full event data for the changed events
        updated_page = client.events.get(event_i_ds=event_ids)

        for event in updated_page.data:
            # Update our data with the full event data
            events[event.event_id] = event

            print(f"  Updated: {event.event_id}")
            if hasattr(event, "teams") and hasattr(event.teams, "away") and hasattr(event.teams.away, "names"):
                away_name = getattr(event.teams.away.names, "long", None)
                home_name = getattr(event.teams.home.names, "long", None)
                if away_name and home_name:
                    print(f"    {away_name} @ {home_name}")

    channel.bind("data", handle_event)

    # Connect to Pusher
    pusher_client.connect()

    print("✓ Connected! Listening for updates...")
    print("Press Ctrl+C to stop\n")

    # Keep the script running
    while True:
        time.sleep(1)

except sports_odds_api.PermissionDeniedError:
    print("✗ Error: Streaming requires an AllStar plan subscription")
    print("Visit https://sportsgameodds.com/pricing to upgrade your plan")
except sports_odds_api.APIError as e:
    print(f"✗ API Error: {e.message if hasattr(e, 'message') else str(e)}")
    print(f"Error type: {e.__class__.__name__}")
except Exception as e:
    print(f"✗ Unexpected error: {str(e)}")
    print(f"Error type: {e.__class__.__name__}")
    # traceback is now correctly imported at the top
    print("\n".join(traceback.format_tb(e.__traceback__)[:5]))
finally:
    if pusher_client:
        pusher_client.disconnect()
