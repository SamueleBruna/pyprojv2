from mathmad.model.abssum import AbsSum


class Fibonacci(AbsSum):
    """
    This class aims to print the first n number of the Fibonacci series and their sum.
    """

    def __init__(self, num: int = 1):
        """
        The constructor creates the instance with the number of series elements that should be evaluated.
        """

        self.num = num

    @staticmethod
    def sum_integers(x: int = 0, y: int = 0) -> int:
        """
        This method sums two integers, forcing the cast to integer.
        """
        return int(x + y)

    def next_fibonacci(self):
        """
        This method calculates the first n numbers of the Fibonacci series.
        """
        x, y = 1, 1
        # print(f"Now I'll print the first {self.num} numbers of the Fibonacci series \n")

        for i in range(self.num):
            # print(f"{i+1}.) {y} \n")
            yield x
            # total += self.sum_integers(x, y) lo mettiamo poi nella cli
            x, y = y, self.sum_integers(x, y)

# mettiamo questo nella cli
# fib = Fibonacci(10)
# total_sum = next(iter(fib.fibonacci()), None)  # Get the last yielded value (sum)
# += per il totale










