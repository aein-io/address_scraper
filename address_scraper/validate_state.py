from states import states


def get_state_code(state: str):
    """
    Get the state abbreviation from the state name

    Args:
        state (str): The state input of the user.

    Returns:
        str: The state code.
    """
    code = None
    for abbrev, name in states.items():
        if name.lower() == state.lower() or abbrev.lower() == state.lower():
            code = abbrev
            break

    return code
