from unittest import TestCase

import pytest
from pytest import fixture

from solver import Solver, div


class SolverTestCase(TestCase):
    # camelCase
    def setUp(self) -> None:
        self.solver = Solver(2, 3)

    # snake_case

    def test_add(self):
        result = self.solver.add()
        self.assertEqual(5, result)
        # self.assertEqual({'spam': 'eggs'}, dict(spam='eggs'))
        self.solver.a = 4
        self.assertEqual(7, self.solver.add())

    def test_mul(self):
        result = self.solver.mul()
        self.assertEqual(6, result)


@fixture
def solver_instance():
    return Solver(2, 3)


@fixture
def solver_mix(request):
    a, b = request.param
    solver = Solver(a, b)
    return solver


class TestSolver:
    @pytest.mark.parametrize('a, b, excepted_result',
                             [
                                 [1, 2, 3],
                                 [2, 2, 4],
                                 [3, 6, 9],
                             ],
                             )
    def test_add(self, a, b, excepted_result):
        solver = Solver(a, b)
        assert solver.add() == excepted_result
        # solver = Solver(2, 3)
        # result = solver_instance.add()
        # assert result == 5
        # solver_instance.a = 4
        # assert solver_instance.add() == 7

    @pytest.mark.parametrize('solver_mix, excepted_result', [

        pytest.param([1, 2], 3),
        pytest.param([5, 6], 11),

    ],
                             indirect=['solver_mix'])
    def test_add_extra(self, solver_mix: Solver, excepted_result: int):
        assert solver_mix.add() == excepted_result

    def test_mul(self, solver_instance):
        # solver = Solver(2, 3)
        result = solver_instance.mul()
        assert result == 6

    def test_mul__raises(self):
        solver = Solver("a", 3)
        with pytest.raises(TypeError) as exc_info:
            solver.mul()
        assert str(exc_info.value) == solver.exc_text


def test_div():
    assert div(1, 2) == 0.5
