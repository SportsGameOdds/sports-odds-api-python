# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Market", "SupportSupportItem"]


class SupportSupportItem(BaseModel):
    supported: Optional[bool] = None
    """
    Whether this market is supported for the given league and bookmaker combination.
    """


class Market(BaseModel):
    active_events: Optional[float] = FieldInfo(alias="activeEvents", default=None)
    """
    The number of unique active events with available odds for this market across
    all supported league and bookmaker combinations.
    """

    bet_type_id: Optional[str] = FieldInfo(alias="betTypeID", default=None)
    """The type of bet"""

    is_main_derivative: Optional[bool] = FieldInfo(alias="isMainDerivative", default=None)
    """True if this is a sub-period of a main market"""

    is_main_market: Optional[bool] = FieldInfo(alias="isMainMarket", default=None)
    """True if this is a main market"""

    is_prop: Optional[bool] = FieldInfo(alias="isProp", default=None)
    """True if this is a prop bet"""

    is_sub_period: Optional[bool] = FieldInfo(alias="isSubPeriod", default=None)
    """True if this market is for a sub-period"""

    is_supported: Optional[bool] = FieldInfo(alias="isSupported", default=None)
    """True if this market is supported by at least one league/bookmaker."""

    market_group_id: Optional[str] = FieldInfo(alias="marketGroupID", default=None)
    """
    The unique identifier for the group (all sides of the market) this market
    belongs to
    """

    market_group_name: Optional[str] = FieldInfo(alias="marketGroupName", default=None)
    """The primary display name for this market's group"""

    market_group_name_alias: Optional[str] = FieldInfo(alias="marketGroupNameAlias", default=None)
    """An alternative display name for this market's group"""

    market_group_name_by_sport: Optional[Dict[str, str]] = FieldInfo(alias="marketGroupNameBySport", default=None)
    """Sport-specific market group names when they differ from the primary name"""

    odd_id: Optional[str] = FieldInfo(alias="oddID", default=None)
    """The unique identifier for this market"""

    period_id: Optional[str] = FieldInfo(alias="periodID", default=None)
    """The period of the event this market applies to"""

    player_id: Optional[str] = FieldInfo(alias="playerID", default=None)
    """Set to a player's unique playerID if it's a player prop"""

    prop_type: Optional[Literal["game_prop", "team_prop", "player_prop", "other_prop"]] = FieldInfo(
        alias="propType", default=None
    )
    """The type of prop bet"""

    side_id: Optional[str] = FieldInfo(alias="sideID", default=None)
    """The side of the bet"""

    stat_entity_id: Optional[str] = FieldInfo(alias="statEntityID", default=None)
    """The statEntityID represents whose performance on the stat is being evaluated"""

    stat_id: Optional[str] = FieldInfo(alias="statID", default=None)
    """The statistic which is being evaluated as a part of this market"""

    support: Optional[Dict[str, Dict[str, SupportSupportItem]]] = None
    """Nested object showing which leagues and bookmakers support this market."""

    team_id: Optional[str] = FieldInfo(alias="teamID", default=None)
    """Set to team's unique teamID if it's a team prop for a tournament type event"""
