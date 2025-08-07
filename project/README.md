A simple calculator

Video URL: https://youtu.be/w6Q6FMr-N1w

This is a simple calculator that allows one to add, subtract,
divide and multiply numbers. One simply chooses which operation
they'd like to conduct, enter two numbers then the app executes
accordingly.

The app consists of two Python files (project.py and test_project.py).
Project.py has six functions (choice(), add(), sub(), mult(), div() as well as main()).
The choice() function displays the arithmetic options available for the user to choose
from, then allows the user to choose one. The function then returns the user's choice in
the form of an int. Should the user enter an incorrect value, the app calls the sys.exit() function
to notify the user that an incorrect value has been entered then exits.

The add() function accepts two arguments,
then perform the preferred calculation, returning an f-string that displays the whole
calculation. The try/except methods are used in case the user enters an invalid value.
The sys.exit() function is executed when the user enters an incorrect value.

The sub() function accepts two arguments,
then perform the preferred calculation, returning an f-string that displays the whole
calculation. The try/except methods are used in case the user enters an invalid value.
The sys.exit() function is executed when the user enters an incorrect value.

The mult() function accepts two arguments,
then perform the preferred calculation, returning an f-string that displays the whole
calculation. The try/except methods are used in case the user enters an invalid value.
The sys.exit() function is executed when the user enters an incorrect value.

The div() function accepts two arguments,
then perform the preferred calculation, returning an f-string that displays the whole
calculation. The try/except methods are used in case the user enters an invalid value
or tries to divide by zero.
The sys.exit() function is executed when the user enters an incorrect value.


Defensive programming was applied to all the functions, meaning should the user enter
an invalid value, the user is notified and the app exits.

The test_project.py is used to test the functions.

