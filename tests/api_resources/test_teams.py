# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sports_odds_api import SportsGameOdds, AsyncSportsGameOdds
from sports_odds_api.types import Team
from sports_odds_api.pagination import SyncNextCursorPage, AsyncNextCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTeams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: SportsGameOdds) -> None:
        team = client.teams.get()
        assert_matches_type(SyncNextCursorPage[Team], team, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: SportsGameOdds) -> None:
        team = client.teams.get(
            cursor="cursor",
            league_id="leagueID",
            limit=0,
            sport_id="sportID",
            team_id="teamID",
        )
        assert_matches_type(SyncNextCursorPage[Team], team, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: SportsGameOdds) -> None:
        response = client.teams.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(SyncNextCursorPage[Team], team, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: SportsGameOdds) -> None:
        with client.teams.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(SyncNextCursorPage[Team], team, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTeams:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncSportsGameOdds) -> None:
        team = await async_client.teams.get()
        assert_matches_type(AsyncNextCursorPage[Team], team, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncSportsGameOdds) -> None:
        team = await async_client.teams.get(
            cursor="cursor",
            league_id="leagueID",
            limit=0,
            sport_id="sportID",
            team_id="teamID",
        )
        assert_matches_type(AsyncNextCursorPage[Team], team, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncSportsGameOdds) -> None:
        response = await async_client.teams.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(AsyncNextCursorPage[Team], team, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncSportsGameOdds) -> None:
        async with async_client.teams.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(AsyncNextCursorPage[Team], team, path=["response"])

        assert cast(Any, response.is_closed) is True
