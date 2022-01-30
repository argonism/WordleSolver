import unittest
from solver import *

class TestSolver(unittest.TestCase):

    def test_patterns(self):
        query = "alert"
        answer = "salet"
        condition = tuple("11102")
        self.assertEqual(condition, to_pattern(query, answer))

    def test_calc_entropy(self):
        query = "alert"
        vocab = ["salet", "print", "robot"]
        # the cue patterns will be: [11102, 00012, 00012]
        entropy = - ((2/3 * math.log2(2/3)) + (1/3 * math.log2(1/3)))
        self.assertEqual(entropy, calc_entropy(query, vocab))

    def test__is_meet_condition(self):
        dict_path = "dictionary.dict"
        solver = WordleSolver(dict_path)
        query = "tares"
        condition = tuple("00100")
        self.assertFalse(solver._is_meet_condition("grant", query, condition))

if __name__ == "__main__":
    unittest.main()