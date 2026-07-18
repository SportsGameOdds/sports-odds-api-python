# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import market_get_params
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
from ..types.market import Market

__all__ = ["MarketsResource", "AsyncMarketsResource"]


class MarketsResource(SyncAPIResource):
    """Get metadata on supported Markets"""

    @cached_property
    def with_raw_response(self) -> MarketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#accessing-raw-response-data-eg-headers
        """
        return MarketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#with_streaming_response
        """
        return MarketsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        bet_type_id: str | Omit = omit,
        bookmaker_id: str | Omit = omit,
        cursor: str | Omit = omit,
        is_main_market: bool | Omit = omit,
        is_prop: bool | Omit = omit,
        is_sub_period: bool | Omit = omit,
        is_supported: bool | Omit = omit,
        league_id: str | Omit = omit,
        limit: float | Omit = omit,
        odd_id: str | Omit = omit,
        period_id: str | Omit = omit,
        prop_type: str | Omit = omit,
        side_id: str | Omit = omit,
        sport_id: str | Omit = omit,
        stat_entity_id: str | Omit = omit,
        stat_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncNextCursorPage[Market]:
        """
        Get a list of Markets

        Args:
          bet_type_id: A single betTypeID or comma-separated list of betTypeIDs to filter Markets by

          bookmaker_id: A single bookmakerID or comma-separated list of bookmakerIDs to filter Markets
              by

          cursor: The cursor for pagination. Use nextCursor from prior response.

          is_main_market: Filter to only include main markets (main period moneyline, spread, and
              over/under)

          is_prop: Filter by whether it is any type of prop bet market

          is_sub_period: Filter by whether it tracks a sub/non-main period

          is_supported: Filter whether this market is fully supported by at least 1 bookmaker in at
              least 1 league. Defaults to true if not specified.

          league_id: A single leagueID or comma-separated list of leagueIDs to filter Markets by

          limit: The maximum number of Markets to return (default: 100, max: 10000)

          odd_id: A single oddID or comma-separated list of oddIDs. Used to specify specific
              Markets to return.

          period_id: A single periodID or comma-separated list of periodIDs to filter Markets by

          prop_type: Filter by prop type (game_prop, team_prop, player_prop, other_prop)

          side_id: A single sideID or comma-separated list of sideIDs to filter Markets by

          sport_id: A single sportID or comma-separated list of sportIDs to filter Markets by

          stat_entity_id: A single statEntityID or comma-separated list of statEntityIDs to filter Markets
              by

          stat_id: A single statID or comma-separated list of statIDs to filter Markets by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/markets/",
            page=SyncNextCursorPage[Market],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bet_type_id": bet_type_id,
                        "bookmaker_id": bookmaker_id,
                        "cursor": cursor,
                        "is_main_market": is_main_market,
                        "is_prop": is_prop,
                        "is_sub_period": is_sub_period,
                        "is_supported": is_supported,
                        "league_id": league_id,
                        "limit": limit,
                        "odd_id": odd_id,
                        "period_id": period_id,
                        "prop_type": prop_type,
                        "side_id": side_id,
                        "sport_id": sport_id,
                        "stat_entity_id": stat_entity_id,
                        "stat_id": stat_id,
                    },
                    market_get_params.MarketGetParams,
                ),
            ),
            model=Market,
        )


class AsyncMarketsResource(AsyncAPIResource):
    """Get metadata on supported Markets"""

    @cached_property
    def with_raw_response(self) -> AsyncMarketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#with_streaming_response
        """
        return AsyncMarketsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        bet_type_id: str | Omit = omit,
        bookmaker_id: str | Omit = omit,
        cursor: str | Omit = omit,
        is_main_market: bool | Omit = omit,
        is_prop: bool | Omit = omit,
        is_sub_period: bool | Omit = omit,
        is_supported: bool | Omit = omit,
        league_id: str | Omit = omit,
        limit: float | Omit = omit,
        odd_id: str | Omit = omit,
        period_id: str | Omit = omit,
        prop_type: str | Omit = omit,
        side_id: str | Omit = omit,
        sport_id: str | Omit = omit,
        stat_entity_id: str | Omit = omit,
        stat_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Market, AsyncNextCursorPage[Market]]:
        """
        Get a list of Markets

        Args:
          bet_type_id: A single betTypeID or comma-separated list of betTypeIDs to filter Markets by

          bookmaker_id: A single bookmakerID or comma-separated list of bookmakerIDs to filter Markets
              by

          cursor: The cursor for pagination. Use nextCursor from prior response.

          is_main_market: Filter to only include main markets (main period moneyline, spread, and
              over/under)

          is_prop: Filter by whether it is any type of prop bet market

          is_sub_period: Filter by whether it tracks a sub/non-main period

          is_supported: Filter whether this market is fully supported by at least 1 bookmaker in at
              least 1 league. Defaults to true if not specified.

          league_id: A single leagueID or comma-separated list of leagueIDs to filter Markets by

          limit: The maximum number of Markets to return (default: 100, max: 10000)

          odd_id: A single oddID or comma-separated list of oddIDs. Used to specify specific
              Markets to return.

          period_id: A single periodID or comma-separated list of periodIDs to filter Markets by

          prop_type: Filter by prop type (game_prop, team_prop, player_prop, other_prop)

          side_id: A single sideID or comma-separated list of sideIDs to filter Markets by

          sport_id: A single sportID or comma-separated list of sportIDs to filter Markets by

          stat_entity_id: A single statEntityID or comma-separated list of statEntityIDs to filter Markets
              by

          stat_id: A single statID or comma-separated list of statIDs to filter Markets by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/markets/",
            page=AsyncNextCursorPage[Market],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bet_type_id": bet_type_id,
                        "bookmaker_id": bookmaker_id,
                        "cursor": cursor,
                        "is_main_market": is_main_market,
                        "is_prop": is_prop,
                        "is_sub_period": is_sub_period,
                        "is_supported": is_supported,
                        "league_id": league_id,
                        "limit": limit,
                        "odd_id": odd_id,
                        "period_id": period_id,
                        "prop_type": prop_type,
                        "side_id": side_id,
                        "sport_id": sport_id,
                        "stat_entity_id": stat_entity_id,
                        "stat_id": stat_id,
                    },
                    market_get_params.MarketGetParams,
                ),
            ),
            model=Market,
        )


class MarketsResourceWithRawResponse:
    def __init__(self, markets: MarketsResource) -> None:
        self._markets = markets

        self.get = to_raw_response_wrapper(
            markets.get,
        )


class AsyncMarketsResourceWithRawResponse:
    def __init__(self, markets: AsyncMarketsResource) -> None:
        self._markets = markets

        self.get = async_to_raw_response_wrapper(
            markets.get,
        )


class MarketsResourceWithStreamingResponse:
    def __init__(self, markets: MarketsResource) -> None:
        self._markets = markets

        self.get = to_streamed_response_wrapper(
            markets.get,
        )


class AsyncMarketsResourceWithStreamingResponse:
    def __init__(self, markets: AsyncMarketsResource) -> None:
        self._markets = markets

        self.get = async_to_streamed_response_wrapper(
            markets.get,
        )
