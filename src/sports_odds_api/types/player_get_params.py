# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PlayerGetParams"]


class PlayerGetParams(TypedDict, total=False):
    cursor: str
    """The cursor for the request.

    Used to get the next group of Players. This should be the nextCursor from the
    prior response.
    """

    event_id: Annotated[str, PropertyInfo(alias="eventID")]
    """EventID to get Players data for"""

    limit: float
    """The maximum number of Players to return"""

    player_id: Annotated[str, PropertyInfo(alias="playerID")]
    """PlayerID to get data for"""

    team_id: Annotated[str, PropertyInfo(alias="teamID")]
    """TeamID to get Players data for"""
