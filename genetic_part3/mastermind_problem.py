# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving Mastermind example)
"""
from ga_solver import GAProblem, Individual
import mastermind as mm
import random

class MastermindProblem(GAProblem):
    """Implementation of GAProblem for the mastermind problem"""
    def __init__(self):
        super().__init__()
        
    def generate(self):
        """Generate a random guess as a chromosome."""
        chromosome = match.generate_random_guess()
        return chromosome
    
    def score(self, chromosome):
        """Return the fitness score associated with a chromosome."""
        return match.rate_guess(chromosome)
    
    def reversed_sort(self):
        """Return True if the highest fitness score is considered the best fit, False otherwise."""
        return True

    def reproduction(self, chromosome_parent_a, chromosome_parent_b, chromosome_child):
        """Perform reproduction between two parent chromosomes and return a new chromosome."""
        return chromosome_child

    def reproduction_point(self, chromosome) -> int:
        """Return the reproduction point for the chromosomes.
           By default pick a random point
        """
        pass


    def mutation(self, new_chrom):
        """Mutate a chromosome to create a new one."""
        valid_genes = mm.get_possible_colors()
        new_gene = random.choice(valid_genes) 
                
        pos = random.randrange(0, len(new_chrom)) 
 
        new_chrom_mutated = new_chrom[0:pos] + [new_gene] + new_chrom[pos+1:] 

        return new_chrom_mutated
      


if __name__ == '__main__':

    from ga_solver import GASolver

    match = mm.MastermindMatch(secret_size=6)
    problem = MastermindProblem()

    solver = GASolver(problem)

    solver.reset_population()
    solver.evolve_until()

    
    print(
        f"Problem solved? {match.is_correct(solver.get_best_individual().chromosome)}")
