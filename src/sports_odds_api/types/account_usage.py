# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .rate_limit_interval import RateLimitInterval

__all__ = ["AccountUsage", "RateLimits"]


class RateLimits(BaseModel):
    per_day: Optional[RateLimitInterval] = FieldInfo(alias="per-day", default=None)

    per_hour: Optional[RateLimitInterval] = FieldInfo(alias="per-hour", default=None)

    per_minute: Optional[RateLimitInterval] = FieldInfo(alias="per-minute", default=None)

    per_month: Optional[RateLimitInterval] = FieldInfo(alias="per-month", default=None)

    per_second: Optional[RateLimitInterval] = FieldInfo(alias="per-second", default=None)


class AccountUsage(BaseModel):
    customer_id: Optional[str] = FieldInfo(alias="customerID", default=None)
    """The Stripe customer ID for the account"""

    email: Optional[str] = None
    """The email address associated with the account"""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)
    """Whether the API key is active"""

    key_id: Optional[str] = FieldInfo(alias="keyID", default=None)
    """The hashed identifier for the API key"""

    rate_limits: Optional[RateLimits] = FieldInfo(alias="rateLimits", default=None)

    tier: Optional[str] = None
    """The current subscription tier"""
