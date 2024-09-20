import unittest
from mood import predict_message_mood


class TestPredictMessageMood(unittest.TestCase):
    """Класс тестов для mood."""

    def test_default_thresholds(self):
        """Тест трешхолдов по умолчанию."""
        self.assertEqual(predict_message_mood("Чапаев и пустота"), "отл")
        self.assertEqual(predict_message_mood("Вулкан"), "норм")
        self.assertEqual(predict_message_mood("Это нормально"), "норм")


    def test_custom_thresholds(self):
        """Тест кастомных трешхолдов."""
        self.assertEqual(
            predict_message_mood("Чапаев и пустота", 0.8, 0.99), "норм"
        )
        self.assertEqual(
            predict_message_mood("Отлично выполнена работа", 0.5, 0.85), "отл"
        )
        self.assertEqual(
            predict_message_mood("Плохо справился", 0.3, 0.8), "неуд"
        )


if __name__ == "__main__":
    unittest.main()
