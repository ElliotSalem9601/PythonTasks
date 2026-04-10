class StringUtils:
    """
    Класс с полезными утилитами для обработки строк.
    """

    def capitilize(self, string: str) -> str:
        """
        Принимает на вход строку, возвращает ее же, но с заглавной первой буквой.
        """
        return string.capitalize()

    def trim(self, string: str) -> str:
        """
        Принимает на вход строку и удаляет все пробелы в начале строки.
        """
        whitespace = " "
        while string.startswith(whitespace):
            string = string.removeprefix(whitespace)
        return string

    def to_list(self, string: str, delimeter=",") -> list:
        """
        Принимает на вход строку с разделителем и возвращает список из элементов.
        """
        if self.is_empty(string):
            return []

        return string.split(delimeter)

    def contains(self, string: str, symbol: str) -> bool:
        """
        Возвращает True, если строка содержит искомый символ и False - если нет.
        """
        return symbol in string

    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет все подстроки из переданной строки.
        """
        return string.replace(symbol, "")

    def starts_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает True, если строка начинается с заданного символа и False - если нет.
        """
        return string.startswith(symbol)

    def end_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает True, если строка заканчивается заданным символом и False - если нет.
        """
        return string.endswith(symbol)

    def is_empty(self, string: str) -> bool:
        """
        Возвращает True, если строка пустая и False - если нет.
        """
        return string == ""

    def list_to_string(self, lst: list, joiner=", ") -> str:
        """
        Преобразует список элементов в строку с указанным разделителем.
        """
        return joiner.join(lst)