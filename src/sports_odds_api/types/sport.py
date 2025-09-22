# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Sport", "EventWord", "EventWordLong", "EventWordShort", "PointWord", "PointWordLong", "PointWordShort"]


class EventWordLong(BaseModel):
    plural: Optional[str] = None

    singular: Optional[str] = None


class EventWordShort(BaseModel):
    plural: Optional[str] = None

    singular: Optional[str] = None


class EventWord(BaseModel):
    long: Optional[EventWordLong] = None

    short: Optional[EventWordShort] = None


class PointWordLong(BaseModel):
    plural: Optional[str] = None

    singular: Optional[str] = None


class PointWordShort(BaseModel):
    plural: Optional[str] = None

    singular: Optional[str] = None


class PointWord(BaseModel):
    long: Optional[PointWordLong] = None

    short: Optional[PointWordShort] = None


class Sport(BaseModel):
    background_image: Optional[str] = FieldInfo(alias="backgroundImage", default=None)

    base_periods: Optional[List[str]] = FieldInfo(alias="basePeriods", default=None)

    clock_type: Optional[str] = FieldInfo(alias="clockType", default=None)

    default_popularity_score: Optional[float] = FieldInfo(alias="defaultPopularityScore", default=None)

    enabled: Optional[bool] = None

    event_word: Optional[EventWord] = FieldInfo(alias="eventWord", default=None)

    extra_periods: Optional[List[str]] = FieldInfo(alias="extraPeriods", default=None)

    has_meaningful_home_away: Optional[bool] = FieldInfo(alias="hasMeaningfulHomeAway", default=None)

    image_icon: Optional[str] = FieldInfo(alias="imageIcon", default=None)

    name: Optional[str] = None

    point_word: Optional[PointWord] = FieldInfo(alias="pointWord", default=None)

    short_name: Optional[str] = FieldInfo(alias="shortName", default=None)

    sport_id: Optional[str] = FieldInfo(alias="sportID", default=None)

    square_image: Optional[str] = FieldInfo(alias="squareImage", default=None)
