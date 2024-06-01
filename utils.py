from typing import Callable, Any

def save_to_file(file_path: str):
    def wrapper(func: Callable[[Any], str]):
        def inner(*args):
            with open(file_path, 'w', encoding='utf-8') as file:
                lines_to_write = func(*args)
                file.write(lines_to_write)
        return inner
    return wrapper