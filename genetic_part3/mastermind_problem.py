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
    def __init__(self, match):
        super().__init__()
        
    def generate(self):
        chromosome = match.generate_random_guess()
        return chromosome
    
    def score(self, chromosome):
        # Given a chromosome, return his fitness score
        return match.rate_guess(chromosome)
    
    def reversed_sort(self):
        # True if the highest fitness score is the best fit. False instead.
        return True

    def reproduction(self, chromosome_parent_a, chromosome_parent_b, new_chrom):
        # Given 2 parents, return a new chromosome. If pass, use default ga_solver reproduction function.
        return new_chrom

    def mutation(self, new_chrom):
        # Given a chromsome, mutate him to a new chromosome.
        valid_genes = mm.get_possible_colors()
        new_gene = random.choice(valid_genes) 
                
        pos = random.randrange(0, len(new_chrom)) 
 
        new_chrom_mutated = new_chrom[0:pos] + [new_gene] + new_chrom[pos+1:] 

        return new_chrom_mutated
      


if __name__ == '__main__':

    from ga_solver import GASolver

    match = mm.MastermindMatch(secret_size=6)
    problem = MastermindProblem(match)

    solver = GASolver(problem)

    solver.reset_population()
    solver.evolve_until()

    
    print(
        f"Problem solved? {match.is_correct(solver.get_best_individual().chromosome)}")
