# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from sports_odds_api import SportsGameOdds, AsyncSportsGameOdds
from sports_odds_api.types import AccountUsage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccount:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_usage(self, client: SportsGameOdds) -> None:
        account = client.account.get_usage()
        assert_matches_type(Optional[AccountUsage], account, path=["response"])

    @parametrize
    def test_raw_response_get_usage(self, client: SportsGameOdds) -> None:
        response = client.account.with_raw_response.get_usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Optional[AccountUsage], account, path=["response"])

    @parametrize
    def test_streaming_response_get_usage(self, client: SportsGameOdds) -> None:
        with client.account.with_streaming_response.get_usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Optional[AccountUsage], account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccount:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_usage(self, async_client: AsyncSportsGameOdds) -> None:
        account = await async_client.account.get_usage()
        assert_matches_type(Optional[AccountUsage], account, path=["response"])

    @parametrize
    async def test_raw_response_get_usage(self, async_client: AsyncSportsGameOdds) -> None:
        response = await async_client.account.with_raw_response.get_usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(Optional[AccountUsage], account, path=["response"])

    @parametrize
    async def test_streaming_response_get_usage(self, async_client: AsyncSportsGameOdds) -> None:
        async with async_client.account.with_streaming_response.get_usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Optional[AccountUsage], account, path=["response"])

        assert cast(Any, response.is_closed) is True
