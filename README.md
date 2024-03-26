# pyprojv2 #

This project has its aim to create a simple python package creating a CLI. The CLI will output the desired first n numbers of the Fibonacci series.\
There is a CLI Option available that asks to insert the user name in prompt and then says hello to him.\
The project is based on Poetry and typer Library. You need to install Poetry to play with it.\
\
__Try it!__

1) Download the project inside a new folder
2) Using your shell, get inside the pyprojv2 folder
3) run shell command: `poetry install`
4) Try the command: `pyprojv2 fibonacci 4`
5) Try the option `pyprojv2 --hello fibonacci 4` (-h is available)
 


## Architecture of the Project ##
![pyprojv2_image](https://github.com/SamueleBruna/pyprojv2/assets/110241700/5527b489-3a2e-4673-a97b-a1318b435778)

The project was created using the poetry command: `poetry new --src <name_of_folder>`.\
It is divided into 2 main sections: libraries and pyprojv2.\
The CLI is implemented inside the \_\_main\_\_.py script using the typer library.\
Inside the libraries folder are implemented the classes used inside the CLI.\
Every class method or CLI command has its own test.

### pyprojv2 ###
Here its implemented the CLI inside \_\_main\_\_.py script.\
The CLI command is called fibonacci and prints the first n numbers of the Fibonacci series and their sum using the custom library mathmad.fibonacci (implemented inside the libraries folder).\
The CLI option is implemented using the typer callback decorator that uses the custom library hellower.hellower (implemented inside the libraries folder).\ 
The callback method asks the user its name and then prompts a kindly hello. By construction this callback method is always invoked before the fibonacci command if the -h or --hello is present in the CLI command.

### libraries ###
Here are the libraries implemented:
1) mathmad has a model folder in which the abstract class AbsSum is implemented. Inside fibonacci.py its implemented the method that calculates the firs n Fibonacci numbers and the class inherits from AbsSum.
2) hellower is a single class which prompts hello to the user.

#### Useful Poetry commands and tips ###

1) `poetry install` (always do this to create the poetry env with the basic toml and then you can use poetry add command freely)
2) `poetry add \<package\>` -> you can add libraries directly into your .toml file
3) `poetry build` -> you can build you artifact

__N.B.__ The CLI command is implemented using the .toml section `\[tool.poetry.scripts\]\`
This line `pyprojv2 = "pyprojv2.\_\_main\_\_:app"` implies:\
that when we install the package using poetry, we want it to create a command line program called pyprojv2 and
that the object to call (like a function) is the one in the variable app inside of the module pyprojv2.\_\_main\_\_ module.\

In this case, these lines (in \_\_main\_\_.py):
```
if __name__ == "__main__":
    app()
```

 are not used directly by the CLI command. They are only there to more easily run and test the script with the IDE.
