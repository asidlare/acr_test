import re
from functools import wraps


def check_args(str_regexp: str):
    str_reg_compiled = re.compile(rf"{str_regexp}")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            resp = func(*args, **kwargs)

            # loop for args
            for arg_value in args:
                if isinstance(arg_value, str) and str_reg_compiled.findall(arg_value):
                    print(f'arg_value: {arg_value} for {str_regexp}')

            # loop for the keyword arguments
            for keyword_name, arg_value in kwargs.items():
                if isinstance(arg_value, str) and str_reg_compiled.findall(arg_value):
                    print(f'keyword_name: {keyword_name}, arg_value: {arg_value} for {str_regexp}')

            return resp
        return wrapper
    return decorator


@check_args(str_regexp='1')
def func1(str1: str, int1: int, str2: str, str3: str = None, str4: str = None):
    return ",".join([str1, str(int1), str2, str3, str4])


if __name__ == '__main__':
    res = func1('a1', 1, 'bc', str3='a7', str4='b1a')
    print(res)