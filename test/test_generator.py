import unittest
import generator as gen


class TestGenerator(unittest.TestCase):

    def test_get_n_valid_one(self):
        answer = gen.get_n(1)
        self.assertEqual(0, answer)

    def test_get_n_valid_two(self):
        answer = gen.get_n(2)
        self.assertEqual(1, answer)

    def test_get_n_valid_three(self):
        answer = gen.get_n(3)
        self.assertEqual(1, answer)

    def test_get_n_valid_four(self):
        answer = gen.get_n(4)
        self.assertEqual(2, answer)

    def test_get_n_valid_five(self):
        answer = gen.get_n(5)
        self.assertEqual(3, answer)

    def test_get_sequence_one(self):
        answer = gen.get_sequence(1)
        self.assertEqual([0], answer)

    def test_get_sequence_two(self):
        answer = gen.get_sequence(2)
        self.assertEqual([0, 1], answer)

    def test_get_sequence_three(self):
        answer = gen.get_sequence(3)
        self.assertEqual([0, 1, 1], answer)

    def test_get_sequence_five(self):
        answer = gen.get_sequence(5)
        self.assertEqual([0, 1, 1, 2, 3], answer)

    def test_get_sequence_ten(self):
        answer = gen.get_sequence(10)
        self.assertEqual([0, 1, 1, 2, 3, 5, 8, 13, 21, 34], answer)

    def test_sum_sequence_one(self):
        answer = gen.sum_of_sequence(1)
        self.assertEqual(0, answer)

    def test_sum_sequence_two(self):
        answer = gen.sum_of_sequence(2)
        self.assertEqual(1, answer)

    def test_sum_sequence_four(self):
        answer = gen.sum_of_sequence(4)
        self.assertEqual(4, answer)

    def test_sum_sequence_five(self):
        answer = gen.sum_of_sequence(5)
        self.assertEqual(7, answer)

    def test_sum_sequence_ten(self):
        answer = gen.sum_of_sequence(10)
        self.assertEqual(88, answer)


if __name__ == "__main__":
    TestGenerator.main()
