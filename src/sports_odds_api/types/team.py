# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Team", "Coach", "Colors", "Lookups", "Names", "Owner", "Standings", "Venue"]


class Coach(BaseModel):
    name: Optional[str] = None


class Colors(BaseModel):
    primary: Optional[str] = None

    primary_contrast: Optional[str] = FieldInfo(alias="primaryContrast", default=None)

    secondary: Optional[str] = None

    secondary_contrast: Optional[str] = FieldInfo(alias="secondaryContrast", default=None)


class Lookups(BaseModel):
    team_name: Optional[List[str]] = FieldInfo(alias="teamName", default=None)


class Names(BaseModel):
    long: Optional[str] = None

    medium: Optional[str] = None

    short: Optional[str] = None


class Owner(BaseModel):
    name: Optional[str] = None


class Standings(BaseModel):
    last5: Optional[str] = None

    losses: Optional[float] = None

    played: Optional[float] = None

    position: Optional[str] = None

    record: Optional[str] = None

    streak: Optional[float] = None

    ties: Optional[float] = None

    wins: Optional[float] = None


class Venue(BaseModel):
    address: Optional[str] = None

    capacity: Optional[float] = None

    city: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    country_name: Optional[str] = FieldInfo(alias="countryName", default=None)

    name: Optional[str] = None

    region_code: Optional[str] = FieldInfo(alias="regionCode", default=None)

    region_name: Optional[str] = FieldInfo(alias="regionName", default=None)


class Team(BaseModel):
    coach: Optional[Coach] = None

    colors: Optional[Colors] = None

    league_id: Optional[str] = FieldInfo(alias="leagueID", default=None)

    logo: Optional[str] = None

    lookups: Optional[Lookups] = None

    names: Optional[Names] = None

    owner: Optional[Owner] = None

    sport_id: Optional[str] = FieldInfo(alias="sportID", default=None)

    standings: Optional[Standings] = None

    team_id: Optional[str] = FieldInfo(alias="teamID", default=None)

    venue: Optional[Venue] = None
