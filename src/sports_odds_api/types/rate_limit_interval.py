# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RateLimitInterval"]


class RateLimitInterval(BaseModel):
    current_entities: Optional[int] = FieldInfo(alias="current-entities", default=None)
    """Current number of entities accessed in the interval"""

    current_requests: Optional[int] = FieldInfo(alias="current-requests", default=None)
    """Current number of requests made in the interval"""

    max_entities: Union[Literal["unlimited"], int, None] = FieldInfo(alias="max-entities", default=None)
    """Maximum allowed entity accesses in the interval"""

    max_requests: Union[Literal["unlimited"], int, None] = FieldInfo(alias="max-requests", default=None)
    """Maximum allowed requests in the interval"""
