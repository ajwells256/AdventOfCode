from re import match
from typing import Union

def first_match(pattern: str, source:str) -> Union[str, None]:
    m = match(f"^.*?({pattern}).*$", source)
    return m.group(1) if m is not None else None

def last_match(pattern: str, source:str) -> Union[str, None]:
    m = match(f"^.*?({pattern}).*$", source)
    return m.group(1) if m is not None else None


