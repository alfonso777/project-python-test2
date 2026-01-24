from mycode import inc

def test_failed_answer():
    result = inc(7)
    print(f"Result: {result}")
    assert result == 8


def test_answer():
    assert inc(4) == 5
