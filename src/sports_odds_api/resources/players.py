# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import player_get_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncNextCursorPage, AsyncNextCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.player import Player

__all__ = ["PlayersResource", "AsyncPlayersResource"]


class PlayersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlayersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#accessing-raw-response-data-eg-headers
        """
        return PlayersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlayersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#with_streaming_response
        """
        return PlayersResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        cursor: str | Omit = omit,
        event_id: str | Omit = omit,
        limit: float | Omit = omit,
        player_id: str | Omit = omit,
        team_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncNextCursorPage[Player]:
        """
        Get a list of Players for a specific Team or Event

        Args:
          cursor: The cursor for the request. Used to get the next group of Players. This should
              be the nextCursor from the prior response.

          event_id: EventID to get Players data for

          limit: The maximum number of Players to return

          player_id: PlayerID to get data for

          team_id: TeamID to get Players data for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/players/",
            page=SyncNextCursorPage[Player],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "event_id": event_id,
                        "limit": limit,
                        "player_id": player_id,
                        "team_id": team_id,
                    },
                    player_get_params.PlayerGetParams,
                ),
            ),
            model=Player,
        )


class AsyncPlayersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlayersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlayersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlayersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#with_streaming_response
        """
        return AsyncPlayersResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        cursor: str | Omit = omit,
        event_id: str | Omit = omit,
        limit: float | Omit = omit,
        player_id: str | Omit = omit,
        team_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Player, AsyncNextCursorPage[Player]]:
        """
        Get a list of Players for a specific Team or Event

        Args:
          cursor: The cursor for the request. Used to get the next group of Players. This should
              be the nextCursor from the prior response.

          event_id: EventID to get Players data for

          limit: The maximum number of Players to return

          player_id: PlayerID to get data for

          team_id: TeamID to get Players data for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/players/",
            page=AsyncNextCursorPage[Player],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "event_id": event_id,
                        "limit": limit,
                        "player_id": player_id,
                        "team_id": team_id,
                    },
                    player_get_params.PlayerGetParams,
                ),
            ),
            model=Player,
        )


class PlayersResourceWithRawResponse:
    def __init__(self, players: PlayersResource) -> None:
        self._players = players

        self.get = to_raw_response_wrapper(
            players.get,
        )


class AsyncPlayersResourceWithRawResponse:
    def __init__(self, players: AsyncPlayersResource) -> None:
        self._players = players

        self.get = async_to_raw_response_wrapper(
            players.get,
        )


class PlayersResourceWithStreamingResponse:
    def __init__(self, players: PlayersResource) -> None:
        self._players = players

        self.get = to_streamed_response_wrapper(
            players.get,
        )


class AsyncPlayersResourceWithStreamingResponse:
    def __init__(self, players: AsyncPlayersResource) -> None:
        self._players = players

        self.get = async_to_streamed_response_wrapper(
            players.get,
        )
