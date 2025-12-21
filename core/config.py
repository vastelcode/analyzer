import questionary


# доступные режимы взаимодействия
available_modes_interface = ['cli','gui','web']

# порт по умолчанию
port = 3000

# разрешенные расширения файлов
extensions =  [
    # Исходные
    'txt', 'md', 'py', 'js', 'ts', 'html', 'css','tsx','jsx'

    # Конфигурационные файлы
    'json', 'yaml', 'yml', 'xml', 'toml', 'ini', 'cfg', 'conf',

    # Веб и шаблоны
    'jsx', 'tsx', 'vue', 'svelte', 'php', 'asp', 'aspx', 'jsp',
    'ejs', 'twig', 'jinja', 'jinja2', 'haml', 'pug',

    # Стили и разметка
    'scss', 'sass', 'less', 'stylus', 'styl',
    'xml', 'svg', 'xsl', 'xslt',

    # Языки программирования
    'java', 'c', 'cpp', 'h', 'hpp', 'cs', 'go', 'rs', 'rb',
    'pl', 'pm', 'lua', 'swift', 'kt', 'scala', 'groovy',
    'r', 'm', 'dart', 'elm', 'clj', 'ex', 'exs', 'hs',

    # Сценарные языки
    'sh', 'bash', 'zsh', 'ps1', 'bat', 'cmd', 'vbs',


    # Документация
    'rst', 'tex', 'bib', 'org', 'wiki', 'adoc', 'asciidoc',

    # Другие текстовые форматы
    'log', 'env', 'gitignore', 'dockerignore', 'editorconfig',
    'markdown', 'mkd', 'rtf', 'properties', 'cfg', 'prefs',

    # Сериализация
    'jsonl', 'ndjson', 'json5',

    # Мета и системные
    'lock', 'toml', 'xml', 'iml', 'project', 'classpath'
]

# доступные режимы работы
available_modes_work = ['fs','web']

# доступные типы поиска

available_types_search = ['deep','shallow']

# папки-исключения
exception_folders = ['node_modules']



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

