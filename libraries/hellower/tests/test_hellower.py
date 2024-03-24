import unittest

from hellower.hellower import Hellower
from unittest.mock import patch


class MyTestCase(unittest.TestCase):

    # mocking the print function that is called by hello_world
    @patch('builtins.print')
    def test_say_hello(self, mock_print):
        # The actual test
        name = 'Samu'
        hello = Hellower(name)
        hello.say_hello()
        # asserting that the print function is called passing the string 'Hello World!'
        mock_print.assert_called_with(f'Hello {name}!')


if __name__ == '__main__':
    unittest.main()
