import questionary

from ..config import available_modes_interface, available_modes_work, available_types_search

# опросы
questionary_modes_interface = questionary.select(
"Выберите режим взаимодействия:",
choices=[
    'консольный интерфейс',
    'графический интерфейс',
    'веб-интерфейс'
],
qmark="?",
pointer=" > "
)

questionary_modes_work = questionary.select(
"Выберите режим работы:",
choices=[
    'анализ файлов',
    'веб-анализ'
],
qmark="?",
pointer=" > "
)

questionary_type_seacrh = questionary.select(
    "Выберите тип анализа",
    choices=[
        'глубокий',
        'поверхностный'
    ],
    qmark="?",
    pointer=" > "
)

prompts = {
    'mode_interface': {
        'questionary': questionary_modes_interface,
        'map_key': 'mode_interface',
        'allowed': available_modes_interface,
        'parameter':'Mode'
    },
    'mode_work': {
        'questionary': questionary_modes_work,
        'map_key': 'mode_work',
        'allowed': available_modes_work,
        'parameter': 'Mode'
    },
    'type_search': {
        'questionary': questionary_type_seacrh,
        'map_key': 'type_search',
        'allowed': available_types_search,
        'parameter': 'Type'
    },
}