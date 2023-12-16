from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

    from something import asdf


def func() -> Callable[[Callable[_P, _R]], Callable[_P, _R]]:
    """Factory for decorators which caches locally using pickles."""
