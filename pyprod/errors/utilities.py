from typing import Any

def handle_none_value(value: Any) -> None:
    if value is None:
        raise ValueError(message="None value provided")
    return None

def handle_none_values(values: list[Any]) -> None:
    if not any(values):
        raise ValueError(message="None value provided")
    
    return None