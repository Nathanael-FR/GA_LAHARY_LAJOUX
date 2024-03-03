# -*- coding: utf-8 -*-
"""
Created on Sun Mar 3 2024

@author: nlahary & mlajous

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
