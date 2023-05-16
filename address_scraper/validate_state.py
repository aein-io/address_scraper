from states import states


def get_state_code(state):
    """
    Get the state abbreviation from the state name
    """
    code = None
    for abbrev, name in states.items():
        if name.lower() == state.lower() or abbrev.lower() == state.lower():
            code = abbrev
            break

    return code
