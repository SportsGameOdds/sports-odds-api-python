# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
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
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import stats, teams, events, sports, stream, account, leagues, players
    from .resources.stats import StatsResource, AsyncStatsResource
    from .resources.teams import TeamsResource, AsyncTeamsResource
    from .resources.events import EventsResource, AsyncEventsResource
    from .resources.sports import SportsResource, AsyncSportsResource
    from .resources.stream import StreamResource, AsyncStreamResource
    from .resources.account import AccountResource, AsyncAccountResource
    from .resources.leagues import LeaguesResource, AsyncLeaguesResource
    from .resources.players import PlayersResource, AsyncPlayersResource

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

    @cached_property
    def events(self) -> EventsResource:
        from .resources.events import EventsResource

        return EventsResource(self)

    @cached_property
    def teams(self) -> TeamsResource:
        from .resources.teams import TeamsResource

        return TeamsResource(self)

    @cached_property
    def players(self) -> PlayersResource:
        from .resources.players import PlayersResource

        return PlayersResource(self)

    @cached_property
    def leagues(self) -> LeaguesResource:
        from .resources.leagues import LeaguesResource

        return LeaguesResource(self)

    @cached_property
    def sports(self) -> SportsResource:
        from .resources.sports import SportsResource

        return SportsResource(self)

    @cached_property
    def stats(self) -> StatsResource:
        from .resources.stats import StatsResource

        return StatsResource(self)

    @cached_property
    def account(self) -> AccountResource:
        from .resources.account import AccountResource

        return AccountResource(self)

    @cached_property
    def stream(self) -> StreamResource:
        from .resources.stream import StreamResource

        return StreamResource(self)

    @cached_property
    def with_raw_response(self) -> SportsGameOddsWithRawResponse:
        return SportsGameOddsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SportsGameOddsWithStreamedResponse:
        return SportsGameOddsWithStreamedResponse(self)

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

    @cached_property
    def events(self) -> AsyncEventsResource:
        from .resources.events import AsyncEventsResource

        return AsyncEventsResource(self)

    @cached_property
    def teams(self) -> AsyncTeamsResource:
        from .resources.teams import AsyncTeamsResource

        return AsyncTeamsResource(self)

    @cached_property
    def players(self) -> AsyncPlayersResource:
        from .resources.players import AsyncPlayersResource

        return AsyncPlayersResource(self)

    @cached_property
    def leagues(self) -> AsyncLeaguesResource:
        from .resources.leagues import AsyncLeaguesResource

        return AsyncLeaguesResource(self)

    @cached_property
    def sports(self) -> AsyncSportsResource:
        from .resources.sports import AsyncSportsResource

        return AsyncSportsResource(self)

    @cached_property
    def stats(self) -> AsyncStatsResource:
        from .resources.stats import AsyncStatsResource

        return AsyncStatsResource(self)

    @cached_property
    def account(self) -> AsyncAccountResource:
        from .resources.account import AsyncAccountResource

        return AsyncAccountResource(self)

    @cached_property
    def stream(self) -> AsyncStreamResource:
        from .resources.stream import AsyncStreamResource

        return AsyncStreamResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncSportsGameOddsWithRawResponse:
        return AsyncSportsGameOddsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSportsGameOddsWithStreamedResponse:
        return AsyncSportsGameOddsWithStreamedResponse(self)

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
    _client: SportsGameOdds

    def __init__(self, client: SportsGameOdds) -> None:
        self._client = client

    @cached_property
    def events(self) -> events.EventsResourceWithRawResponse:
        from .resources.events import EventsResourceWithRawResponse

        return EventsResourceWithRawResponse(self._client.events)

    @cached_property
    def teams(self) -> teams.TeamsResourceWithRawResponse:
        from .resources.teams import TeamsResourceWithRawResponse

        return TeamsResourceWithRawResponse(self._client.teams)

    @cached_property
    def players(self) -> players.PlayersResourceWithRawResponse:
        from .resources.players import PlayersResourceWithRawResponse

        return PlayersResourceWithRawResponse(self._client.players)

    @cached_property
    def leagues(self) -> leagues.LeaguesResourceWithRawResponse:
        from .resources.leagues import LeaguesResourceWithRawResponse

        return LeaguesResourceWithRawResponse(self._client.leagues)

    @cached_property
    def sports(self) -> sports.SportsResourceWithRawResponse:
        from .resources.sports import SportsResourceWithRawResponse

        return SportsResourceWithRawResponse(self._client.sports)

    @cached_property
    def stats(self) -> stats.StatsResourceWithRawResponse:
        from .resources.stats import StatsResourceWithRawResponse

        return StatsResourceWithRawResponse(self._client.stats)

    @cached_property
    def account(self) -> account.AccountResourceWithRawResponse:
        from .resources.account import AccountResourceWithRawResponse

        return AccountResourceWithRawResponse(self._client.account)

    @cached_property
    def stream(self) -> stream.StreamResourceWithRawResponse:
        from .resources.stream import StreamResourceWithRawResponse

        return StreamResourceWithRawResponse(self._client.stream)


