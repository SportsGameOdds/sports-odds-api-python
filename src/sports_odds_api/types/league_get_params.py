# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LeagueGetParams"]


class LeagueGetParams(TypedDict, total=False):
    league_id: Annotated[str, PropertyInfo(alias="leagueID")]
    """The league to get data for"""

    sport_id: Annotated[str, PropertyInfo(alias="sportID")]
    """The sport to get leagues for"""
