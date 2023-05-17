from inflection import camelize
from states import states


def is_camel(s: str) -> bool:
    return camelize(s) == s or camelize(s, False) == s


def split_camel(s: str) -> str:
    import re

    strings = re.sub('([A-Z][a-z]+)', r' \1',
                     re.sub('([A-Z]+)', r' \1', s)).split()

    return " ".join(strings)


def get_state_code(state: str):
    """
    Get the state abbreviation from the state name

    Args:
        state (str): The state input of the user.

    Returns:
        str: The state code.
    """
    code = None
    if len(state) > 2 and is_camel(state):
        state = split_camel(state)

    for abbrev, name in states.items():
        if name.lower() == state.lower() or abbrev.lower() == state.lower():
            code = abbrev
            break

    return code
