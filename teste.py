import pytest
from view import calculate_interest

@pytest.mark.parametrize("principal, rate, time, expected_interest", [
    (1000, 5, 1, 50),
    (2000, 10, 2, 400),
    # Adicione mais casos de teste conforme necessário
])
def test_calculate_interest(principal, rate, time, expected_interest):
    interest = calculate_interest(principal, rate, time)
    assert interest == expected_interest