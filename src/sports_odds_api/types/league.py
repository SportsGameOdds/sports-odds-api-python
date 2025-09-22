# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["League"]


class League(BaseModel):
    enabled: Optional[bool] = None

    league_id: Optional[str] = FieldInfo(alias="leagueID", default=None)

    name: Optional[str] = None

    short_name: Optional[str] = FieldInfo(alias="shortName", default=None)

    sport_id: Optional[str] = FieldInfo(alias="sportID", default=None)
