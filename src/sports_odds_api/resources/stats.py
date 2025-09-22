# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..types import stat_get_params
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
from ..types.stat_get_response import StatGetResponse

__all__ = ["StatsResource", "AsyncStatsResource"]


class StatsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#accessing-raw-response-data-eg-headers
        """
        return StatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#with_streaming_response
        """
        return StatsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        sport_id: str | Omit = omit,
        stat_id: str | Omit = omit,
        stat_level: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[StatGetResponse]:
        """
        Get a list of StatIDs

        Args:
          sport_id: SportID to get StatIDs for

          stat_id: StatID to get data for

          stat_level: Level of the stat, must be used in combination with sportID. Must be one of all,
              player, or team. Shows stats that are applicable to that specified entity,
              defaults to all.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/stats/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "sport_id": sport_id,
                        "stat_id": stat_id,
                        "stat_level": stat_level,
                    },
                    stat_get_params.StatGetParams,
                ),
                post_parser=DataWrapper[Optional[StatGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[StatGetResponse]], DataWrapper[StatGetResponse]),
        )


class AsyncStatsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#with_streaming_response
        """
        return AsyncStatsResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        sport_id: str | Omit = omit,
        stat_id: str | Omit = omit,
        stat_level: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[StatGetResponse]:
        """
        Get a list of StatIDs

        Args:
          sport_id: SportID to get StatIDs for

          stat_id: StatID to get data for

          stat_level: Level of the stat, must be used in combination with sportID. Must be one of all,
              player, or team. Shows stats that are applicable to that specified entity,
              defaults to all.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/stats/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "sport_id": sport_id,
                        "stat_id": stat_id,
                        "stat_level": stat_level,
                    },
                    stat_get_params.StatGetParams,
                ),
                post_parser=DataWrapper[Optional[StatGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[StatGetResponse]], DataWrapper[StatGetResponse]),
        )


class StatsResourceWithRawResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

        self.get = to_raw_response_wrapper(
            stats.get,
        )


class AsyncStatsResourceWithRawResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

        self.get = async_to_raw_response_wrapper(
            stats.get,
        )


class StatsResourceWithStreamingResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

        self.get = to_streamed_response_wrapper(
            stats.get,
        )


class AsyncStatsResourceWithStreamingResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

        self.get = async_to_streamed_response_wrapper(
            stats.get,
        )
