#!/usr/bin/python3
"""Module that defines a class_to_json function."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    Args:
        obj: an instance of a class whose attributes are all
            serializable (list, dict, str, int, bool).

    Returns:
        dict: the object's attribute dictionary.
    """
    return obj.__dict__
