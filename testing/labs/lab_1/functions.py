def check_number(value):
    if not value.lstrip("-").isdigit():
        raise ValueError("Потрібно ввести ціле число")
    number = int(value)
    assert number > 0, "Число має бути більшим за нуль!"
    return number


def count_symbols(text: str) -> int:
    return len(text)


def divide(a, b):
    return a / b


def count_vowels(text: str) -> int:
    count = 0
    for ch in text.lower():
        if ch in "aeiouаеєиіїоуюя":
            count += 1
    return count


def ask_number():
    value = input("Введіть число: ")
    return check_number(value)


if __name__ == "__main__":
    print(check_number(input("Введіть число: ")))
