struct1 = {
    "a": [],
    "b": ["a"],
    "c": [],
    "d": ["c", "b"],
    "e": ["a", "d"],
    "f": ["a", "f"],
    "g": ["d", "h"],
    "h": ["a", "g"],
    "i": ["h", "a"],
    "k": ["a", "z"]
}

'''
Implement a function which for given item returns ordered list of items it depends on.
For example:
     +-------------+-------------------+
     | input       | output            |
     +-------------+-------------------+
     | a           | []                |
     | b           | a                 |
     | c           | []                |
     | d           | c, a, b           |
     | e           | a, c, b, d        |
     | f           | ?                 |
     | g           | ?                 |
     | h           | ?                 |
     | i           | ?                 |
     | k           | ?                 |
     +-------------+-------------------+
'''


def ordered_list_of_items_depends_on(struct: dict, item: str) -> list:
    if item not in struct:
        raise ValueError(f"{item} not in struct")
    output_struct = {}
    for key, values in struct.items():
        if item in output_struct:
            return output_struct[item] if not output_struct[item] else list(dict.fromkeys(output_struct[item]))
        output_struct[key] = []
        for val in values:
            if val in output_struct:
                output_struct[key].extend(output_struct[val])
                output_struct[key].append(val)
            else:
                raise ValueError(f"{val} does not exist in output")


if __name__ == '__main__':
    output = ordered_list_of_items_depends_on(struct1, 'a')
    print('a', output)
    output = ordered_list_of_items_depends_on(struct1, 'b')
    print('b', output)
    output = ordered_list_of_items_depends_on(struct1, 'd')
    print('d', output)
    output = ordered_list_of_items_depends_on(struct1, 'e')
    print('e', output)
    output = ordered_list_of_items_depends_on(struct1, 'f')
    print('f', output)
    output = ordered_list_of_items_depends_on(struct1, 'g')
    print('g', output)
