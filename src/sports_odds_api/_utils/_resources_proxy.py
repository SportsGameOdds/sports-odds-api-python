from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `sports_odds_api.resources` module.

    This is used so that we can lazily import `sports_odds_api.resources` only when
    needed *and* so that users can just import `sports_odds_api` and reference `sports_odds_api.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("sports_odds_api.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
