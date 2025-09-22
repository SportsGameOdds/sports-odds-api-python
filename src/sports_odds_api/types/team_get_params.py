# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TeamGetParams"]


class TeamGetParams(TypedDict, total=False):
    cursor: str
    """The cursor for the request.

    Used to get the next group of Teams. This should be the nextCursor from the
    prior response.
    """

    league_id: Annotated[str, PropertyInfo(alias="leagueID")]
    """A single leagueID or comma-separated list of leagueIDs to get Teams for"""

    limit: float
    """The maximum number of Teams to return"""

    sport_id: Annotated[str, PropertyInfo(alias="sportID")]
    """A single sportID or comma-separated list of sportIDs to get Teams for"""

    team_id: Annotated[str, PropertyInfo(alias="teamID")]
    """A single teamID or comma-separated list of teamIDs to get data for"""
