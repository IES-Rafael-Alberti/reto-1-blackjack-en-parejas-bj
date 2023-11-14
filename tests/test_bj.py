import pytest
from src.bj import valorCarta

@pytest.mark.parametrize(
    "carta, total, expected",
    [
        ("5",10,5),
        ("A",12,1),
        ("A",11,10),
        ("0",23,10)
        
    ]
)
def test_valorCarta(carta, total, expected):
    assert valorCarta(carta, total) == expected