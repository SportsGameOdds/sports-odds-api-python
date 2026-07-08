# Sports Odds API - Live Sports Data & Sportsbook Betting Odds - Powered by SportsGameOdds Python API Library

Get live betting odds, spreads, and totals for NFL, NBA, MLB, and 50 additional sports and leagues. Production-ready Python SDK with WebSocket support, 99.9% uptime, and sub-minute updates during live games. Perfect for developers building sportsbook platforms, odds comparison tools, positive EV models, and anything else that requires fast, accurate sports data.

[![PyPI version](https://img.shields.io/pypi/v/sports-odds-api.svg?label=pypi%20(stable))](https://pypi.org/project/sports-odds-api/)

This library provides convenient access to the Sports Game Odds REST API from Python 3.8+ applications.

The REST API documentation can be found on [sportsgameodds.com](https://sportsgameodds.com/docs/). The full API of this library can be found in [api.md](api.md).

## MCP Server

Use the Sports Game Odds MCP Server to enable AI assistants to interact with this API, allowing them to explore endpoints, make test requests, and use documentation to help integrate this SDK into your application.

[![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=sports-odds-api-mcp&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsInNwb3J0cy1vZGRzLWFwaS1tY3AiXSwiZW52Ijp7IlNQT1JUU19PRERTX0FQSV9LRVlfSEVBREVSIjoiTXkgQVBJIEtleSBQYXJhbSJ9fQ)
[![Install in VS Code](https://img.shields.io/badge/_-Add_to_VS_Code-blue?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PHBhdGggZmlsbD0iI0VFRSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMzAuMjM1IDM5Ljg4NGEyLjQ5MSAyLjQ5MSAwIDAgMS0xLjc4MS0uNzNMMTIuNyAyNC43OGwtMy40NiAyLjYyNC0zLjQwNiAyLjU4MmExLjY2NSAxLjY2NSAwIDAgMS0xLjA4Mi4zMzggMS42NjQgMS42NjQgMCAwIDEtMS4wNDYtLjQzMWwtMi4yLTJhMS42NjYgMS42NjYgMCAwIDEgMC0yLjQ2M0w3LjQ1OCAyMCA0LjY3IDE3LjQ1MyAxLjUwNyAxNC41N2ExLjY2NSAxLjY2NSAwIDAgMSAwLTIuNDYzbDIuMi0yYTEuNjY1IDEuNjY1IDAgMCAxIDIuMTMtLjA5N2w2Ljg2MyA1LjIwOUwyOC40NTIuODQ0YTIuNDg4IDIuNDg4IDAgMCAxIDEuODQxLS43MjljLjM1MS4wMDkuNjk5LjA5MSAxLjAxOS4yNDVsOC4yMzYgMy45NjFhMi41IDIuNSAwIDAgMSAxLjQxNSAyLjI1M3YuMDk5LS4wNDVWMzMuMzd2LS4wNDUuMDk1YTIuNTAxIDIuNTAxIDAgMCAxLTEuNDE2IDIuMjU3bC04LjIzNSAzLjk2MWEyLjQ5MiAyLjQ5MiAwIDAgMS0xLjA3Ny4yNDZabS43MTYtMjguOTQ3LTExLjk0OCA5LjA2MiAxMS45NTIgOS4wNjUtLjAwNC0xOC4xMjdaIi8+PC9zdmc+)](https://vscode.stainless.com/mcp/%7B%22name%22%3A%22sports-odds-api-mcp%22%2C%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22sports-odds-api-mcp%22%5D%2C%22env%22%3A%7B%22SPORTS_ODDS_API_KEY_HEADER%22%3A%22My%20API%20Key%20Param%22%7D%7D)

> Note: You may need to set environment variables in your MCP client.

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

Python 3.9 or higher.

## Contributing

See [the contributing documentation](./CONTRIBUTING.md).
