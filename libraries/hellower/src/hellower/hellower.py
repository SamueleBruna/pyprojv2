class Hellower:
    """
    This is the class Hellower. Its aim is to say hello to everybody.
    """

    def __init__(self, name: str = 'World'):  # This is the constructor method
        """
        The constructor creates the instance with the name of the addressee.
        """

        self.name = name

    def say_hello(self) -> None:
        """
        This is the method that says hello to the desired addressee.
        """

        print(f'Hello {self.name}!')
