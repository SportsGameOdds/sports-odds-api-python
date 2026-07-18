# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sports_odds_api import SportsGameOdds, AsyncSportsGameOdds
from sports_odds_api.types import Market
from sports_odds_api.pagination import SyncNextCursorPage, AsyncNextCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMarkets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: SportsGameOdds) -> None:
        market = client.markets.get()
        assert_matches_type(SyncNextCursorPage[Market], market, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: SportsGameOdds) -> None:
        market = client.markets.get(
            bet_type_id="betTypeID",
            bookmaker_id="bookmakerID",
            cursor="cursor",
            is_main_market=True,
            is_prop=True,
            is_sub_period=True,
            is_supported=True,
            league_id="leagueID",
            limit=0,
            odd_id="oddID",
            period_id="periodID",
            prop_type="propType",
            side_id="sideID",
            sport_id="sportID",
            stat_entity_id="statEntityID",
            stat_id="statID",
        )
        assert_matches_type(SyncNextCursorPage[Market], market, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: SportsGameOdds) -> None:
        response = client.markets.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = response.parse()
        assert_matches_type(SyncNextCursorPage[Market], market, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: SportsGameOdds) -> None:
        with client.markets.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = response.parse()
            assert_matches_type(SyncNextCursorPage[Market], market, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMarkets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncSportsGameOdds) -> None:
        market = await async_client.markets.get()
        assert_matches_type(AsyncNextCursorPage[Market], market, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncSportsGameOdds) -> None:
        market = await async_client.markets.get(
            bet_type_id="betTypeID",
            bookmaker_id="bookmakerID",
            cursor="cursor",
            is_main_market=True,
            is_prop=True,
            is_sub_period=True,
            is_supported=True,
            league_id="leagueID",
            limit=0,
            odd_id="oddID",
            period_id="periodID",
            prop_type="propType",
            side_id="sideID",
            sport_id="sportID",
            stat_entity_id="statEntityID",
            stat_id="statID",
        )
        assert_matches_type(AsyncNextCursorPage[Market], market, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncSportsGameOdds) -> None:
        response = await async_client.markets.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = await response.parse()
        assert_matches_type(AsyncNextCursorPage[Market], market, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncSportsGameOdds) -> None:
        async with async_client.markets.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = await response.parse()
            assert_matches_type(AsyncNextCursorPage[Market], market, path=["response"])

        assert cast(Any, response.is_closed) is True
