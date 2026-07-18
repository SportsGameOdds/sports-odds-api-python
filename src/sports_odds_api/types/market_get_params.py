# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MarketGetParams"]


class MarketGetParams(TypedDict, total=False):
    bet_type_id: Annotated[str, PropertyInfo(alias="betTypeID")]
    """A single betTypeID or comma-separated list of betTypeIDs to filter Markets by"""

    bookmaker_id: Annotated[str, PropertyInfo(alias="bookmakerID")]
    """
    A single bookmakerID or comma-separated list of bookmakerIDs to filter Markets
    by
    """

    cursor: str
    """The cursor for pagination. Use nextCursor from prior response."""

    is_main_market: Annotated[bool, PropertyInfo(alias="isMainMarket")]
    """
    Filter to only include main markets (main period moneyline, spread, and
    over/under)
    """

    is_prop: Annotated[bool, PropertyInfo(alias="isProp")]
    """Filter by whether it is any type of prop bet market"""

    is_sub_period: Annotated[bool, PropertyInfo(alias="isSubPeriod")]
    """Filter by whether it tracks a sub/non-main period"""

    is_supported: Annotated[bool, PropertyInfo(alias="isSupported")]
    """
    Filter whether this market is fully supported by at least 1 bookmaker in at
    least 1 league. Defaults to true if not specified.
    """

    league_id: Annotated[str, PropertyInfo(alias="leagueID")]
    """A single leagueID or comma-separated list of leagueIDs to filter Markets by"""

    limit: float
    """The maximum number of Markets to return (default: 100, max: 10000)"""

    odd_id: Annotated[str, PropertyInfo(alias="oddID")]
    """A single oddID or comma-separated list of oddIDs.

    Used to specify specific Markets to return.
    """

    period_id: Annotated[str, PropertyInfo(alias="periodID")]
    """A single periodID or comma-separated list of periodIDs to filter Markets by"""

    prop_type: Annotated[str, PropertyInfo(alias="propType")]
    """Filter by prop type (game_prop, team_prop, player_prop, other_prop)"""

    side_id: Annotated[str, PropertyInfo(alias="sideID")]
    """A single sideID or comma-separated list of sideIDs to filter Markets by"""

    sport_id: Annotated[str, PropertyInfo(alias="sportID")]
    """A single sportID or comma-separated list of sportIDs to filter Markets by"""

    stat_entity_id: Annotated[str, PropertyInfo(alias="statEntityID")]
    """
    A single statEntityID or comma-separated list of statEntityIDs to filter Markets
    by
    """

    stat_id: Annotated[str, PropertyInfo(alias="statID")]
    """A single statID or comma-separated list of statIDs to filter Markets by"""
