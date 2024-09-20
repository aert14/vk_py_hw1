class SomeModel:
    """Пример класса модели."""

    def predict(self, message: str) -> float:
        """
        Метод предсказания настроения сообщения.
        """
        if "отлично" in message.lower():
            return 0.9
        if "пустота" in message.lower():
            return 0.85
        if "плохо" in message.lower():
            return 0.2
        return 0.5



def predict_message_mood(
    message: str,
    bad_threshold: float = 0.3,
    good_threshold: float = 0.8,
) -> str:
    """
    Оценивает настроение сообщения на основе порогов хорошести.

    :param message: Текст сообщения.
    :param bad_threshold: Порог для классификации как "неуд".
    :param good_threshold: Порог для классификации как "отл".
    :return: "неуд", "отл" или "норм".
    """
    model = SomeModel()
    prediction = model.predict(message)

    if prediction < bad_threshold:
        return "неуд"
    if prediction > good_threshold:
        return "отл"
    return "норм"
