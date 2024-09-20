import io
import unittest
from file_filter import filtered_lines


class TestFilteredLines(unittest.TestCase):
    """
    Тесты функции filtered_lines.
    """

    def setUp(self):
        """
        Инициализация примера файла с тестовым содержимым.
        """
        self.sample_content = """а Роза упала на лапу Азора
        Великолепный день сегодня
        Плохая погода
        Чапаев и пустота
        Отлично справился
        Вулкан
        Розан"""



        self.file = io.StringIO(self.sample_content)

    def test_filtered_lines_basic(self):
        """
        Тест базового сценария.
        """
        search_words = ["роза", "вулкан", "чапаев"]
        stop_words = ["азора", "плохая"]

        expected = ["Чапаев и пустота", "Вулкан"]

        result = list(filtered_lines(self.file, search_words, stop_words))
        self.assertEqual(result, expected)

    def test_no_matches(self):
        """
        Тест на отсутствие совпадений.
        """
        search_words = ["нет", "совпадений"]
        stop_words = ["игнорировать"]

        result = list(filtered_lines(self.file, search_words, stop_words))
        self.assertEqual(result, [])

    def test_all_stop_words(self):
        """
        Тест на полное совпадение со стоп-словами.
        """
        search_words = ["роза", "вулкан", "чапаев"]
        stop_words = ["азора", "чапаев", "вулкан"]

        result = list(filtered_lines(self.file, search_words, stop_words))
        self.assertEqual(result, [])

    def test_case_insensitivity(self):
        """
        Тест нечувствительности к регистру: поиск должен игнорировать регистр
        как для слов поиска, так и для стоп-слов.
        """
        search_words = ["РОЗА", "ВУЛКАН", "ЧАПАЕВ"]
        stop_words = ["АЗОРА", "ПЛОХАЯ"]

        expected = ["Чапаев и пустота", "Вулкан"]

        # Сброс позиции файла для повторного чтения
        self.file.seek(0)
        result = list(filtered_lines(self.file, search_words, stop_words))
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
