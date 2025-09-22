# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..types import league_get_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import DataWrapper
from .._base_client import make_request_options
from ..types.league_get_response import LeagueGetResponse

__all__ = ["LeaguesResource", "AsyncLeaguesResource"]


class LeaguesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LeaguesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#accessing-raw-response-data-eg-headers
        """
        return LeaguesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LeaguesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#with_streaming_response
        """
        return LeaguesResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        league_id: str | Omit = omit,
        sport_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[LeagueGetResponse]:
        """
        Get a list of Leagues

        Args:
          league_id: The league to get data for

          sport_id: The sport to get leagues for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/leagues/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "league_id": league_id,
                        "sport_id": sport_id,
                    },
                    league_get_params.LeagueGetParams,
                ),
                post_parser=DataWrapper[Optional[LeagueGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LeagueGetResponse]], DataWrapper[LeagueGetResponse]),
        )


class AsyncLeaguesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLeaguesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLeaguesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLeaguesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#with_streaming_response
        """
        return AsyncLeaguesResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        league_id: str | Omit = omit,
        sport_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[LeagueGetResponse]:
        """
        Get a list of Leagues

        Args:
          league_id: The league to get data for

          sport_id: The sport to get leagues for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/leagues/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "league_id": league_id,
                        "sport_id": sport_id,
                    },
                    league_get_params.LeagueGetParams,
                ),
                post_parser=DataWrapper[Optional[LeagueGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LeagueGetResponse]], DataWrapper[LeagueGetResponse]),
        )


class LeaguesResourceWithRawResponse:
    def __init__(self, leagues: LeaguesResource) -> None:
        self._leagues = leagues

        self.get = to_raw_response_wrapper(
            leagues.get,
        )


class AsyncLeaguesResourceWithRawResponse:
    def __init__(self, leagues: AsyncLeaguesResource) -> None:
        self._leagues = leagues

        self.get = async_to_raw_response_wrapper(
            leagues.get,
        )


class LeaguesResourceWithStreamingResponse:
    def __init__(self, leagues: LeaguesResource) -> None:
        self._leagues = leagues

        self.get = to_streamed_response_wrapper(
            leagues.get,
        )


class AsyncLeaguesResourceWithStreamingResponse:
    def __init__(self, leagues: AsyncLeaguesResource) -> None:
        self._leagues = leagues

        self.get = async_to_streamed_response_wrapper(
            leagues.get,
        )
