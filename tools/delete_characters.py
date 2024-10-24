import re
from collections import Counter

def delete_consecutive_recurring_characters(word: str) -> str:
    return re.sub(r'(.)\1+', r'\1', word)


def delete_recurring_characters(word: str) -> str:
    return "".join(dict.fromkeys(word))


def delete_non_unique_characters(word: str) -> str:
    seen = set()
    counts = Counter(word)
    output = ''
    for c in word:
        if c in seen:
            continue
        if counts[c] == 1:
            output += c
        seen.add(c)
    return output


if __name__ == '__main__':
    word1 = 'aaabbbcccddde'
    word2 = 'aaabbbcaccddde'
    print(delete_consecutive_recurring_characters(word1))
    print(delete_consecutive_recurring_characters(word2))

    word3 = 'abbaaccddec'
    print(delete_recurring_characters(word3))

    word4 = 'aabafeooc'
    word5 = 'abbaacdedc'
    print(delete_non_unique_characters(word4))
    print(delete_non_unique_characters(word5))
