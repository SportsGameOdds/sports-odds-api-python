# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventGetParams"]


class EventGetParams(TypedDict, total=False):
    bookmaker_id: Annotated[str, PropertyInfo(alias="bookmakerID")]
    """A bookmakerID or comma-separated list of bookmakerIDs to include odds for"""

    cancelled: bool
    """
    Only include cancelled Events (true), only non-cancelled Events (false) or all
    Events (omit)
    """

    cursor: str
    """The cursor for the request.

    Used to get the next group of Events. This should be the nextCursor from the
    prior response.
    """

    ended: bool
    """
    Only include Events which have have ended (true), only Events which have not
    ended (false) or all Events (omit)
    """

    event_id: Annotated[str, PropertyInfo(alias="eventID")]
    """An eventID to get Event data for"""

    event_ids: Annotated[str, PropertyInfo(alias="eventIDs")]
    """A comma separated list of eventIDs to get Event data for"""

    finalized: bool
    """
    Only include finalized Events (true), exclude unfinalized Events (false) or all
    Events (omit)
    """

    include_alt_lines: Annotated[bool, PropertyInfo(alias="includeAltLines")]
    """Whether to include alternate lines in the odds byBookmaker data"""

    include_opposing_odds: Annotated[bool, PropertyInfo(alias="includeOpposingOdds")]
    """Whether to include opposing odds for each included oddID"""

    league_id: Annotated[str, PropertyInfo(alias="leagueID")]
    """A leagueID or comma-separated list of leagueIDs to get Events for"""

    limit: float
    """The maximum number of Events to return"""

    live: bool
    """
    Only include live Events (true), only non-live Events (false) or all Events
    (omit)
    """

    odd_id: Annotated[str, PropertyInfo(alias="oddID")]
    """An oddID or comma-separated list of oddIDs to include odds for"""

    odds_available: Annotated[bool, PropertyInfo(alias="oddsAvailable")]
    """
    Whether you want only Events which do (true) or do not (false) have odds markets
    which are currently available (open for wagering)
    """

    odds_present: Annotated[bool, PropertyInfo(alias="oddsPresent")]
    """
    Whether you want only Events which do (true) or do not (false) have any
    associated odds markets regardless of whether those odds markets are currently
    available (open for wagering)
    """

    player_id: Annotated[str, PropertyInfo(alias="playerID")]
    """
    A playerID or comma-separated list of playerIDs to include Events (and
    associated odds) for
    """

    sport_id: Annotated[str, PropertyInfo(alias="sportID")]
    """A sportID or comma-separated list of sportIDs to get Events for"""

    started: bool
    """
    Only include Events which have have previously started (true), only Events which
    have not previously started (false) or all Events (omit)
    """

    starts_after: Annotated[Union[str, datetime], PropertyInfo(alias="startsAfter", format="iso8601")]
    """Get Events that start after this date"""

    starts_before: Annotated[Union[str, datetime], PropertyInfo(alias="startsBefore", format="iso8601")]
    """Get Events that start before this date"""

    team_id: Annotated[str, PropertyInfo(alias="teamID")]
    """A teamID or comma-separated list of teamIDs to include Events for"""

    type: str
    """Only include Events of the specified type"""
