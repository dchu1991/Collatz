a simple recursive program to iterate through all hailstone numbers inspired by the Collatz conjucture.

## usage

```
# navigate to this directory
!pip install -e .

from collatz.three_n_plus_one import ThreeNPlusOne, recursive_iter

```
then call the ThreeNPlusOne class with int.
each instance has a attribute, intermediate_steps, which is a tuple containing all hailstone numbers starting with the initialized int.

however the code is flawed such that elements of a loop depends on the order you initialized it.  i recommend you first initialize ThreeNPlusOne(1) before initialize with other positive int instances such that the outcome of intermediate_steps is correct except ThreeNPlueOne(2).
you can refer to the test file for details.

//TODO: make this improvement.

the package also comes with another function, recursive_iter, to help compute the correct intermediate_steps.  however it doesn't make connection with previous called results so is less helpful in terms of reducing computation time... in my opinion.

have fun.
![Tests](https://github.com/dchu1991/Collatz/actions/workflows/test.yml/badge.svg)
