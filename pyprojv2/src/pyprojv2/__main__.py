import typer
from typing_extensions import Annotated
from mathmad.fibonacci import Fibonacci
from hellower.hellower import Hellower

app = typer.Typer(name="pyprojv2", no_args_is_help=True, add_completion=False, pretty_exceptions_enable=False)
help_fib = "This Argument represents the how many numbers from the Fibonacci series you want  to know"
help_hello = "If launched with --hello or -h the app will ask the user its name and says hello to him \n ex. pyprojv2 -h fibonacci 4"


@app.callback()
def main(hello: Annotated[bool, typer.Option("--hello", "-h", help=help_hello)] = False):
    """
    This is a polite Cli that gives you the opportunity to know the first n numbers of the Fibonacci Series
    """

    if hello:
        user_name = typer.prompt("What's your name?")
        hi = Hellower(user_name)
        hi.say_hello()


# add callbacks for argument type https://typer.tiangolo.com/tutorial/options/callback-and-context/
@app.command()
def fibonacci(n_fib: Annotated[int, typer.Argument(help=help_fib)]):
    """
    Prints the first n numbers of the Fibonacci series and their sum
    """

    fib = Fibonacci(n_fib)
    sum_fib: int = 0
    typer.echo(f"The first {n_fib} Fibonacci Series numbers are:")
    for n in fib.next_fibonacci():
        typer.echo(f"{n}\t")
        sum_fib += n
    typer.echo(f"Their sum is {sum_fib}")


if __name__ == "__main__":
    app()
