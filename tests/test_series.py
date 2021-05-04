from math_series.series import fibonacci, lucas, sum_series


def test_fibonacci():
    input_values = 5
    actual = fibonacci(input_values)
    expected = 5
    assert actual == expected


def test_lucas():
    input_values = 7
    actual = lucas(input_values)
    expected = 29
    assert actual == expected


def test_sum_series_one():
    print_this = 4
    actual = sum_series(print_this)
    expected = 3
    assert actual == expected

def test_sum_series_two():
    print_this = 4
    actual = sum_series(print_this,2,1)
    expected = 7
    assert actual == expected