# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.sport_get_response import SportGetResponse

__all__ = ["SportsResource", "AsyncSportsResource"]


class SportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#accessing-raw-response-data-eg-headers
        """
        return SportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#with_streaming_response
        """
        return SportsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SportGetResponse]:
        """Get a list of sports"""
        return self._get(
            "/sports/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[SportGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SportGetResponse]], DataWrapper[SportGetResponse]),
        )


class AsyncSportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#with_streaming_response
        """
        return AsyncSportsResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SportGetResponse]:
        """Get a list of sports"""
        return await self._get(
            "/sports/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[SportGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SportGetResponse]], DataWrapper[SportGetResponse]),
        )


class SportsResourceWithRawResponse:
    def __init__(self, sports: SportsResource) -> None:
        self._sports = sports

        self.get = to_raw_response_wrapper(
            sports.get,
        )


class AsyncSportsResourceWithRawResponse:
    def __init__(self, sports: AsyncSportsResource) -> None:
        self._sports = sports

        self.get = async_to_raw_response_wrapper(
            sports.get,
        )


class SportsResourceWithStreamingResponse:
    def __init__(self, sports: SportsResource) -> None:
        self._sports = sports

        self.get = to_streamed_response_wrapper(
            sports.get,
        )


class AsyncSportsResourceWithStreamingResponse:
    def __init__(self, sports: AsyncSportsResource) -> None:
        self._sports = sports

        self.get = async_to_streamed_response_wrapper(
            sports.get,
        )
