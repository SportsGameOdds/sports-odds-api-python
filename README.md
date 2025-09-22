# Sports Odds API - Live Sports Data & Sportsbook Betting Odds - Powered by SportsGameOdds Python API Library

Get live betting odds, spreads, and totals for NFL, NBA, MLB, and 50 additional sports and leagues. Production-ready Python SDK with WebSocket support, 99.9% uptime, and sub-minute updates during live games. Perfect for developers building sportsbook platforms, odds comparison tools, positive EV models, and anything else that requires fast, accurate sports data.

[![PyPI version](https://img.shields.io/pypi/v/sports-odds-api.svg?label=pypi%20(stable))](https://pypi.org/project/sports-odds-api/)

This library provides convenient access to the Sports Game Odds REST API from Python 3.8+ applications.

The REST API documentation can be found on [sportsgameodds.com](https://sportsgameodds.com/docs/). The full API of this library can be found in [api.md](api.md).

## Features

**For developers building the next generation of sports stats and/or betting applications:**

- 📈 **3k+ odds markets** including moneylines, spreads, over/unders, team props, player props & more
- 🏈 **50+ leagues covered** including NFL, NBA, MLB, NHL, NCAAF, NCAAB, EPL, UCL, UFC, PGA, ATP & more
- 📊 **80+ sportsbooks** with unified odds formats, alt lines & deeplinks
- 📺 **Live scores & stats** coverage on all games, teams, and players
- ⚡ **Sub-100ms response times** and sub-minute updates for fast data
- 🔧 **Typed requests & responses** via Pydantic models
- 💰 **Developer-friendly pricing** with a generous free tier
- ⏱️ **5-minute setup** with copy-paste examples

## Installation

```sh
pip install sports-odds-api
```

## Obtain an API Key

Get a free API key from [sportsgameodds.com](https://sportsgameodds.com/pricing).

Unlike enterprise-only solutions, the Sports Game Odds API offers a developer-friendly experience, transparent pricing, comprehensive documentation, and a generous free tier.

## Usage

The full API of this library can be found in [api.md](api.md).

```python
import os
from sports_odds_api import SportsGameOdds

client = SportsGameOdds(
    api_key_param=os.environ.get("SPORTS_ODDS_API_KEY_HEADER"),  # default, can be omitted
)

page = client.events.get()
event = page.data[0]

print(event.activity)
```

# Real-Time Event Streaming API

This API endpoint is only available to **AllStar** and **custom plan** subscribers. It is not included with basic subscription tiers. [Contact support](mailto:api@sportsgameodds.com) to get access.

This streaming API is currently in **beta**. API call patterns, response formats, and functionality may change. Fully managed streaming via SDK may be available in future releases.

Our Streaming API provides real-time updates for Event objects through WebSocket connections. Instead of polling our REST endpoints, you can maintain a persistent connection to receive instant notifications when events change. This is ideal for applications that need immediate updates with minimal delay.

We use [Pusher Protocol](https://pusher.com/docs/channels/library_auth_reference/pusher-websockets-protocol/) for WebSocket communication. While you can connect using any WebSocket library, we strongly recommend using any [Pusher Client Library](https://pusher.com/docs/channels/library_auth_reference/pusher-client-libraries) (ex: [Python](https://github.com/pusher/pusher-http-python))

## How It Works

The streaming process involves two steps:

1. **Get Connection Details**: Make a request using `client.stream.events()` to receive:
    - WebSocket authentication credentials
    - WebSocket URL/channel info
    - Initial snapshot of current data

2. **Connect and Stream**: Use the provided details to connect via Pusher (or another WebSocket library) and receive real-time `eventID` notifications for changed events

Your API key will have limits on concurrent streams.

## Available Feeds

Subscribe to different feeds using the `feed` query parameter:

| Feed              | Description                                                                 | Required Parameters |
| ----------------- | --------------------------------------------------------------------------- | ------------------- |
| `events:live`     | All events currently in progress (started but not finished)                | None                |
| `events:upcoming` | Upcoming events with available odds for a specific league                  | `leagueID`          |
| `events:byid`     | Updates for a single specific event                                         | `eventID`           |

The number of supported feeds will increase over time. Please reach out if you have a use case which can't be covered by these feeds.

## Quick Start Example

Here's the minimal code to connect to live events:

```python
import os
import pusher

from sports_odds_api import SportsGameOdds

STREAM_FEED = "events:live"  # ex: events:upcoming, events:byid, events:live
API_KEY = os.environ.get("SPORTS_ODDS_API_KEY_HEADER")
client = SportsGameOdds(api_key_param=API_KEY)

# Initialize a data structure where we'll save the event data
EVENTS = {}

# Call this endpoint to get initial data and connection parameters
stream_info = client.stream.events(feed=STREAM_FEED)

# Seed initial data
for event in stream_info.data:
    EVENTS[event.eventID] = event

# Connect to WebSocket server
pusher_client = pusher.Pusher(
    app_id=stream_info.pusherKey,
    **stream_info.pusherOptions,
)

channel = pusher_client.subscribe(stream_info.channel)

def handle_event(changed_events):
    event_ids = ",".join([e["eventID"] for e in changed_events])
    for event in client.events.getEvents(eventIDs=event_ids):
        EVENTS[event.eventID] = event

channel.bind("data", handle_event)
```

### Request & Response types

This library includes Python type hints for all request params and response fields.  
Responses are returned as Pydantic models, giving you:

- Autocomplete and inline docs in your IDE
- Helper methods like `.to_dict()` and `.to_json()`

## Handling errors

When the library is unable to connect to the API,
or if the API returns a non-success status code (i.e., 4xx or 5xx response),
a subclass of `sports_odds_api.APIError` will be raised:

```python
import sports_odds_api
from sports_odds_api import SportsGameOdds

client = SportsGameOdds()

try:
    client.events.get()
except sports_odds_api.APIConnectionError as e:
    print("The server could not be reached")
except sports_odds_api.RateLimitError:
    print("A 429 status code was received; we should back off a bit.")
except sports_odds_api.APIStatusError as e:
    print("Non-200 response:", e.status_code)
```

Error codes are as follows:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with exponential backoff.  
You can configure retries using the `max_retries` option:

```python
client = SportsGameOdds(max_retries=0)  # default is 2

client.with_options(max_retries=5).events.get()
```

### Timeouts

Requests time out after 1 minute by default. Configure this with a `timeout` option:

```python
from sports_odds_api import SportsGameOdds
import httpx

client = SportsGameOdds(timeout=20.0)

client = SportsGameOdds(timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0))

client.with_options(timeout=5.0).events.get()
```

On timeout, an `APITimeoutError` is thrown.

## Auto-pagination

Requests for Events, Teams, and Players are paginated.

```python
from sports_odds_api import SportsGameOdds

client = SportsGameOdds()

all_events = []
for event in client.events.get(limit=30):
    all_events.append(event)
```

Async:

```python
import asyncio
from sports_odds_api import AsyncSportsGameOdds

client = AsyncSportsGameOdds()

async def main():
    all_events = []
    async for event in client.events.get(limit=30):
        all_events.append(event)
    print(all_events)

asyncio.run(main())
```

Convenience methods: `.has_next_page()`, `.next_page_info()`, `.get_next_page()`

## Advanced Usage

### Accessing raw response data (e.g., headers)

```python
from sports_odds_api import SportsGameOdds

client = SportsGameOdds()
response = client.events.with_raw_response.get()
print(response.headers.get("X-My-Header"))

event = response.parse()
print(event.activity)
```

### Logging

Enable logging with:

```sh
export SPORTS_GAME_ODDS_LOG=info
```

Or for more verbose:

```sh
export SPORTS_GAME_ODDS_LOG=debug
```

### Making custom/undocumented requests

```python
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

## Requirements

Python 3.8 or higher.

## Contributing

See [the contributing documentation](./CONTRIBUTING.md).
