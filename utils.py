# utils.py

def is_palindrome(text: str) -> bool:
    """
    Check whether a given text is a palindrome.
    Ignores case and non-alphanumeric characters.
    """
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def count_words(text: str) -> int:
    """
    Count the number of words in a given text.
    Words are separated by whitespace.
    """
    words = text.split()
    return len(words)


def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius temperature to Fahrenheit.
    Formula: (C × 9/5) + 32
    """
    return (celsius * 9/5) + 32
