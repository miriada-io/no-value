import pytest
from pytest import param

from no_value import NoValue


def test_no_value_eq():
    assert NoValue is NoValue
    assert NoValue == NoValue


@pytest.mark.parametrize(['value'], [
    param(None), param(False), param(0), param([]), param({})
])
def test_no_value_ne(value):
    assert NoValue != value
    assert NoValue is not value


@pytest.mark.parametrize(['type_', 'is_instance', 'is_subclass'], [
    param(bool, False, False),
    param(type(None), False, False),
    param(type, True, False)
])
def test_no_value_is_not_instance(type_: type, is_instance: bool, is_subclass: bool):
    assert isinstance(NoValue, type_) == is_instance
    assert issubclass(NoValue, type_) == is_subclass


def test_no_value_str():
    assert str(NoValue) == 'NoValue'


def test_no_value_repr():
    assert repr(NoValue) == 'NoValue'


def test_no_value_cannot_be_instantiated():
    with pytest.raises(TypeError, match="NoValue cannot be instantiated"):
        NoValue()


def test_no_value_cannot_be_cast_to_bool():
    with pytest.raises(TypeError, match="NoValue cannot be cast to bool"):
        bool(NoValue)
