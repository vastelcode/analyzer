# точка входа в приложение

# импорты
from core.config import prompts
from core.utils.helpers import prompt

from gui.app_gui import start_gui
from web.app_web import start_web

print('Welcome to Analyzer!')

def main():

    try:
        choice_mode_interface = prompt(**prompts['mode_interface'])

        if choice_mode_interface == 'cli':

            choice_mode_work = prompt(**prompts['mode_work'])
            # выбор типа поиска
            choice_type_search = prompt(**prompts['type_search'])

            main()

        elif choice_mode_interface == 'gui':
            start_gui()


        else:
            start_web()


    except Exception as exc:
        print(f'Analyzer Error: {exc}')

main()
