from collections.abc import Callable
from functools import wraps
from inspect import signature
from pathlib import Path
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def check_for_ext(func: Callable[P, T]) -> Callable[P, T]:
    sig = signature(func)

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        if "file_path" in bound.arguments:
            file_path = bound.arguments["file_path"]
        else:
            raise ValueError("Was not able to find path to file in func arguments.")

        if not isinstance(file_path, Path):
            file_path = Path(file_path)

        if file_path.suffix.lower() == ".csv":
            return func(*args, **kwargs)
        else:
            raise ValueError(
                f"The file has {file_path.suffix.lower()}, expected '.csv'."
            )

    return wrapper
