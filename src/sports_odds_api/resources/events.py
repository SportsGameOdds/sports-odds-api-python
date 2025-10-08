# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import event_get_params
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
from ..types.event import Event
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        bookmaker_id: str | Omit = omit,
        cancelled: bool | Omit = omit,
        cursor: str | Omit = omit,
        ended: bool | Omit = omit,
        event_id: str | Omit = omit,
        event_ids: str | Omit = omit,
        finalized: bool | Omit = omit,
        include_alt_lines: bool | Omit = omit,
        include_opposing_odds: bool | Omit = omit,
        league_id: str | Omit = omit,
        limit: float | Omit = omit,
        live: bool | Omit = omit,
        odd_id: str | Omit = omit,
        odds_available: bool | Omit = omit,
        odds_present: bool | Omit = omit,
        player_id: str | Omit = omit,
        sport_id: str | Omit = omit,
        started: bool | Omit = omit,
        starts_after: Union[str, datetime] | Omit = omit,
        starts_before: Union[str, datetime] | Omit = omit,
        team_id: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncNextCursorPage[Event]:
        """
        Get a list of Events

        Args:
          bookmaker_id: A bookmakerID or comma-separated list of bookmakerIDs to include odds for

          cancelled: Only include cancelled Events (true), only non-cancelled Events (false) or all
              Events (omit)

          cursor: The cursor for the request. Used to get the next group of Events. This should be
              the nextCursor from the prior response.

          ended: Only include Events which have have ended (true), only Events which have not
              ended (false) or all Events (omit)

          event_id: An eventID to get Event data for

          event_ids: A comma separated list of eventIDs to get Event data for

          finalized: Only include finalized Events (true), exclude unfinalized Events (false) or all
              Events (omit)

          include_alt_lines: Whether to include alternate lines in the odds byBookmaker data

          include_opposing_odds: Whether to include opposing odds for each included oddID

          league_id: A leagueID or comma-separated list of leagueIDs to get Events for

          limit: The maximum number of Events to return

          live: Only include live Events (true), only non-live Events (false) or all Events
              (omit)

          odd_id: An oddID or comma-separated list of oddIDs to include odds for

          odds_available: Whether you want only Events which do (true) or do not (false) have odds markets
              which are currently available (open for wagering)

          odds_present: Whether you want only Events which do (true) or do not (false) have any
              associated odds markets regardless of whether those odds markets are currently
              available (open for wagering)

          player_id: A playerID or comma-separated list of playerIDs to include Events (and
              associated odds) for

          sport_id: A sportID or comma-separated list of sportIDs to get Events for

          started: Only include Events which have have previously started (true), only Events which
              have not previously started (false) or all Events (omit)

          starts_after: Get Events that start after this date

          starts_before: Get Events that start before this date

          team_id: A teamID or comma-separated list of teamIDs to include Events for

          type: Only include Events of the specified type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/events/",
            page=SyncNextCursorPage[Event],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bookmaker_id": bookmaker_id,
                        "cancelled": cancelled,
                        "cursor": cursor,
                        "ended": ended,
                        "event_id": event_id,
                        "event_ids": event_ids,
                        "finalized": finalized,
                        "include_alt_lines": include_alt_lines,
                        "include_opposing_odds": include_opposing_odds,
                        "league_id": league_id,
                        "limit": limit,
                        "live": live,
                        "odd_id": odd_id,
                        "odds_available": odds_available,
                        "odds_present": odds_present,
                        "player_id": player_id,
                        "sport_id": sport_id,
                        "started": started,
                        "starts_after": starts_after,
                        "starts_before": starts_before,
                        "team_id": team_id,
                        "type": type,
                    },
                    event_get_params.EventGetParams,
                ),
            ),
            model=Event,
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        bookmaker_id: str | Omit = omit,
        cancelled: bool | Omit = omit,
        cursor: str | Omit = omit,
        ended: bool | Omit = omit,
        event_id: str | Omit = omit,
        event_ids: str | Omit = omit,
        finalized: bool | Omit = omit,
        include_alt_lines: bool | Omit = omit,
        include_opposing_odds: bool | Omit = omit,
        league_id: str | Omit = omit,
        limit: float | Omit = omit,
        live: bool | Omit = omit,
        odd_id: str | Omit = omit,
        odds_available: bool | Omit = omit,
        odds_present: bool | Omit = omit,
        player_id: str | Omit = omit,
        sport_id: str | Omit = omit,
        started: bool | Omit = omit,
        starts_after: Union[str, datetime] | Omit = omit,
        starts_before: Union[str, datetime] | Omit = omit,
        team_id: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Event, AsyncNextCursorPage[Event]]:
        """
        Get a list of Events

        Args:
          bookmaker_id: A bookmakerID or comma-separated list of bookmakerIDs to include odds for

          cancelled: Only include cancelled Events (true), only non-cancelled Events (false) or all
              Events (omit)

          cursor: The cursor for the request. Used to get the next group of Events. This should be
              the nextCursor from the prior response.

          ended: Only include Events which have have ended (true), only Events which have not
              ended (false) or all Events (omit)

          event_id: An eventID to get Event data for

          event_ids: A comma separated list of eventIDs to get Event data for

          finalized: Only include finalized Events (true), exclude unfinalized Events (false) or all
              Events (omit)

          include_alt_lines: Whether to include alternate lines in the odds byBookmaker data

          include_opposing_odds: Whether to include opposing odds for each included oddID

          league_id: A leagueID or comma-separated list of leagueIDs to get Events for

          limit: The maximum number of Events to return

          live: Only include live Events (true), only non-live Events (false) or all Events
              (omit)

          odd_id: An oddID or comma-separated list of oddIDs to include odds for

          odds_available: Whether you want only Events which do (true) or do not (false) have odds markets
              which are currently available (open for wagering)

          odds_present: Whether you want only Events which do (true) or do not (false) have any
              associated odds markets regardless of whether those odds markets are currently
              available (open for wagering)

          player_id: A playerID or comma-separated list of playerIDs to include Events (and
              associated odds) for

          sport_id: A sportID or comma-separated list of sportIDs to get Events for

          started: Only include Events which have have previously started (true), only Events which
              have not previously started (false) or all Events (omit)

          starts_after: Get Events that start after this date

          starts_before: Get Events that start before this date

          team_id: A teamID or comma-separated list of teamIDs to include Events for

          type: Only include Events of the specified type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/events/",
            page=AsyncNextCursorPage[Event],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bookmaker_id": bookmaker_id,
                        "cancelled": cancelled,
                        "cursor": cursor,
                        "ended": ended,
                        "event_id": event_id,
                        "event_ids": event_ids,
                        "finalized": finalized,
                        "include_alt_lines": include_alt_lines,
                        "include_opposing_odds": include_opposing_odds,
                        "league_id": league_id,
                        "limit": limit,
                        "live": live,
                        "odd_id": odd_id,
                        "odds_available": odds_available,
                        "odds_present": odds_present,
                        "player_id": player_id,
                        "sport_id": sport_id,
                        "started": started,
                        "starts_after": starts_after,
                        "starts_before": starts_before,
                        "team_id": team_id,
                        "type": type,
                    },
                    event_get_params.EventGetParams,
                ),
            ),
            model=Event,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.get = to_raw_response_wrapper(
            events.get,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.get = async_to_raw_response_wrapper(
            events.get,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.get = to_streamed_response_wrapper(
            events.get,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.get = async_to_streamed_response_wrapper(
            events.get,
        )
