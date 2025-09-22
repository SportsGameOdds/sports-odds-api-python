# Events

Types:

```python
from sports_odds_api.types import Event
```

Methods:

- <code title="get /events/">client.events.<a href="./src/sports_odds_api/resources/events.py">get</a>(\*\*<a href="src/sports_odds_api/types/event_get_params.py">params</a>) -> <a href="./src/sports_odds_api/types/event.py">SyncNextCursorPage[Event]</a></code>

# Teams

Types:

```python
from sports_odds_api.types import Team
```

Methods:

- <code title="get /teams/">client.teams.<a href="./src/sports_odds_api/resources/teams.py">get</a>(\*\*<a href="src/sports_odds_api/types/team_get_params.py">params</a>) -> <a href="./src/sports_odds_api/types/team.py">SyncNextCursorPage[Team]</a></code>

# Players

Types:

```python
from sports_odds_api.types import Player
```

Methods:

- <code title="get /players/">client.players.<a href="./src/sports_odds_api/resources/players.py">get</a>(\*\*<a href="src/sports_odds_api/types/player_get_params.py">params</a>) -> <a href="./src/sports_odds_api/types/player.py">SyncNextCursorPage[Player]</a></code>

# Leagues

Types:

```python
from sports_odds_api.types import League, LeagueGetResponse
```

Methods:

- <code title="get /leagues/">client.leagues.<a href="./src/sports_odds_api/resources/leagues.py">get</a>(\*\*<a href="src/sports_odds_api/types/league_get_params.py">params</a>) -> <a href="./src/sports_odds_api/types/league_get_response.py">Optional[LeagueGetResponse]</a></code>

# Sports

Types:

```python
from sports_odds_api.types import Sport, SportGetResponse
```

Methods:

- <code title="get /sports/">client.sports.<a href="./src/sports_odds_api/resources/sports.py">get</a>() -> <a href="./src/sports_odds_api/types/sport_get_response.py">Optional[SportGetResponse]</a></code>

# Stats

Types:

```python
from sports_odds_api.types import Stat, StatGetResponse
```

Methods:

- <code title="get /stats/">client.stats.<a href="./src/sports_odds_api/resources/stats.py">get</a>(\*\*<a href="src/sports_odds_api/types/stat_get_params.py">params</a>) -> <a href="./src/sports_odds_api/types/stat_get_response.py">Optional[StatGetResponse]</a></code>

# Account

Types:

```python
from sports_odds_api.types import AccountUsage, RateLimitInterval
```

Methods:

- <code title="get /account/usage">client.account.<a href="./src/sports_odds_api/resources/account.py">get_usage</a>() -> <a href="./src/sports_odds_api/types/account_usage.py">Optional[AccountUsage]</a></code>

# Stream

Types:

```python
from sports_odds_api.types import StreamEventsResponse
```

Methods:

- <code title="get /stream/events">client.stream.<a href="./src/sports_odds_api/resources/stream.py">events</a>(\*\*<a href="src/sports_odds_api/types/stream_events_params.py">params</a>) -> <a href="./src/sports_odds_api/types/stream_events_response.py">StreamEventsResponse</a></code>
