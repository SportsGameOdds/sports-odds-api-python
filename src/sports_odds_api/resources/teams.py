# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import team_get_params
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
from ..types.team import Team
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["TeamsResource", "AsyncTeamsResource"]


class TeamsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#accessing-raw-response-data-eg-headers
        """
        return TeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#with_streaming_response
        """
        return TeamsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        cursor: str | Omit = omit,
        league_id: str | Omit = omit,
        limit: float | Omit = omit,
        sport_id: str | Omit = omit,
        team_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncNextCursorPage[Team]:
        """Get a list of Teams by ID or league

        Args:
          cursor: The cursor for the request.

        Used to get the next group of Teams. This should be
              the nextCursor from the prior response.

          league_id: A single leagueID or comma-separated list of leagueIDs to get Teams for

          limit: The maximum number of Teams to return

          sport_id: A single sportID or comma-separated list of sportIDs to get Teams for

          team_id: A single teamID or comma-separated list of teamIDs to get data for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/teams/",
            page=SyncNextCursorPage[Team],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "league_id": league_id,
                        "limit": limit,
                        "sport_id": sport_id,
                        "team_id": team_id,
                    },
                    team_get_params.TeamGetParams,
                ),
            ),
            model=Team,
        )


class AsyncTeamsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#with_streaming_response
        """
        return AsyncTeamsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        cursor: str | Omit = omit,
        league_id: str | Omit = omit,
        limit: float | Omit = omit,
        sport_id: str | Omit = omit,
        team_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Team, AsyncNextCursorPage[Team]]:
        """Get a list of Teams by ID or league

        Args:
          cursor: The cursor for the request.

        Used to get the next group of Teams. This should be
              the nextCursor from the prior response.

          league_id: A single leagueID or comma-separated list of leagueIDs to get Teams for

          limit: The maximum number of Teams to return

          sport_id: A single sportID or comma-separated list of sportIDs to get Teams for

          team_id: A single teamID or comma-separated list of teamIDs to get data for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/teams/",
            page=AsyncNextCursorPage[Team],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "league_id": league_id,
                        "limit": limit,
                        "sport_id": sport_id,
                        "team_id": team_id,
                    },
                    team_get_params.TeamGetParams,
                ),
            ),
            model=Team,
        )


class TeamsResourceWithRawResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

        self.get = to_raw_response_wrapper(
            teams.get,
        )


class AsyncTeamsResourceWithRawResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

        self.get = async_to_raw_response_wrapper(
            teams.get,
        )


class TeamsResourceWithStreamingResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

        self.get = to_streamed_response_wrapper(
            teams.get,
        )


class AsyncTeamsResourceWithStreamingResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

        self.get = async_to_streamed_response_wrapper(
            teams.get,
        )
