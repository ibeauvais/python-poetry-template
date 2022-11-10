from src.main import hello


def test_hello():
    # Given
    value = "world"

    # When
    result = hello(value)

    # Then
    assert result == "hello world"
