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
from ..types.account_usage import AccountUsage

__all__ = ["AccountResource", "AsyncAccountResource"]


class AccountResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#accessing-raw-response-data-eg-headers
        """
        return AccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#with_streaming_response
        """
        return AccountResourceWithStreamingResponse(self)

    def get_usage(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AccountUsage]:
        """Get rate-limits and usage data about your API key"""
        return self._get(
            "/account/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[AccountUsage]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccountUsage]], DataWrapper[AccountUsage]),
        )


class AsyncAccountResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#with_streaming_response
        """
        return AsyncAccountResourceWithStreamingResponse(self)

    async def get_usage(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AccountUsage]:
        """Get rate-limits and usage data about your API key"""
        return await self._get(
            "/account/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[AccountUsage]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccountUsage]], DataWrapper[AccountUsage]),
        )


class AccountResourceWithRawResponse:
    def __init__(self, account: AccountResource) -> None:
        self._account = account

        self.get_usage = to_raw_response_wrapper(
            account.get_usage,
        )


class AsyncAccountResourceWithRawResponse:
    def __init__(self, account: AsyncAccountResource) -> None:
        self._account = account

        self.get_usage = async_to_raw_response_wrapper(
            account.get_usage,
        )


class AccountResourceWithStreamingResponse:
    def __init__(self, account: AccountResource) -> None:
        self._account = account

        self.get_usage = to_streamed_response_wrapper(
            account.get_usage,
        )


class AsyncAccountResourceWithStreamingResponse:
    def __init__(self, account: AsyncAccountResource) -> None:
        self._account = account

        self.get_usage = async_to_streamed_response_wrapper(
            account.get_usage,
        )
