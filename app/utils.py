from typing import Dict, Any, Optional


def flatten_json(
    data: Dict[str, Any],
    parent_key: str = "",
    sep: str = "_",
    result: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:

    if result is None:
        result = {}

    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key

        if isinstance(value, dict):
            flatten_json(value, new_key, sep, result)
        else:
            result[new_key] = value

    return result

