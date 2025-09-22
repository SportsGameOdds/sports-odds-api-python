# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .event import Event
from .._models import BaseModel

__all__ = ["StreamEventsResponse", "PusherOptions", "PusherOptionsChannelAuthorization"]


class PusherOptionsChannelAuthorization(BaseModel):
    endpoint: Optional[str] = None

    headers: Optional[Dict[str, str]] = None


class PusherOptions(BaseModel):
    channel_authorization: Optional[PusherOptionsChannelAuthorization] = FieldInfo(
        alias="channelAuthorization", default=None
    )

    cluster: Optional[str] = None

    http_host: Optional[str] = FieldInfo(alias="httpHost", default=None)

    http_port: Optional[int] = FieldInfo(alias="httpPort", default=None)

    https_port: Optional[int] = FieldInfo(alias="httpsPort", default=None)

    ws_host: Optional[str] = FieldInfo(alias="wsHost", default=None)

    ws_port: Optional[int] = FieldInfo(alias="wsPort", default=None)

    wss_port: Optional[int] = FieldInfo(alias="wssPort", default=None)


class StreamEventsResponse(BaseModel):
    channel: Optional[str] = None

    data: Optional[List[Event]] = None

    pusher_key: Optional[str] = FieldInfo(alias="pusherKey", default=None)

    pusher_options: Optional[PusherOptions] = FieldInfo(alias="pusherOptions", default=None)

    success: Optional[bool] = None

    user: Optional[str] = None
