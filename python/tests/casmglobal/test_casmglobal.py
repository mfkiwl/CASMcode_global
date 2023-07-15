import math
import libcasm.casmglobal as casmglobal


def test_TOL():
    assert math.isclose(casmglobal.TOL, 1e-5)


def test_KB():
    assert math.isclose(casmglobal.KB, 8.6173423e-05)  # eV/K


def test_PLANK():
    assert math.isclose(casmglobal.PLANCK, 4.135667516e-15)  # eV-s
