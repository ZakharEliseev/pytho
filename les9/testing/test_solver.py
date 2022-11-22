from unittest import TestCase

from solver import Solver


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

