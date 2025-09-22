# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Player", "Lookups", "Names", "PlayerTeams"]


class Lookups(BaseModel):
    any_name: Optional[List[str]] = FieldInfo(alias="anyName", default=None)

    full_name: Optional[List[str]] = FieldInfo(alias="fullName", default=None)

    initials: Optional[List[str]] = None


class Names(BaseModel):
    display: Optional[str] = None

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)


class PlayerTeams(BaseModel):
    team_id: Optional[str] = FieldInfo(alias="teamID", default=None)


class Player(BaseModel):
    aliases: Optional[List[str]] = None

    jersey_number: Optional[float] = FieldInfo(alias="jerseyNumber", default=None)

    league_id: Optional[str] = FieldInfo(alias="leagueID", default=None)

    lookups: Optional[Lookups] = None

    names: Optional[Names] = None

    player_id: Optional[str] = FieldInfo(alias="playerID", default=None)

    player_teams: Optional[Dict[str, PlayerTeams]] = FieldInfo(alias="playerTeams", default=None)

    position: Optional[str] = None

    sport_id: Optional[str] = FieldInfo(alias="sportID", default=None)

    team_id: Optional[str] = FieldInfo(alias="teamID", default=None)
