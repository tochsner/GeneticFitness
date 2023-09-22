from functools import partial
from typing import Callable

from .preprocessing import remove_non_functional, remove_non_significant


def preprocessing_factory(name: str, **kwargs) -> Callable:
    """Factory function for preprocessing functions."""
    if name == "remove_non_functional":
        return partial(remove_non_functional, **kwargs)
    elif name == "remove_non_significant":
        return partial(remove_non_significant, **kwargs)
    else:
        raise ValueError(f"Unknown preprocessing function {name}.")