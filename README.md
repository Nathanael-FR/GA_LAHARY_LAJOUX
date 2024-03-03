# GA Solver

authors : Nathanaël Lahary & Malo
This program is a generic implementation of a genetic algorithm (GA) in Python. Genetic algorithm is an optimization method based on principles of natural selection and genetics. It is used to find the best possible solutions to a given problem using concepts inspired by biological evolution.

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
- `show_generation_summary()`: Displays information about the current state of the population (not implemented in the provided code).
- `get_best_individual()`: Returns the best individual from the current population.
- `evolve_until(max_nb_of_generations, threshold_fitness)`: Evolves the population until a maximum number of generations is reached or a specific fitness level is achieved.

## Usage

To use the GA Solver, follow these steps:

1. Define your own problem class by inheriting from `GAProblem` and implement the necessary methods.
2. Instantiate a `GASolver` object by passing your defined problem.
3. Call the `reset_population()` and `evolve_until()` methods to solve the problem.

```python
# Example usage
from ga_solver import GAProblem, GASolver

# Define your own problem class
class MyProblem(GAProblem):
    # Implement the necessary methods

# Instantiate the solver with your problem
solver = GASolver(MyProblem())

# Solve the problem
solver.reset_population()
solver.evolve_until()
```
