import pytest
from string_utils import StringUtils


class TestStringUtils:
    """Класс для тестирования утилит работы со строками"""

    @pytest.fixture
    def utils(self):
        """Фикстура для создания экземпляра StringUtils"""
        return StringUtils()

    # ========== Тесты для метода capitilize ==========
    def test_capitilize_positive_normal_string(self, utils):
        """Позитивный тест: нормальная строка"""
        assert utils.capitilize("skypro") == "Skypro"
        assert utils.capitilize("hello world") == "Hello world"

    def test_capitilize_positive_already_capitalized(self, utils):
        """Позитивный тест: уже с заглавной буквы"""
        assert utils.capitilize("Skypro") == "Skypro"

    def test_capitilize_positive_with_numbers(self, utils):
        """Позитивный тест: строка с числами"""
        assert utils.capitilize("123abc") == "123abc"

    def test_capitilize_negative_empty_string(self, utils):
        """Негативный тест: пустая строка"""
        assert utils.capitilize("") == ""

    def test_capitilize_negative_string_with_spaces(self, utils):
        """Негативный тест: строка с пробелами в начале"""
        assert utils.capitilize("   hello") == "   hello"

    def test_capitilize_negative_none(self, utils):
        """Негативный тест: None (ожидаем ошибку)"""
        with pytest.raises(AttributeError):
            utils.capitilize(None)

    # ========== Тесты для метода trim ==========
    def test_trim_positive_no_spaces(self, utils):
        """Позитивный тест: строка без пробелов в начале"""
        assert utils.trim("hello") == "hello"

    def test_trim_positive_with_spaces(self, utils):
        """Позитивный тест: строка с пробелами в начале"""
        assert utils.trim("   hello") == "hello"
        assert utils.trim("  hello world  ") == "hello world  "

    def test_trim_positive_only_spaces(self, utils):
        """Позитивный тест: строка из одних пробелов"""
        assert utils.trim("   ") == ""

    def test_trim_negative_empty_string(self, utils):
        """Негативный тест: пустая строка"""
        assert utils.trim("") == ""

    def test_trim_negative_none(self, utils):
        """Негативный тест: None (ожидаем ошибку)"""
        with pytest.raises(AttributeError):
            utils.trim(None)

    # ========== Тесты для метода to_list ==========
    def test_to_list_positive_default_delimiter(self, utils):
        """Позитивный тест: разделитель по умолчанию (запятая)"""
        assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]

    def test_to_list_positive_custom_delimiter(self, utils):
        """Позитивный тест: пользовательский разделитель"""
        assert utils.to_list("1:2:3:4", ":") == ["1", "2", "3", "4"]
        assert utils.to_list("apple;orange;banana", ";") == ["apple", "orange", "banana"]

    def test_to_list_positive_with_spaces(self, utils):
        """Позитивный тест: строка с пробелами"""
        assert utils.to_list("a, b, c") == ["a", " b", " c"]

    def test_to_list_negative_empty_string(self, utils):
        """Негативный тест: пустая строка"""
        assert utils.to_list("") == []

    def test_to_list_negative_string_without_delimiter(self, utils):
        """Негативный тест: строка без разделителя"""
        assert utils.to_list("abc") == ["abc"]

    def test_to_list_negative_none(self, utils):
        """Негативный тест: None (ожидаем ошибку)"""
        with pytest.raises(AttributeError):
            utils.to_list(None)

    # ========== Тесты для метода contains ==========
    def test_contains_positive_symbol_exists(self, utils):
        """Позитивный тест: символ присутствует в строке"""
        assert utils.contains("SkyPro", "S") is True
        assert utils.contains("Hello", "e") is True

    def test_contains_positive_symbol_not_exists(self, utils):
        """Позитивный тест: символ отсутствует в строке"""
        assert utils.contains("SkyPro", "U") is False

    def test_contains_positive_with_numbers(self, utils):
        """Позитивный тест: строка с числами"""
        assert utils.contains("12345", "3") is True

    def test_contains_negative_empty_string(self, utils):
        """Негативный тест: пустая строка"""
        assert utils.contains("", "a") is False

    def test_contains_negative_empty_symbol(self, utils):
        """Негативный тест: пустой символ"""
        assert utils.contains("hello", "") is True  # пустая строка есть в любой строке

    def test_contains_negative_none(self, utils):
        """Негативный тест: None (ожидаем ошибку)"""
        with pytest.raises(TypeError):
            utils.contains(None, "a")

    # ========== Тесты для метода delete_symbol ==========
    def test_delete_symbol_positive_single_occurrence(self, utils):
        """Позитивный тест: удаление одного символа"""
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"

    def test_delete_symbol_positive_multiple_occurrences(self, utils):
        """Позитивный тест: удаление символа с несколькими вхождениями"""
        assert utils.delete_symbol("Hello World", "l") == "Heo Word"
        assert utils.delete_symbol("aaaaa", "a") == ""

    def test_delete_symbol_positive_symbol_not_exists(self, utils):
        """Позитивный тест: удаление отсутствующего символа"""
        assert utils.delete_symbol("SkyPro", "z") == "SkyPro"

    def test_delete_symbol_negative_empty_string(self, utils):
        """Негативный тест: пустая строка"""
        assert utils.delete_symbol("", "a") == ""

    def test_delete_symbol_negative_empty_symbol(self, utils):
        """Негативный тест: удаление пустого символа"""
        assert utils.delete_symbol("hello", "") == "hello"

    def test_delete_symbol_negative_none(self, utils):
        """Негативный тест: None (ожидаем ошибку)"""
        with pytest.raises(AttributeError):
            utils.delete_symbol(None, "a")

    # ========== Тесты для метода starts_with ==========
    def test_starts_with_positive_match(self, utils):
        """Позитивный тест: строка начинается с заданного символа"""
        assert utils.starts_with("SkyPro", "S") is True
        assert utils.starts_with("Hello", "H") is True

    def test_starts_with_positive_no_match(self, utils):
        """Позитивный тест: строка не начинается с заданного символа"""
        assert utils.starts_with("SkyPro", "P") is False

    def test_starts_with_positive_with_numbers(self, utils):
        """Позитивный тест: строка с числами"""
        assert utils.starts_with("12345", "1") is True

    def test_starts_with_negative_empty_string(self, utils):
        """Негативный тест: пустая строка"""
        assert utils.starts_with("", "a") is False

    def test_starts_with_negative_empty_symbol(self, utils):
        """Негативный тест: пустой символ"""
        assert utils.starts_with("hello", "") is True

    def test_starts_with_negative_none(self, utils):
        """Негативный тест: None (ожидаем ошибку)"""
        with pytest.raises(AttributeError):
            utils.starts_with(None, "a")

    # ========== Тесты для метода end_with ==========
    def test_end_with_positive_match(self, utils):
        """Позитивный тест: строка заканчивается заданным символом"""
        assert utils.end_with("SkyPro", "o") is True
        assert utils.end_with("Hello", "o") is True

    def test_end_with_positive_no_match(self, utils):
        """Позитивный тест: строка не заканчивается заданным символом"""
        assert utils.end_with("SkyPro", "P") is False

    def test_end_with_positive_with_numbers(self, utils):
        """Позитивный тест: строка с числами"""
        assert utils.end_with("12345", "5") is True

    def test_end_with_negative_empty_string(self, utils):
        """Негативный тест: пустая строка"""
        assert utils.end_with("", "a") is False

    def test_end_with_negative_empty_symbol(self, utils):
        """Негативный тест: пустой символ"""
        assert utils.end_with("hello", "") is True

    def test_end_with_negative_none(self, utils):
        """Негативный тест: None (ожидаем ошибку)"""
        with pytest.raises(AttributeError):
            utils.end_with(None, "a")

    # ========== Тесты для метода is_empty ==========
    def test_is_empty_positive_empty_string(self, utils):
        """Позитивный тест: пустая строка"""
        assert utils.is_empty("") is True

    def test_is_empty_positive_not_empty(self, utils):
        """Позитивный тест: не пустая строка"""
        assert utils.is_empty("hello") is False
        assert utils.is_empty(" ") is False

    def test_is_empty_positive_only_spaces(self, utils):
        """Позитивный тест: строка только из пробелов"""
        assert utils.is_empty("   ") is False  # ВНИМАНИЕ: потенциальный дефект!

    def test_is_empty_negative_none(self, utils):
        """Негативный тест: None (ожидаем ошибку)"""
        with pytest.raises(AttributeError):
            utils.is_empty(None)

    # ========== Тесты для метода list_to_string ==========
    def test_list_to_string_positive_default_joiner(self, utils):
        """Позитивный тест: разделитель по умолчанию"""
        assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"

    def test_list_to_string_positive_custom_joiner(self, utils):
        """Позитивный тест: пользовательский разделитель"""
        assert utils.list_to_string(["a", "b", "c"], "-") == "a-b-c"
        assert utils.list_to_string(["apple", "banana"], "; ") == "apple; banana"

    def test_list_to_string_positive_empty_list(self, utils):
        """Позитивный тест: пустой список"""
        assert utils.list_to_string([]) == ""

    def test_list_to_string_positive_single_element(self, utils):
        """Позитивный тест: список с одним элементом"""
        assert utils.list_to_string(["hello"]) == "hello"

    def test_list_to_string_positive_with_numbers(self, utils):
        """Позитивный тест: список с числами"""
        assert utils.list_to_string([1, 2, 3], "|") == "1|2|3"

    def test_list_to_string_negative_none(self, utils):
        """Негативный тест: None вместо списка"""
        with pytest.raises(AttributeError):
            utils.list_to_string(None)