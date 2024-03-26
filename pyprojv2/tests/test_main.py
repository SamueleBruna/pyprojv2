import unittest
from typer.testing import CliRunner
from pyprojv2.__main__ import app
from mathmad.fibonacci import Fibonacci
from hellower.hellower import Hellower

# this is what will invoke the app when testing
runner = CliRunner()


class MyTestCase(unittest.TestCase):
    def test_app_1(self):
        result = runner.invoke(app, ["fibonacci", "1"])
        output = "The first 1 Fibonacci Series numbers are:\n"
        output += "1\t\nTheir sum is 1"

        assert result.exit_code == 0
        assert output in result.stdout

    def test_app_2(self):
        result = runner.invoke(app, ["-h", "fibonacci", "1"], input="Mago\n")
        output = "Hello Mago!\n"
        output += "The first 1 Fibonacci Series numbers are:\n"
        output += "1\t\nTheir sum is 1"

        assert result.exit_code == 0
        assert output in result.stdout

    def test_app_3(self):
        result = runner.invoke(app, ["--hello", "fibonacci", "1"], input="Mago\n")
        output = "Hello Mago!\n"
        output += "The first 1 Fibonacci Series numbers are:\n"
        output += "1\t\nTheir sum is 1"

        assert result.exit_code == 0
        assert output in result.stdout


if __name__ == '__main__':
    unittest.main()
