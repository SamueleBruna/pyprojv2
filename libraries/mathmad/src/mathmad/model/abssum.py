import abc


class AbsSum(abc.ABC):
    """
    This is an abstract class, which gives a template to other classes that must implement an integer sum.
    """

    @staticmethod
    @abc.abstractmethod
    def sum_integers(x: int = 0, y: int = 0) -> int:
        """
        The abstract method should implement a mathematical integer sum.
        """

        pass
