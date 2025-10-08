# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sports_odds_api import SportsGameOdds, AsyncSportsGameOdds
from sports_odds_api.types import Event
from sports_odds_api._utils import parse_datetime
from sports_odds_api.pagination import SyncNextCursorPage, AsyncNextCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: SportsGameOdds) -> None:
        event = client.events.get()
        assert_matches_type(SyncNextCursorPage[Event], event, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: SportsGameOdds) -> None:
        event = client.events.get(
            bookmaker_id="bookmakerID",
            cancelled=True,
            cursor="cursor",
            ended=True,
            event_id="eventID",
            event_ids="eventIDs",
            finalized=True,
            include_alt_lines=True,
            include_opposing_odds=True,
            league_id="leagueID",
            limit=0,
            live=True,
            odd_id="oddID",
            odds_available=True,
            odds_present=True,
            player_id="playerID",
            sport_id="sportID",
            started=True,
            starts_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            starts_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            team_id="teamID",
            type="type",
        )
        assert_matches_type(SyncNextCursorPage[Event], event, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: SportsGameOdds) -> None:
        response = client.events.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(SyncNextCursorPage[Event], event, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: SportsGameOdds) -> None:
        with client.events.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(SyncNextCursorPage[Event], event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncSportsGameOdds) -> None:
        event = await async_client.events.get()
        assert_matches_type(AsyncNextCursorPage[Event], event, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncSportsGameOdds) -> None:
        event = await async_client.events.get(
            bookmaker_id="bookmakerID",
            cancelled=True,
            cursor="cursor",
            ended=True,
            event_id="eventID",
            event_ids="eventIDs",
            finalized=True,
            include_alt_lines=True,
            include_opposing_odds=True,
            league_id="leagueID",
            limit=0,
            live=True,
            odd_id="oddID",
            odds_available=True,
            odds_present=True,
            player_id="playerID",
            sport_id="sportID",
            started=True,
            starts_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            starts_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            team_id="teamID",
            type="type",
        )
        assert_matches_type(AsyncNextCursorPage[Event], event, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncSportsGameOdds) -> None:
        response = await async_client.events.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(AsyncNextCursorPage[Event], event, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncSportsGameOdds) -> None:
        async with async_client.events.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(AsyncNextCursorPage[Event], event, path=["response"])

        assert cast(Any, response.is_closed) is True
