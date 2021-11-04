import pytest
from collatz.three_n_plus_one import ThreeNPlusOne, recursive_iter


@pytest.mark.xfail(reason="code not working well")
@pytest.mark.parametrize("x", [1, 2])
def test_intermediate_steps_test1(x):
    assert ThreeNPlusOne(x).intermediate_steps == recursive_iter(x)[0]


@pytest.mark.parametrize("x", [4, 3, 5, 7])
def test_intermediate_steps_test2(x):
    assert ThreeNPlusOne(x).intermediate_steps == recursive_iter(x)[0]
