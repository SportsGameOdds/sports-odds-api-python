# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Event",
    "Activity",
    "Info",
    "InfoBroadcast",
    "InfoReferee",
    "InfoVenue",
    "Odds",
    "OddsByBookmaker",
    "Players",
    "Status",
    "StatusPeriods",
    "Teams",
    "TeamsAway",
    "TeamsAwayColors",
    "TeamsAwayNames",
    "TeamsHome",
    "TeamsHomeColors",
    "TeamsHomeNames",
]


class Activity(BaseModel):
    count: Optional[float] = None

    score: Optional[float] = None


class InfoBroadcast(BaseModel):
    broadcaster_id: Optional[str] = FieldInfo(alias="broadcasterID", default=None)

    name: Optional[str] = None

    type: Optional[Literal["tv", "webstream", "subscription", "sportsbook"]] = None


class InfoReferee(BaseModel):
    name: Optional[str] = None


class InfoVenue(BaseModel):
    address: Optional[str] = None

    capacity: Optional[float] = None

    city: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    country_name: Optional[str] = FieldInfo(alias="countryName", default=None)

    name: Optional[str] = None

    region_code: Optional[str] = FieldInfo(alias="regionCode", default=None)

    region_name: Optional[str] = FieldInfo(alias="regionName", default=None)


class Info(BaseModel):
    broadcasts: Optional[List[InfoBroadcast]] = None

    referee: Optional[InfoReferee] = None

    season_week: Optional[str] = FieldInfo(alias="seasonWeek", default=None)

    venue: Optional[InfoVenue] = None


class OddsByBookmaker(BaseModel):
    available: Optional[bool] = None

    bookmaker_id: Optional[str] = FieldInfo(alias="bookmakerID", default=None)

    close_odds: Optional[str] = FieldInfo(alias="closeOdds", default=None)

    close_over_under: Optional[str] = FieldInfo(alias="closeOverUnder", default=None)

    close_spread: Optional[str] = FieldInfo(alias="closeSpread", default=None)

    is_main_line: Optional[bool] = FieldInfo(alias="isMainLine", default=None)

    last_updated_at: Optional[datetime] = FieldInfo(alias="lastUpdatedAt", default=None)

    odds: Optional[str] = None

    open_odds: Optional[str] = FieldInfo(alias="openOdds", default=None)

    open_over_under: Optional[str] = FieldInfo(alias="openOverUnder", default=None)

    open_spread: Optional[str] = FieldInfo(alias="openSpread", default=None)

    over_under: Optional[str] = FieldInfo(alias="overUnder", default=None)

    spread: Optional[str] = None


class Odds(BaseModel):
    bet_type_id: Optional[str] = FieldInfo(alias="betTypeID", default=None)

    book_odds: Optional[str] = FieldInfo(alias="bookOdds", default=None)

    book_odds_available: Optional[bool] = FieldInfo(alias="bookOddsAvailable", default=None)

    book_over_under: Optional[str] = FieldInfo(alias="bookOverUnder", default=None)

    book_spread: Optional[str] = FieldInfo(alias="bookSpread", default=None)

    by_bookmaker: Optional[Dict[str, OddsByBookmaker]] = FieldInfo(alias="byBookmaker", default=None)

    cancelled: Optional[bool] = None

    ended: Optional[bool] = None

    fair_odds: Optional[str] = FieldInfo(alias="fairOdds", default=None)

    fair_odds_available: Optional[bool] = FieldInfo(alias="fairOddsAvailable", default=None)

    fair_over_under: Optional[str] = FieldInfo(alias="fairOverUnder", default=None)

    fair_spread: Optional[str] = FieldInfo(alias="fairSpread", default=None)

    market_name: Optional[str] = FieldInfo(alias="marketName", default=None)

    odd_id: Optional[str] = FieldInfo(alias="oddID", default=None)

    opposing_odd_id: Optional[str] = FieldInfo(alias="opposingOddID", default=None)

    period_id: Optional[str] = FieldInfo(alias="periodID", default=None)

    player_id: Optional[str] = FieldInfo(alias="playerID", default=None)

    score: Optional[float] = None

    scoring_supported: Optional[bool] = FieldInfo(alias="scoringSupported", default=None)

    side_id: Optional[str] = FieldInfo(alias="sideID", default=None)

    started: Optional[bool] = None

    stat_entity_id: Optional[str] = FieldInfo(alias="statEntityID", default=None)

    stat_id: Optional[str] = FieldInfo(alias="statID", default=None)


