import str_ops


def test_reverse_string():
    assert str_ops.reverse_string("hello") == "olleh"


def test_is_palindrome():
    assert str_ops.is_palindrome("A man a plan a canal Panama") is True
    assert str_ops.is_palindrome("hello") is False


def test_count_vowels():
    assert str_ops.count_vowels("hello world") == 3


def test_is_anagram():
    assert str_ops.is_anagram("listen", "silent") is True
    assert str_ops.is_anagram("hello", "world") is False


def test_snake_to_camel():
    assert str_ops.snake_to_camel("hello_world_example") == "helloWorldExample"


def test_camel_to_snake():
    assert str_ops.camel_to_snake("helloWorldExample") == "hello_world_example"


def test_truncate_string():
    assert str_ops.truncate_string("hello world", 5) == "hello..."


def test_levenshtein_distance():
    assert str_ops.levenshtein_distance("kitten", "sitting") == 3


def test_word_frequency():
    result = str_ops.word_frequency("the quick brown fox the lazy dog the")
    assert result["the"] == 3


def test_encode_decode_base64():
    encoded = str_ops.encode_base64("hello")
    assert str_ops.decode_base64(encoded) == "hello"
