# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sports_odds_api import SportsGameOdds, AsyncSportsGameOdds
from sports_odds_api.types import StreamEventsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStream:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_events(self, client: SportsGameOdds) -> None:
        stream = client.stream.events()
        assert_matches_type(StreamEventsResponse, stream, path=["response"])

    @parametrize
    def test_method_events_with_all_params(self, client: SportsGameOdds) -> None:
        stream = client.stream.events(
            event_id="eventID",
            feed="feed",
            league_id="leagueID",
        )
        assert_matches_type(StreamEventsResponse, stream, path=["response"])

    @parametrize
    def test_raw_response_events(self, client: SportsGameOdds) -> None:
        response = client.stream.with_raw_response.events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert_matches_type(StreamEventsResponse, stream, path=["response"])

    @parametrize
    def test_streaming_response_events(self, client: SportsGameOdds) -> None:
        with client.stream.with_streaming_response.events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert_matches_type(StreamEventsResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStream:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_events(self, async_client: AsyncSportsGameOdds) -> None:
        stream = await async_client.stream.events()
        assert_matches_type(StreamEventsResponse, stream, path=["response"])

    @parametrize
    async def test_method_events_with_all_params(self, async_client: AsyncSportsGameOdds) -> None:
        stream = await async_client.stream.events(
            event_id="eventID",
            feed="feed",
            league_id="leagueID",
        )
        assert_matches_type(StreamEventsResponse, stream, path=["response"])

    @parametrize
    async def test_raw_response_events(self, async_client: AsyncSportsGameOdds) -> None:
        response = await async_client.stream.with_raw_response.events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert_matches_type(StreamEventsResponse, stream, path=["response"])

    @parametrize
    async def test_streaming_response_events(self, async_client: AsyncSportsGameOdds) -> None:
        async with async_client.stream.with_streaming_response.events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert_matches_type(StreamEventsResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True
