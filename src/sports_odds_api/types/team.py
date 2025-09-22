# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Team", "Colors", "Lookups", "Names", "Standings"]


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


class Standings(BaseModel):
    losses: Optional[float] = None

    played: Optional[float] = None

    position: Optional[str] = None

    record: Optional[str] = None

    ties: Optional[float] = None

    wins: Optional[float] = None


class Team(BaseModel):
    colors: Optional[Colors] = None

    league_id: Optional[str] = FieldInfo(alias="leagueID", default=None)

    logo: Optional[str] = None

    lookups: Optional[Lookups] = None

    names: Optional[Names] = None

    sport_id: Optional[str] = FieldInfo(alias="sportID", default=None)

    standings: Optional[Standings] = None

    team_id: Optional[str] = FieldInfo(alias="teamID", default=None)
