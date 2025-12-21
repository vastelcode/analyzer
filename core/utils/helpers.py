from core.utils.mappers import map_term

def prompt(questionary, map_key, allowed, parameter):

    value = questionary.ask()
    value = map_term(value,map_key)

    if value not in allowed:

        raise Exception(f'{parameter} {value} temporarily unavailable')

    return value