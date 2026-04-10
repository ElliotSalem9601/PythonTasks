# Установка pytest (если не установлен)
pip install pytest

# Запуск всех тестов
pytest 04_lesson/ -v

# Запуск с подробным выводом
pytest 04_lesson/test_string_utils.py -v

# Запуск с отчетом о покрытии (если установлен pytest-cov)
pip install pytest-cov
pytest 04_lesson/ --cov=string_utils