# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import stats, teams, events, sports, stream, account, leagues, players
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "SportsGameOdds",
    "AsyncSportsGameOdds",
    "Client",
    "AsyncClient",
]


class SportsGameOdds(SyncAPIClient):
    events: events.EventsResource
    teams: teams.TeamsResource
    players: players.PlayersResource
    leagues: leagues.LeaguesResource
    sports: sports.SportsResource
    stats: stats.StatsResource
    account: account.AccountResource
    stream: stream.StreamResource
    with_raw_response: SportsGameOddsWithRawResponse
    with_streaming_response: SportsGameOddsWithStreamedResponse

    # client options
    api_key_header: str | None
    api_key_param: str | None

    def __init__(
        self,
        *,
        api_key_header: str | None = None,
        api_key_param: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous SportsGameOdds client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key_header` from `SPORTS_ODDS_API_KEY_HEADER`
        - `api_key_param` from `SPORTS_ODDS_API_KEY_HEADER`
        """
        if api_key_header is None:
            api_key_header = os.environ.get("SPORTS_ODDS_API_KEY_HEADER")
        self.api_key_header = api_key_header

        if api_key_param is None:
            api_key_param = os.environ.get("SPORTS_ODDS_API_KEY_HEADER")
        self.api_key_param = api_key_param

        if base_url is None:
            base_url = os.environ.get("SPORTS_GAME_ODDS_BASE_URL")
        if base_url is None:
            base_url = f"https://api.sportsgameodds.com/v2"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.events = events.EventsResource(self)
        self.teams = teams.TeamsResource(self)
        self.players = players.PlayersResource(self)
        self.leagues = leagues.LeaguesResource(self)
        self.sports = sports.SportsResource(self)
        self.stats = stats.StatsResource(self)
        self.account = account.AccountResource(self)
        self.stream = stream.StreamResource(self)
        self.with_raw_response = SportsGameOddsWithRawResponse(self)
        self.with_streaming_response = SportsGameOddsWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key_header = self.api_key_header
        if api_key_header is None:
            return {}
        return {"x-api-key": api_key_header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @property
    @override
    def default_query(self) -> dict[str, object]:
        return {
            **super().default_query,
            "apiKey": self.api_key_param if self.api_key_param is not None else Omit(),
            **self._custom_query,
        }

    def copy(
        self,
        *,
        api_key_header: str | None = None,
        api_key_param: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key_header=api_key_header or self.api_key_header,
            api_key_param=api_key_param or self.api_key_param,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncSportsGameOdds(AsyncAPIClient):
    events: events.AsyncEventsResource
    teams: teams.AsyncTeamsResource
    players: players.AsyncPlayersResource
    leagues: leagues.AsyncLeaguesResource
    sports: sports.AsyncSportsResource
    stats: stats.AsyncStatsResource
    account: account.AsyncAccountResource
    stream: stream.AsyncStreamResource
    with_raw_response: AsyncSportsGameOddsWithRawResponse
    with_streaming_response: AsyncSportsGameOddsWithStreamedResponse

    # client options
    api_key_header: str | None
    api_key_param: str | None

    def __init__(
        self,
        *,
        api_key_header: str | None = None,
        api_key_param: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncSportsGameOdds client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key_header` from `SPORTS_ODDS_API_KEY_HEADER`
        - `api_key_param` from `SPORTS_ODDS_API_KEY_HEADER`
        """
        if api_key_header is None:
            api_key_header = os.environ.get("SPORTS_ODDS_API_KEY_HEADER")
        self.api_key_header = api_key_header

        if api_key_param is None:
            api_key_param = os.environ.get("SPORTS_ODDS_API_KEY_HEADER")
        self.api_key_param = api_key_param

        if base_url is None:
            base_url = os.environ.get("SPORTS_GAME_ODDS_BASE_URL")
        if base_url is None:
            base_url = f"https://api.sportsgameodds.com/v2"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.events = events.AsyncEventsResource(self)
        self.teams = teams.AsyncTeamsResource(self)
        self.players = players.AsyncPlayersResource(self)
        self.leagues = leagues.AsyncLeaguesResource(self)
        self.sports = sports.AsyncSportsResource(self)
        self.stats = stats.AsyncStatsResource(self)
        self.account = account.AsyncAccountResource(self)
        self.stream = stream.AsyncStreamResource(self)
        self.with_raw_response = AsyncSportsGameOddsWithRawResponse(self)
        self.with_streaming_response = AsyncSportsGameOddsWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key_header = self.api_key_header
        if api_key_header is None:
            return {}
        return {"x-api-key": api_key_header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @property
    @override
    def default_query(self) -> dict[str, object]:
        return {
            **super().default_query,
            "apiKey": self.api_key_param if self.api_key_param is not None else Omit(),
            **self._custom_query,
        }

    def copy(
        self,
        *,
        api_key_header: str | None = None,
        api_key_param: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key_header=api_key_header or self.api_key_header,
            api_key_param=api_key_param or self.api_key_param,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class SportsGameOddsWithRawResponse:
    def __init__(self, client: SportsGameOdds) -> None:
        self.events = events.EventsResourceWithRawResponse(client.events)
        self.teams = teams.TeamsResourceWithRawResponse(client.teams)
        self.players = players.PlayersResourceWithRawResponse(client.players)
        self.leagues = leagues.LeaguesResourceWithRawResponse(client.leagues)
        self.sports = sports.SportsResourceWithRawResponse(client.sports)
        self.stats = stats.StatsResourceWithRawResponse(client.stats)
        self.account = account.AccountResourceWithRawResponse(client.account)
        self.stream = stream.StreamResourceWithRawResponse(client.stream)


class AsyncSportsGameOddsWithRawResponse:
    def __init__(self, client: AsyncSportsGameOdds) -> None:
        self.events = events.AsyncEventsResourceWithRawResponse(client.events)
        self.teams = teams.AsyncTeamsResourceWithRawResponse(client.teams)
        self.players = players.AsyncPlayersResourceWithRawResponse(client.players)
        self.leagues = leagues.AsyncLeaguesResourceWithRawResponse(client.leagues)
        self.sports = sports.AsyncSportsResourceWithRawResponse(client.sports)
        self.stats = stats.AsyncStatsResourceWithRawResponse(client.stats)
        self.account = account.AsyncAccountResourceWithRawResponse(client.account)
        self.stream = stream.AsyncStreamResourceWithRawResponse(client.stream)


class SportsGameOddsWithStreamedResponse:
    def __init__(self, client: SportsGameOdds) -> None:
        self.events = events.EventsResourceWithStreamingResponse(client.events)
        self.teams = teams.TeamsResourceWithStreamingResponse(client.teams)
        self.players = players.PlayersResourceWithStreamingResponse(client.players)
        self.leagues = leagues.LeaguesResourceWithStreamingResponse(client.leagues)
        self.sports = sports.SportsResourceWithStreamingResponse(client.sports)
        self.stats = stats.StatsResourceWithStreamingResponse(client.stats)
        self.account = account.AccountResourceWithStreamingResponse(client.account)
        self.stream = stream.StreamResourceWithStreamingResponse(client.stream)


class AsyncSportsGameOddsWithStreamedResponse:
    def __init__(self, client: AsyncSportsGameOdds) -> None:
        self.events = events.AsyncEventsResourceWithStreamingResponse(client.events)
        self.teams = teams.AsyncTeamsResourceWithStreamingResponse(client.teams)
        self.players = players.AsyncPlayersResourceWithStreamingResponse(client.players)
        self.leagues = leagues.AsyncLeaguesResourceWithStreamingResponse(client.leagues)
        self.sports = sports.AsyncSportsResourceWithStreamingResponse(client.sports)
        self.stats = stats.AsyncStatsResourceWithStreamingResponse(client.stats)
        self.account = account.AsyncAccountResourceWithStreamingResponse(client.account)
        self.stream = stream.AsyncStreamResourceWithStreamingResponse(client.stream)


Client = SportsGameOdds

AsyncClient = AsyncSportsGameOdds
