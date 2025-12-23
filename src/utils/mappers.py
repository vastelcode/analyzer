from ..data.ready_regex import ready_regex
from re import compile


# объекты для сопоставления

modes_interface = {
    'консольный интерфейс': 'cli',
    'веб-интерфейс': 'web',
    'графический интерфейс': 'gui'
}

modes_work = {
    'анализ файлов': 'fs',
    'веб-анализ':'web'
}

types_search = {
    'глубокий': 'deep',
    'поверхностный': 'shallow'
}

terms = {
    'mode_interface': modes_interface,
    'mode_work': modes_work,
    'type_search': types_search
}


# функция для сопоставления термина из соответствующего набора

def map_term(term, set):

    if set not in terms:

        raise Exception(f'There is no such set of terms {set}')

    else:

        set = terms[set]

        if term not in set:

            raise Exception(f'There is no such term, like {term} in {set} ')

        else:

            return set[term]

# функция для поиска и перевода готовых, регулярных выражений

def map_regex(list_regex):

    for index,regex in enumerate(list_regex):
        
        # есть есть в готовых
        if regex in ready_regex:
            # заменяем на шаблон
            list_regex[index] = ready_regex[regex]
        
        else:
            regex = compile(regex)
    
    return list_regex