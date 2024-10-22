import pytest

from tools.delete_characters import (
    delete_consecutive_recurring_characters,
    delete_recurring_characters,
    delete_non_unique_characters
)


@pytest.mark.parametrize(
    'test_string,expected_result',
    [('aaabbbcccddde', 'abcde'),
    ('aaabbbcaccddde', 'abcacde')]
)
def test_delete_cosecutive_recurring_characters(test_string, expected_result):
    assert delete_consecutive_recurring_characters(test_string) == expected_result


@pytest.mark.parametrize(
    'test_string,expected_result',
    [('abbaaccddec', 'abcde'),
     ('aabfggaacb', 'abfgc')]
)
def test_delete_recurring_characters(test_string, expected_result):
    assert delete_recurring_characters(test_string) == expected_result


@pytest.mark.parametrize(
    'test_string,expected_result',
    [('aabafeooc', 'bfec'),
     ('abbaacdedc', 'e')]
)
def test_delete_non_unique_characters(test_string, expected_result):
    assert delete_non_unique_characters(test_string) == expected_result
