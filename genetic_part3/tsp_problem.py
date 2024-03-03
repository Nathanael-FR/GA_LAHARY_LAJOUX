# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving TSP example)
"""
from ga_solver import GAProblem
import cities
import random

class TSProblem(GAProblem):
    """Implementation of GAProblem for the traveling salesperson problem"""
    def __init__(self):
        super().__init__()
        
    def generate(self):
        """Generate a random guess as a chromosome."""

        chromosome = cities.default_road(city_dict)
        random.shuffle(chromosome)
        return chromosome
    
    def score(self, chromosome):
        """Return the fitness score associated with a chromosome."""
        return cities.road_length(city_dict, chromosome)

    def reproduction_point(self, chromosome):
        """Return the reproduction point for the chromosomes.
           By default pick a random point
        """        
        return len(chromosome)//2

    def reproduction(self, chromosome_parent_a, chromosome_parent_b, chromosome_child):
        """Perform reproduction between two parent chromosomes and return a new chromosome."""
        new_chrom_clean = []
        seen = set()

        for city in chromosome_child:
            if city not in seen:
                new_chrom_clean.append(city)
                seen.add(city)

        possible_cities = cities.default_road(city_dict) 

        while len(new_chrom_clean) != len(self.generate()) : 
                cities_available = [city for city in possible_cities if city not in new_chrom_clean] 
                new_chrom_clean.append(random.choice(cities_available))

        return new_chrom_clean

    def mutation(self, new_chrom):
        """Mutate a chromosome to create a new one."""

        mutation_points = random.sample(range(len(new_chrom)), 2)
        new_chrom[mutation_points[0]], new_chrom[mutation_points[1]] = new_chrom[mutation_points[1]], new_chrom[mutation_points[0]]
        return new_chrom
    
    def reversed_sort(self):
        """Return True if the highest fitness score is considered the best fit, False otherwise."""
        return False 

if __name__ == '__main__':

    from ga_solver import GASolver

    city_dict = cities.load_cities("cities.txt")
    problem = TSProblem()
    solver = GASolver(problem)
    solver.reset_population()
    solver.evolve_until(max_nb_of_generations=500, threshold_fitness=349) 
    # cities.draw_cities(city_dict, solver.getBestIndiv().chromosome)
    cities.draw_cities(city_dict, solver.get_best_individual().chromosome)
