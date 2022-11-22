from unittest import TestCase

from solver import Solver


class SolverTestCase(TestCase):

    def test_add(self):
        solver = Solver(2, 3)
        result = solver.add()
        self.assertEqual(5, result)
        # self.assertEqual({'spam': 'eggs'}, dict(spam='eggs'))
        # solver.a = 4
        # self.assertEqual(7, solver.add())
