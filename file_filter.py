from typing import List, Union, Iterator
import io
from contextlib import ExitStack

def filtered_lines(
    file: Union[str, io.TextIOBase],
    search_words: List[str],
    stop_words: List[str],
) -> Iterator[str]:
    """
    Генератор, возвращающий строки из файла, содержащие хотя бы одно слово
    из search_words и не содержащие ни одного слова из stop_words.
    """
    search_set = set(word.lower() for word in search_words)
    stop_set = set(word.lower() for word in stop_words)

    with ExitStack() as stack:
        if isinstance(file, str):
            file_obj = stack.enter_context(open(file, "r", encoding="utf-8"))
        else:
            file_obj = file

        for line in file_obj:
            words = set(word.lower() for word in line.strip().split())
            if words & stop_set:
                continue
            if words & search_set:
                # Удаляем лишние пробелы в начале и конце строки
                yield line.strip()
