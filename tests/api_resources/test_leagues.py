# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from sports_odds_api import SportsGameOdds, AsyncSportsGameOdds
from sports_odds_api.types import LeagueGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLeagues:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: SportsGameOdds) -> None:
        league = client.leagues.get()
        assert_matches_type(Optional[LeagueGetResponse], league, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: SportsGameOdds) -> None:
        league = client.leagues.get(
            league_id="leagueID",
            sport_id="sportID",
        )
        assert_matches_type(Optional[LeagueGetResponse], league, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: SportsGameOdds) -> None:
        response = client.leagues.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        league = response.parse()
        assert_matches_type(Optional[LeagueGetResponse], league, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: SportsGameOdds) -> None:
        with client.leagues.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            league = response.parse()
            assert_matches_type(Optional[LeagueGetResponse], league, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLeagues:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncSportsGameOdds) -> None:
        league = await async_client.leagues.get()
        assert_matches_type(Optional[LeagueGetResponse], league, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncSportsGameOdds) -> None:
        league = await async_client.leagues.get(
            league_id="leagueID",
            sport_id="sportID",
        )
        assert_matches_type(Optional[LeagueGetResponse], league, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncSportsGameOdds) -> None:
        response = await async_client.leagues.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        league = await response.parse()
        assert_matches_type(Optional[LeagueGetResponse], league, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncSportsGameOdds) -> None:
        async with async_client.leagues.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            league = await response.parse()
            assert_matches_type(Optional[LeagueGetResponse], league, path=["response"])

        assert cast(Any, response.is_closed) is True
