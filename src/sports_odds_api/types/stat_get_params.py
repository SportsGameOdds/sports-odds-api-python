# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StatGetParams"]


class StatGetParams(TypedDict, total=False):
    sport_id: Annotated[str, PropertyInfo(alias="sportID")]
    """SportID to get StatIDs for"""

    stat_id: Annotated[str, PropertyInfo(alias="statID")]
    """StatID to get data for"""

    stat_level: Annotated[str, PropertyInfo(alias="statLevel")]
    """Level of the stat, must be used in combination with sportID.

    Must be one of all, player, or team. Shows stats that are applicable to that
    specified entity, defaults to all.
    """
