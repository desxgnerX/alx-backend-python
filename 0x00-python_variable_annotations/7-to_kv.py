#!/usr/bin/env python3
"""
Type-annotated function to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a string and an int/float to a tuple.

    The first element of the tuple is the string k.
    The second element is the square of the int/float v as a float.

    Args:
        k (str): The string element.
        v (Union[int, float]): The int or float element.

    Returns:
        Tuple[str, float]: A tuple containing the string k and the square of v
        as a float.
    """
    return k, float(v ** 2)
