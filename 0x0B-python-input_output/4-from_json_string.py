#!/usr/bin/python3

import json


def from_json_string(my_str):
    """
    Returns the JSON representation of an object as a string.

    Args:
        my_obj: The object to be serialized.

    Returns:
        A string containing the JSON representation of the object.
    """
    return json.loads(my_str)
