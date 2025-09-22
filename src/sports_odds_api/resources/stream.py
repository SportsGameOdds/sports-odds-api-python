# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import stream_events_params
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
from .._base_client import make_request_options
from ..types.stream_events_response import StreamEventsResponse

__all__ = ["StreamResource", "AsyncStreamResource"]


class StreamResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StreamResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#accessing-raw-response-data-eg-headers
        """
        return StreamResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StreamResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#with_streaming_response
        """
        return StreamResourceWithStreamingResponse(self)

    def events(
        self,
        *,
        event_id: str | Omit = omit,
        feed: str | Omit = omit,
        league_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamEventsResponse:
        """
        Setup streamed (WebSocket) connection

        Args:
          event_id: An eventID to stream events for

          feed: The feed you would like to subscribe to

          league_id: A leagueID to stream events for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/stream/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "event_id": event_id,
                        "feed": feed,
                        "league_id": league_id,
                    },
                    stream_events_params.StreamEventsParams,
                ),
            ),
            cast_to=StreamEventsResponse,
        )


class AsyncStreamResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStreamResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStreamResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStreamResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/SportsGameOdds/sports-odds-api-python#with_streaming_response
        """
        return AsyncStreamResourceWithStreamingResponse(self)

    async def events(
        self,
        *,
        event_id: str | Omit = omit,
        feed: str | Omit = omit,
        league_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamEventsResponse:
        """
        Setup streamed (WebSocket) connection

        Args:
          event_id: An eventID to stream events for

          feed: The feed you would like to subscribe to

          league_id: A leagueID to stream events for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/stream/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "event_id": event_id,
                        "feed": feed,
                        "league_id": league_id,
                    },
                    stream_events_params.StreamEventsParams,
                ),
            ),
            cast_to=StreamEventsResponse,
        )


class StreamResourceWithRawResponse:
    def __init__(self, stream: StreamResource) -> None:
        self._stream = stream

        self.events = to_raw_response_wrapper(
            stream.events,
        )


class AsyncStreamResourceWithRawResponse:
    def __init__(self, stream: AsyncStreamResource) -> None:
        self._stream = stream

        self.events = async_to_raw_response_wrapper(
            stream.events,
        )


class StreamResourceWithStreamingResponse:
    def __init__(self, stream: StreamResource) -> None:
        self._stream = stream

        self.events = to_streamed_response_wrapper(
            stream.events,
        )


class AsyncStreamResourceWithStreamingResponse:
    def __init__(self, stream: AsyncStreamResource) -> None:
        self._stream = stream

        self.events = async_to_streamed_response_wrapper(
            stream.events,
        )
