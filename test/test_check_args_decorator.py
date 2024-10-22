from tools.check_args_decorator import func1


def test_check_args_decorator(capfd):
    func_res = func1('a1', 1, 'bc', str3='a7', str4='b1a')

    assert func_res == 'a1,1,bc,a7,b1a'

    out, _ = capfd.readouterr()

    output_data = out.splitlines()
    assert output_data[0] == 'arg_value: a1 for 1'
    assert output_data[1] == 'keyword_name: str4, arg_value: b1a for 1'
