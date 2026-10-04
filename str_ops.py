"""
str_ops.py - A collection of string manipulation utility functions.

Written for Python 3.9. Uses typing.List/Dict/Optional in the
pre-3.10 style.
"""
import base64
import hashlib
import string
from typing import Dict, List, Optional


def reverse_string(text: str) -> str:
    """Return the input string reversed."""
    return text[::-1]


def is_palindrome(text: str) -> bool:
    """Return True if text reads the same forwards and backwards (case-insensitive)."""
    normalized = "".join(char.lower() for char in text if char.isalnum())
    return normalized == normalized[::-1]


def to_uppercase(text: str) -> str:
    """Return text converted to uppercase."""
    return text.upper()


def to_lowercase(text: str) -> str:
    """Return text converted to lowercase."""
    return text.lower()


def to_titlecase(text: str) -> str:
    """Return text converted to title case."""
    return text.title()


def swap_case(text: str) -> str:
    """Return text with uppercase and lowercase letters swapped."""
    return text.swapcase()


def count_vowels(text: str) -> int:
    """Return the number of vowels in text."""
    return sum(1 for char in text.lower() if char in "aeiou")


def count_consonants(text: str) -> int:
    """Return the number of consonants in text."""
    return sum(1 for char in text.lower() if char.isalpha() and char not in "aeiou")


def count_words(text: str) -> int:
    """Return the number of whitespace-separated words in text."""
    return len(text.split())


def count_characters(text: str) -> int:
    """Return the total number of characters in text."""
    return len(text)


def remove_whitespace(text: str) -> str:
    """Return text with all whitespace characters removed."""
    return "".join(text.split())


def remove_punctuation(text: str) -> str:
    """Return text with all punctuation characters removed."""
    return "".join(char for char in text if char not in string.punctuation)


def is_anagram(first: str, second: str) -> bool:
    """Return True if first and second are anagrams of each other."""
    normalize = lambda value: sorted(value.lower().replace(" ", ""))
    return normalize(first) == normalize(second)


def longest_word(text: str) -> str:
    """Return the longest word in text."""
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)


def shortest_word(text: str) -> str:
    """Return the shortest word in text."""
    words = text.split()
    if not words:
        return ""
    return min(words, key=len)


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of every word in text."""
    return " ".join(word.capitalize() for word in text.split())


def snake_to_camel(text: str) -> str:
    """Convert a snake_case string to camelCase."""
    parts = text.split("_")
    return parts[0] + "".join(part.capitalize() for part in parts[1:])


def camel_to_snake(text: str) -> str:
    """Convert a camelCase string to snake_case."""
    result = []
    for index, char in enumerate(text):
        if char.isupper() and index != 0:
            result.append("_")
        result.append(char.lower())
    return "".join(result)


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to max_length characters, appending suffix if truncated."""
    if len(text) <= max_length:
        return text
    return text[:max_length].rstrip() + suffix


def pad_string(text: str, width: int, fill_char: str = " ", align: str = "left") -> str:
    """Pad text to the given width using fill_char, aligned left/right/center."""
    if align == "left":
        return text.ljust(width, fill_char)
    if align == "right":
        return text.rjust(width, fill_char)
    if align == "center":
        return text.center(width, fill_char)
    raise ValueError("align must be 'left', 'right', or 'center'")


def repeat_string(text: str, times: int) -> str:
    """Repeat text the given number of times."""
    return text * times


def find_substring(text: str, substring: str) -> int:
    """Return the index of the first occurrence of substring in text, or -1."""
    return text.find(substring)


def find_all_occurrences(text: str, substring: str) -> List[int]:
    """Return the indices of every occurrence of substring in text."""
    indices = []
    start = 0
    while True:
        index = text.find(substring, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1
    return indices


def replace_substring(text: str, old: str, new: str) -> str:
    """Replace every occurrence of old with new in text."""
    return text.replace(old, new)


def split_string(text: str, delimiter: Optional[str] = None) -> List[str]:
    """Split text by the given delimiter (or whitespace if None)."""
    return text.split(delimiter)


def join_strings(parts: List[str], delimiter: str = "") -> str:
    """Join a list of strings using the given delimiter."""
    return delimiter.join(parts)


def strip_string(text: str, chars: Optional[str] = None) -> str:
    """Strip leading and trailing characters (or whitespace if None) from text."""
    return text.strip(chars)


def is_numeric(text: str) -> bool:
    """Return True if text consists only of digits."""
    return text.isdigit()


def is_alpha(text: str) -> bool:
    """Return True if text consists only of alphabetic characters."""
    return text.isalpha()


def is_alphanumeric(text: str) -> bool:
    """Return True if text consists only of alphanumeric characters."""
    return text.isalnum()


def char_frequency(text: str) -> Dict[str, int]:
    """Return a mapping of each character in text to its occurrence count."""
    frequency: Dict[str, int] = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


def most_common_char(text: str) -> Optional[str]:
    """Return the most frequently occurring character in text."""
    if not text:
        return None
    frequency = char_frequency(text)
    return max(frequency, key=frequency.get)


def remove_duplicate_chars(text: str) -> str:
    """Remove duplicate characters from text, preserving first occurrence order."""
    seen = set()
    result = []
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)


def string_to_list(text: str) -> List[str]:
    """Convert a string to a list of its characters."""
    return list(text)


def list_to_string(chars: List[str]) -> str:
    """Convert a list of characters (or strings) to a single string."""
    return "".join(chars)


def encode_base64(text: str) -> str:
    """Encode a string as base64."""
    return base64.b64encode(text.encode("utf-8")).decode("ascii")


def decode_base64(encoded: str) -> str:
    """Decode a base64-encoded string."""
    return base64.b64decode(encoded.encode("ascii")).decode("utf-8")


def compute_hash(text: str, algorithm: str = "sha256") -> str:
    """Return the hex digest of text using the given hash algorithm."""
    hasher = hashlib.new(algorithm)
    hasher.update(text.encode("utf-8"))
    return hasher.hexdigest()


def mask_string(text: str, visible_chars: int = 4, mask_char: str = "*") -> str:
    """Mask all but the last `visible_chars` characters of text."""
    if len(text) <= visible_chars:
        return mask_char * len(text)
    return mask_char * (len(text) - visible_chars) + text[-visible_chars:]


def levenshtein_distance(first: str, second: str) -> int:
    """Return the Levenshtein (edit) distance between two strings."""
    if len(first) < len(second):
        return levenshtein_distance(second, first)
    if len(second) == 0:
        return len(first)
    previous_row = list(range(len(second) + 1))
    for i, first_char in enumerate(first):
        current_row = [i + 1]
        for j, second_char in enumerate(second):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (first_char != second_char)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]


def word_frequency(text: str) -> Dict[str, int]:
    """Return a mapping of each word in text to its occurrence count."""
    frequency: Dict[str, int] = {}
    for word in text.lower().split():
        cleaned = word.strip(string.punctuation)
        if cleaned:
            frequency[cleaned] = frequency.get(cleaned, 0) + 1
    return frequency


def starts_with(text: str, prefix: str) -> bool:
    """Return True if text starts with prefix."""
    return text.startswith(prefix)


def ends_with(text: str, suffix: str) -> bool:
    """Return True if text ends with suffix."""
    return text.endswith(suffix)


def contains_substring(text: str, substring: str) -> bool:
    """Return True if substring is contained in text."""
    return substring in text
