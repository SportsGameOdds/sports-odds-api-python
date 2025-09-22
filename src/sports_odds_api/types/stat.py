# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Stat", "Displays", "SupportedLevels", "Units", "UnitsLong", "UnitsShort"]


class Displays(BaseModel):
    long: Optional[str] = None

    short: Optional[str] = None


class SupportedLevels(BaseModel):
    all: Optional[bool] = None

    player: Optional[bool] = None

    team: Optional[bool] = None


class UnitsLong(BaseModel):
    plural: Optional[str] = None

    singular: Optional[str] = None


class UnitsShort(BaseModel):
    plural: Optional[str] = None

    singular: Optional[str] = None


class Units(BaseModel):
    long: Optional[UnitsLong] = None

    short: Optional[UnitsShort] = None


class Stat(BaseModel):
    description: Optional[str] = None

    displays: Optional[Displays] = None

    is_score_stat: Optional[bool] = FieldInfo(alias="isScoreStat", default=None)

    stat_id: Optional[str] = FieldInfo(alias="statID", default=None)

    supported_levels: Optional[SupportedLevels] = FieldInfo(alias="supportedLevels", default=None)

    supported_sports: Optional[Dict[str, object]] = FieldInfo(alias="supportedSports", default=None)

    units: Optional[Units] = None
