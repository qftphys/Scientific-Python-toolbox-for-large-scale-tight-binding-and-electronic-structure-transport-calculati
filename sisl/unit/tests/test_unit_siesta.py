from __future__ import print_function, division

import pytest

from sisl.unit.siesta import unit_group, unit_convert, unit_default

pytestmark = pytest.mark.unit


def test_group():
    assert unit_group('kg') == 'mass'
    assert unit_group('eV') == 'energy'
    assert unit_group('N') == 'force'


def test_unit_convert():
    assert pytest.approx(unit_convert('kg', 'g')) == 1.e3
    assert pytest.approx(unit_convert('eV', 'J')) == 1.60219e-19
    assert pytest.approx(unit_convert('J', 'eV')) == 1/1.60219e-19


def test_default():
    assert unit_default('mass') == 'amu'
    assert unit_default('energy') == 'Ry'
    assert unit_default('force') == 'Ry/Bohr'
