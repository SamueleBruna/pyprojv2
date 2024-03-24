import unittest

from mathmad.fibonacci import Fibonacci


class MyTestCase(unittest.TestCase):

    def test_next_fibonacci(self):
        """
        This Test verifies that the Fibonacci sequence is computed correctly by asserting the last value yielded.
        """
        # The actual test
        num, total_sum = 5, 0
        fib = Fibonacci(num)
        for n in fib.next_fibonacci():
            total_sum += n
        self.assertEqual(12, total_sum)


if __name__ == '__main__':
    unittest.main()
