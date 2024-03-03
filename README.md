# GA Solver

authors : Nathanaël Lahary & Malo Lajous.

This program is a generic implementation of a genetic algorithm (GA) in Python. Genetic algorithm is an optimization method based on principles of natural selection and genetics. It is used to find the best possible solutions to a given problem using concepts inspired by biological evolution.

2 examples (TSP and Mastermind) are provided so you can find how this algorithm can your problem.

## Operation

The GA Solver comprises two main classes: `GAProblem` and `GASolver`.

### `GAProblem`

The `GAProblem` class defines a specific problem to be solved with the genetic algorithm. To use the GA Solver, you need to define your own problem class by inheriting from `GAProblem` and implementing the following methods:

- `generate()`: Generates an initial chromosome.
- `score(chromosome)`: Evaluates the fitness score of a given chromosome.
- `reversed_sort()`: Indicates whether a higher fitness score is considered better.
- `reproduction(chromosome_parent_a, chromosome_parent_b)`: Performs reproduction between two parent chromosomes to create a new chromosome.
- `reproduction_point(chromosome)`: Defines the reproduction point between parent chromosomes.
- `mutation(chromosome)`: Performs a mutation on a given chromosome.

### `GASolver`

The `GASolver` class takes a specific problem defined by an instance of `GAProblem` and solves that problem using a genetic algorithm. The main methods are:

- `reset_population(pop_size)`: Initializes the initial population with a specified size.
- `evolve_for_one_generation()`: Evolves the population for one generation by performing selection, reproduction, and mutation.
- `show_generation_summary()`: Displays information about the population after problem solved.
- `get_best_individual()`: Returns the best individual from the current population.
- `evolve_until(max_nb_of_generations, threshold_fitness)`: Evolves the population until a maximum number of generations is reached or a specific fitness level is achieved.

## Usage 

To use the GA Solver, follow these steps:

1. Define your own problem class by inheriting from `GAProblem` and implement the necessary methods. Make sure to check the documentation of each method of the `GAProblem` class for a better understanding of the expected outputs.
2. Instantiate a `GASolver` object by passing your defined problem.
3. Call the `reset_population()` and `evolve_until()` methods to solve the problem.

You may use the template provided :

```python
# Example usage

"""
Template file for your GAProblem

WARNING : You may check the documentation of each methods in the GAProblem class for a better understanding.
"""
from ga_solver import GAProblem


class YourProblem(GAProblem):
    """Implementation of GAProblem your problem"""
    def __init__(self):
        super().__init__()
        
    def generate(self):
        """Generate a random guess as a chromosome."""
        pass # Write your code
    
    def score(self, chromosome):
        """Return the fitness score associated with a chromosome."""
        pass # Write your code

    def reproduction_point(self, chromosome) -> int:
        """(Optionnal) Return the reproduction point (index) for the parent chromosomes.
           By default pick a random index.
        """        
        pass # Write your code

    def reproduction(self, chromosome_parent_a, chromosome_parent_b, chromosome_child) -> list:
        """(Optionnal) Perform reproduction between two parent chromosomes and return a new chromosome.
            By default reproduce two parents by merging their halfs obtained by spliting them with
            the reproduction point. 
        
            You may edit edit the reproduction to fit your problem.

            i.e : A gene can be duplicated in the child chromosome. 
        """
        return chromosome_child # Write your code

    def mutation(self, chromosome) -> list:
        """(Optionnal) Mutate a chromosome to create a new one.
            By default no mutation is performed. It is recommended to performe a mutation
            to get better results.
        """
        return chromosome # Write your code
    
    def reversed_sort(self) -> bool:
        """Return True if the highest fitness score is considered the best fit, False (by default) otherwise."""
        return False # Write your code

if __name__ == '__main__':

    from ga_solver import GASolver

    problem = YourProblem()
    solver = GASolver(problem)
    solver.reset_population()
    solver.evolve_until() 
```
