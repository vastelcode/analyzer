"""
Модуль для красивого вывода текста в терминал с использованием ANSI-кодов.
Поддерживает цвета, начертания и предопределенные стили сообщений.
"""

from ...data.ansi_colors import ANSI_CODES


class StyledPrint:
    """
    Класс для стилизованного вывода текста в терминал.
    
    Attributes:
        config (dict): Конфигурация стилей (цвета и начертания).
        styles (dict): Предопределенные стили для различных типов сообщений.
    """
    
    
    def __init__(self):
        """
        Инициализация StyledPrint с конфигурацией стилей.
        
        Args:
            config (dict, optional): Пользовательская конфигурация стилей.
                                     Если не указана, используется стандартная.
        """

        self.config =  {
            'primary_color': ANSI_CODES['bright_cyan'],
            'secondary_color': ANSI_CODES['bright_blue'],
            'success_color': ANSI_CODES['bright_green'],
            'error_color': ANSI_CODES['bright_red'],
            'warning_color': ANSI_CODES['bright_yellow'],
            'info_color': ANSI_CODES['bright_white'],
            'text_color': ANSI_CODES['white'],
            'muted_color': ANSI_CODES['bright_black'],
            
            'bold': ANSI_CODES['bold'],
            'underline': ANSI_CODES['underline'],
            'italic': ANSI_CODES['italic'],
            'dim': ANSI_CODES['dim'],
            
            'reset': ANSI_CODES['reset'],
        }

        self._init_styles()
    
    
    def _init_styles(self):
        """Инициализирует предопределенные стили для различных типов сообщений."""
        c = self.config
        
        self.styles = {
            'header': f"{c['primary_color']}{c['bold']}",
            'subheader': f"{c['secondary_color']}{c['bold']}",
            'text': f"{c['text_color']}",
            'success': f"{c['success_color']}{c['bold']}",
            'error': f"{c['error_color']}{c['bold']}",
            'warning': f"{c['warning_color']}{c['bold']}",
            'info': f"{c['info_color']}{c['bold']}",
            'muted': f"{c['muted_color']}{c['dim']}",
            'highlight': f"{c['primary_color']}{c['bold']}",
            'bold': f"{c['bold']}",
            'underline': f"{c['underline']}",
            'italic': f"{c['italic']}",
        }
    
    def _format_text(self, text, style):
        """
        Форматирует текст с указанным стилем.
        
        Args:
            text (str): Текст для форматирования.
            style (str): Ключ стиля из self.styles.
            
        Returns:
            str: Отформатированная строка.
        """
        style_code = self.styles.get(style, '')
        return f"{style_code}{text}{self.config['reset']}"
    
    def print(self, text, style='text', is_print=True, end='\n', **kwargs):
        """
        Форматирует и/или выводит текст с указанным стилем.
        
        Args:
            text (str): Текст для вывода.
            style (str): Ключ стиля (по умолчанию 'text').
            is_print (bool): Если True, выводит текст. Если False, только возвращает.
            end (str): Символ конца строки (по умолчанию '\\n').
            **kwargs: Дополнительные аргументы для функции print.
            
        Returns:
            str: Отформатированная строка.
        """
        formatted_text = self._format_text(text, style)
        if is_print:
            print(formatted_text, end=end, **kwargs)
        return formatted_text
    
    # Основные методы для различных типов сообщений
    
    def header(self, text, is_print=True, **kwargs):
        """
        Форматирует и/или выводит заголовок.
        
        Args:
            text (str): Текст заголовка.
            is_print (bool): Если True, выводит текст.
            **kwargs: Дополнительные аргументы для print.
            
        Returns:
            str: Отформатированная строка.
        """
        return self.print(text, style='header', is_print=is_print, **kwargs)
    
    def subheader(self, text, is_print=True, **kwargs):
        """
        Форматирует и/или выводит подзаголовок.
        
        Args:
            text (str): Текст подзаголовка.
            is_print (bool): Если True, выводит текст.
            **kwargs: Дополнительные аргументы для print.
            
        Returns:
            str: Отформатированная строка.
        """
        return self.print(text, style='subheader', is_print=is_print, **kwargs)
    
    def text(self, text, is_print=True, **kwargs):
        """
        Форматирует и/или выводит обычный текст.
        
        Args:
            text (str): Текст для вывода.
            is_print (bool): Если True, выводит текст.
            **kwargs: Дополнительные аргументы для print.
            
        Returns:
            str: Отформатированная строка.
        """
        return self.print(text, style='text', is_print=is_print, **kwargs)
    
    def success(self, text, is_print=True, **kwargs):
        """
        Форматирует и/или выводит сообщение об успехе.
        
        Args:
            text (str): Текст сообщения.
            is_print (bool): Если True, выводит текст.
            **kwargs: Дополнительные аргументы для print.
            
        Returns:
            str: Отформатированная строка.
        """
        return self.print(' ✓ ' + text, style='success', is_print=is_print, **kwargs)
    
    def error(self, text, is_print=True, **kwargs):
        """
        Форматирует и/или выводит сообщение об ошибке.
        
        Args:
            text (str): Текст ошибки.
            is_print (bool): Если True, выводит текст.
            **kwargs: Дополнительные аргументы для print.
            
        Returns:
            str: Отформатированная строка.
        """
        return self.print(' ✗ ' + text, style='error', is_print=is_print, **kwargs)
    
    def warning(self, text, is_print=True, **kwargs):
        """
        Форматирует и/или выводит предупреждение.
        
        Args:
            text (str): Текст предупреждения.
            is_print (bool): Если True, выводит текст.
            **kwargs: Дополнительные аргументы для print.
            
        Returns:
            str: Отформатированная строка.
        """
        return self.print(' ⚠ ' + text, style='warning', is_print=is_print, **kwargs)
    
    def info(self, text, is_print=True, **kwargs):
        """
        Форматирует и/или выводит информационное сообщение.
        
        Args:
            text (str): Текст сообщения.
            is_print (bool): Если True, выводит текст.
            **kwargs: Дополнительные аргументы для print.
            
        Returns:
            str: Отформатированная строка.
        """
        return self.print(' ℹ ' + text, style='info', is_print=is_print, **kwargs)
    
    def muted(self, text, is_print=True, **kwargs):
        """
        Форматирует и/или выводит приглушенный/вторичный текст.
        
        Args:
            text (str): Текст для вывода.
            is_print (bool): Если True, выводит текст.
            **kwargs: Дополнительные аргументы для print.
            
        Returns:
            str: Отформатированная строка.
        """
        return self.print(text, style='muted', is_print=is_print, **kwargs)
    
    def highlight(self, text, is_print=True, **kwargs):
        """
        Форматирует и/или выводит выделенный текст.
        
        Args:
            text (str): Текст для выделения.
            is_print (bool): Если True, выводит текст.
            **kwargs: Дополнительные аргументы для print.
            
        Returns:
            str: Отформатированная строка.
        """
        return self.print(text, style='highlight', is_print=is_print, **kwargs)
    
    # Методы для форматирования
    
    def bold(self, text, is_print=True, **kwargs):
        """
        Форматирует и/или выводит жирный текст.
        
        Args:
            text (str): Текст для вывода.
            is_print (bool): Если True, выводит текст.
            **kwargs: Дополнительные аргументы для print.
            
        Returns:
            str: Отформатированная строка.
        """
        return self.print(text, style='bold', is_print=is_print, **kwargs)
    
    def underline(self, text, is_print=True, **kwargs):
        """
        Форматирует и/или выводит подчеркнутый текст.
        
        Args:
            text (str): Текст для вывода.
            is_print (bool): Если True, выводит текст.
            **kwargs: Дополнительные аргументы для print.
            
        Returns:
            str: Отформатированная строка.
        """
        return self.print(text, style='underline', is_print=is_print, **kwargs)
    
    def italic(self, text, is_print=True, **kwargs):
        """
        Форматирует и/или выводит курсивный текст.
        
        Args:
            text (str): Текст для вывода.
            is_print (bool): Если True, выводит текст.
            **kwargs: Дополнительные аргументы для print.
            
        Returns:
            str: Отформатированная строка.
        """
        return self.print(text, style='italic', is_print=is_print, **kwargs)
    
    # Составные методы
    
    def divider(self, char='=', length=60, is_print=True, **kwargs):
        """
        Форматирует и/или выводит разделительную линию.
        
        Args:
            char (str): Символ для заполнения линии.
            length (int): Длина линии.
            is_print (bool): Если True, выводит текст.
            **kwargs: Дополнительные аргументы для print.
            
        Returns:
            str: Отформатированная строка.
        """
        line = char * length
        return self.print(line, style='muted', is_print=is_print, **kwargs)
    
    def title(self, text, char='=', is_print=True, **kwargs):
        """
        Форматирует и/или выводит заголовок с разделительными линиями.
        
        Args:
            text (str): Текст заголовка.
            char (str): Символ для заполнения линий.
            is_print (bool): Если True, выводит текст.
            **kwargs: Дополнительные аргументы для print.
            
        Returns:
            tuple: (верхняя линия, заголовок, нижняя линия)
        """
        lines = []
        top_line = self.divider(char, len(text) + 4, is_print=is_print, **kwargs)
        lines.append(top_line)
        
        header_text = self.print(f"  {text}  ", style='header', is_print=is_print, **kwargs)
        lines.append(header_text)
        
        bottom_line = self.divider(char, len(text) + 4, is_print=is_print, **kwargs)
        lines.append(bottom_line)
        
        return '\n'.join(lines)
    
    def list_item(self, text, bullet='•', is_print=True, **kwargs):
        """
        Форматирует и/или выводит элемент списка.
        
        Args:
            text (str): Текст элемента.
            bullet (str): Маркер списка.
            is_print (bool): Если True, выводит текст.
            **kwargs: Дополнительные аргументы для print.
            
        Returns:
            str: Отформатированная строка.
        """
        return self.print(f"{bullet} {text}", style='text', is_print=is_print, **kwargs)
    
    def demo(self):
        """
        Демонстрация всех возможностей модуля.
        """
        # Использование с выводом
        self.title("Демонстрация StyledPrint", is_print=True)
       
        self.header("Основные типы сообщений:", is_print=True)
        self.success("Успешная операция завершена", is_print=True)
        self.error("Произошла ошибка!", is_print=True)
        self.warning("Внимание: важное предупреждение", is_print=True)
        self.info("Информационное сообщение", is_print=True)
    
        self.divider(is_print=True)
    
        self.subheader("Форматирование текста:", is_print=True)
        self.text("Обычный текст", is_print=True)
        self.bold("Жирный текст", is_print=True)
        self.italic("Курсивный текст", is_print=True)
        self.underline("Подчеркнутый текст", is_print=True)
        self.muted("Приглушенный текст", is_print=True)
        self.highlight("Выделенный текст", is_print=True)
    
        self.divider(is_print=True)
    
        self.subheader("Списки:", is_print=True)
        self.list_item("Первый элемент списка", is_print=True)
        self.list_item("Второй элемент списка", bullet='→', is_print=True)
        self.list_item("Третий элемент списка", bullet='✓', is_print=True)
        
        self.divider(is_print=True)


# Создаем глобальный экземпляр для удобства использования
styled_print = StyledPrint()