class AsyncSportsGameOddsWithRawResponse:
    _client: AsyncSportsGameOdds

    def __init__(self, client: AsyncSportsGameOdds) -> None:
        self._client = client

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithRawResponse:
        from .resources.events import AsyncEventsResourceWithRawResponse

        return AsyncEventsResourceWithRawResponse(self._client.events)

    @cached_property
    def teams(self) -> teams.AsyncTeamsResourceWithRawResponse:
        from .resources.teams import AsyncTeamsResourceWithRawResponse

        return AsyncTeamsResourceWithRawResponse(self._client.teams)

    @cached_property
    def players(self) -> players.AsyncPlayersResourceWithRawResponse:
        from .resources.players import AsyncPlayersResourceWithRawResponse

        return AsyncPlayersResourceWithRawResponse(self._client.players)

    @cached_property
    def leagues(self) -> leagues.AsyncLeaguesResourceWithRawResponse:
        from .resources.leagues import AsyncLeaguesResourceWithRawResponse

        return AsyncLeaguesResourceWithRawResponse(self._client.leagues)

    @cached_property
    def sports(self) -> sports.AsyncSportsResourceWithRawResponse:
        from .resources.sports import AsyncSportsResourceWithRawResponse

        return AsyncSportsResourceWithRawResponse(self._client.sports)

    @cached_property
    def stats(self) -> stats.AsyncStatsResourceWithRawResponse:
        from .resources.stats import AsyncStatsResourceWithRawResponse

        return AsyncStatsResourceWithRawResponse(self._client.stats)

    @cached_property
    def account(self) -> account.AsyncAccountResourceWithRawResponse:
        from .resources.account import AsyncAccountResourceWithRawResponse

        return AsyncAccountResourceWithRawResponse(self._client.account)

    @cached_property
    def stream(self) -> stream.AsyncStreamResourceWithRawResponse:
        from .resources.stream import AsyncStreamResourceWithRawResponse

        return AsyncStreamResourceWithRawResponse(self._client.stream)


class SportsGameOddsWithStreamedResponse:
    _client: SportsGameOdds

    def __init__(self, client: SportsGameOdds) -> None:
        self._client = client

    @cached_property
    def events(self) -> events.EventsResourceWithStreamingResponse:
        from .resources.events import EventsResourceWithStreamingResponse

        return EventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def teams(self) -> teams.TeamsResourceWithStreamingResponse:
        from .resources.teams import TeamsResourceWithStreamingResponse

        return TeamsResourceWithStreamingResponse(self._client.teams)

    @cached_property
    def players(self) -> players.PlayersResourceWithStreamingResponse:
        from .resources.players import PlayersResourceWithStreamingResponse

        return PlayersResourceWithStreamingResponse(self._client.players)

    @cached_property
    def leagues(self) -> leagues.LeaguesResourceWithStreamingResponse:
        from .resources.leagues import LeaguesResourceWithStreamingResponse

        return LeaguesResourceWithStreamingResponse(self._client.leagues)

    @cached_property
    def sports(self) -> sports.SportsResourceWithStreamingResponse:
        from .resources.sports import SportsResourceWithStreamingResponse

        return SportsResourceWithStreamingResponse(self._client.sports)

    @cached_property
    def stats(self) -> stats.StatsResourceWithStreamingResponse:
        from .resources.stats import StatsResourceWithStreamingResponse

        return StatsResourceWithStreamingResponse(self._client.stats)

    @cached_property
    def account(self) -> account.AccountResourceWithStreamingResponse:
        from .resources.account import AccountResourceWithStreamingResponse

        return AccountResourceWithStreamingResponse(self._client.account)

    @cached_property
    def stream(self) -> stream.StreamResourceWithStreamingResponse:
        from .resources.stream import StreamResourceWithStreamingResponse

        return StreamResourceWithStreamingResponse(self._client.stream)


class AsyncSportsGameOddsWithStreamedResponse:
    _client: AsyncSportsGameOdds

    def __init__(self, client: AsyncSportsGameOdds) -> None:
        self._client = client

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithStreamingResponse:
        from .resources.events import AsyncEventsResourceWithStreamingResponse

        return AsyncEventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def teams(self) -> teams.AsyncTeamsResourceWithStreamingResponse:
        from .resources.teams import AsyncTeamsResourceWithStreamingResponse

        return AsyncTeamsResourceWithStreamingResponse(self._client.teams)

    @cached_property
    def players(self) -> players.AsyncPlayersResourceWithStreamingResponse:
        from .resources.players import AsyncPlayersResourceWithStreamingResponse

        return AsyncPlayersResourceWithStreamingResponse(self._client.players)

    @cached_property
    def leagues(self) -> leagues.AsyncLeaguesResourceWithStreamingResponse:
        from .resources.leagues import AsyncLeaguesResourceWithStreamingResponse

        return AsyncLeaguesResourceWithStreamingResponse(self._client.leagues)

    @cached_property
    def sports(self) -> sports.AsyncSportsResourceWithStreamingResponse:
        from .resources.sports import AsyncSportsResourceWithStreamingResponse

        return AsyncSportsResourceWithStreamingResponse(self._client.sports)

    @cached_property
    def stats(self) -> stats.AsyncStatsResourceWithStreamingResponse:
        from .resources.stats import AsyncStatsResourceWithStreamingResponse

        return AsyncStatsResourceWithStreamingResponse(self._client.stats)

    @cached_property
    def account(self) -> account.AsyncAccountResourceWithStreamingResponse:
        from .resources.account import AsyncAccountResourceWithStreamingResponse

        return AsyncAccountResourceWithStreamingResponse(self._client.account)

    @cached_property
    def stream(self) -> stream.AsyncStreamResourceWithStreamingResponse:
        from .resources.stream import AsyncStreamResourceWithStreamingResponse

        return AsyncStreamResourceWithStreamingResponse(self._client.stream)


Client = SportsGameOdds

AsyncClient = AsyncSportsGameOdds
