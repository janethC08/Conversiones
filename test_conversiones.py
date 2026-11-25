import pytest
import Conversion as con


def test_pulgadas_cm():
    assert con.centimetrosApulgadas(5.08) == 2
    assert con.pulgadasAcentimetros(2) == 5.08


def test_pies_metros():
    assert con.pies_a_metros(5) == 1.524
    assert con.metros_a_pies(1.524) == 5


def test_millas_kilometros():
    assert con.millas_a_kilometros(5) == 8.0467
    assert con.kilometros_a_millas(8.0467) == 5