class Players(BaseModel):
    alias: Optional[str] = None

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    name: Optional[str] = None

    photo: Optional[str] = None

    player_id: Optional[str] = FieldInfo(alias="playerID", default=None)

    status: Optional[Literal["ir", "active", "out", "suspended", "questionable", "doubtful", "probable"]] = None

    status_details: Optional[str] = FieldInfo(alias="statusDetails", default=None)

    team_id: Optional[str] = FieldInfo(alias="teamID", default=None)


class StatusPeriods(BaseModel):
    ended: Optional[List[str]] = None

    started: Optional[List[str]] = None


class Status(BaseModel):
    cancelled: Optional[bool] = None

    completed: Optional[bool] = None

    current_period_id: Optional[str] = FieldInfo(alias="currentPeriodID", default=None)

    delayed: Optional[bool] = None

    display_long: Optional[str] = FieldInfo(alias="displayLong", default=None)

    display_short: Optional[str] = FieldInfo(alias="displayShort", default=None)

    ended: Optional[bool] = None

    finalized: Optional[bool] = None

    hard_start: Optional[bool] = FieldInfo(alias="hardStart", default=None)

    live: Optional[bool] = None

    odds_available: Optional[bool] = FieldInfo(alias="oddsAvailable", default=None)

    odds_present: Optional[bool] = FieldInfo(alias="oddsPresent", default=None)

    periods: Optional[StatusPeriods] = None

    previous_period_id: Optional[str] = FieldInfo(alias="previousPeriodID", default=None)

    re_grade: Optional[bool] = FieldInfo(alias="reGrade", default=None)

    started: Optional[bool] = None

    starts_at: Optional[datetime] = FieldInfo(alias="startsAt", default=None)


class TeamsAwayColors(BaseModel):
    primary: Optional[str] = None

    primary_contrast: Optional[str] = FieldInfo(alias="primaryContrast", default=None)

    secondary: Optional[str] = None

    secondary_contrast: Optional[str] = FieldInfo(alias="secondaryContrast", default=None)


class TeamsAwayNames(BaseModel):
    long: Optional[str] = None

    medium: Optional[str] = None

    short: Optional[str] = None


class TeamsAway(BaseModel):
    colors: Optional[TeamsAwayColors] = None

    logo: Optional[str] = None

    names: Optional[TeamsAwayNames] = None

    score: Optional[float] = None

    stat_entity_id: Optional[str] = FieldInfo(alias="statEntityID", default=None)

    team_id: Optional[str] = FieldInfo(alias="teamID", default=None)


class TeamsHomeColors(BaseModel):
    primary: Optional[str] = None

    primary_contrast: Optional[str] = FieldInfo(alias="primaryContrast", default=None)

    secondary: Optional[str] = None

    secondary_contrast: Optional[str] = FieldInfo(alias="secondaryContrast", default=None)


class TeamsHomeNames(BaseModel):
    long: Optional[str] = None

    medium: Optional[str] = None

    short: Optional[str] = None


class TeamsHome(BaseModel):
    colors: Optional[TeamsHomeColors] = None

    logo: Optional[str] = None

    names: Optional[TeamsHomeNames] = None

    score: Optional[float] = None

    stat_entity_id: Optional[str] = FieldInfo(alias="statEntityID", default=None)

    team_id: Optional[str] = FieldInfo(alias="teamID", default=None)


class Teams(BaseModel):
    away: Optional[TeamsAway] = None

    home: Optional[TeamsHome] = None


class Event(BaseModel):
    activity: Optional[Activity] = None

    event_id: Optional[str] = FieldInfo(alias="eventID", default=None)

    info: Optional[Info] = None

    league_id: Optional[str] = FieldInfo(alias="leagueID", default=None)

    manual: Optional[bool] = None

    odds: Optional[Dict[str, Odds]] = None

    players: Optional[Dict[str, Players]] = None

    results: Optional[Dict[str, Dict[str, Dict[str, float]]]] = None
    """Nested results in the format `{periodID}.{statEntityID}.{statID} → number`."""

    sport_id: Optional[str] = FieldInfo(alias="sportID", default=None)

    status: Optional[Status] = None

    teams: Optional[Teams] = None

    type: Optional[str] = None
