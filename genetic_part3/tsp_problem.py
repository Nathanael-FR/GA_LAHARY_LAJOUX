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
        chromosome = cities.default_road(city_dict)
        random.shuffle(chromosome)
        return chromosome
    
    def score(self, chromosome):
        # Given a chromosome, return his fitness score
        return cities.road_length(city_dict, chromosome)

    def reproduction(self, chromosome_parent_a, chromosome_parent_b, new_chrom):
        # Given 2 parents, return a new chromosome. If pass, use default ga_solver reproduction function.


        new_chrom = list(set(new_chrom))    
        possible_cities = cities.default_road(city_dict) 

        while len(new_chrom) != len(self.generate()) : 
                cities_available = [city for city in possible_cities if city not in new_chrom] 
                new_chrom.append(random.choice(cities_available))

        return new_chrom

    def mutation(self, new_chrom):
        # Given a chromsome, mutate him to a new chromosome.

        mutation_point = 0
        mutation_point_2 = 0

        while (mutation_point == mutation_point_2):   
            mutation_point = random.randrange(0, len(new_chrom))
            mutation_point_2 = random.randrange(0, len(new_chrom))
                
        new_chrom[mutation_point], new_chrom[mutation_point_2] = new_chrom[mutation_point_2], new_chrom[mutation_point]
        return new_chrom
    
    def reversed_sort(self):
        # True if the highest fitness score is the best fit. True instead.
        return False 

if __name__ == '__main__':

    from ga_solver import GASolver

    city_dict = cities.load_cities("cities.txt")
    problem = TSProblem()
    solver = GASolver(problem)
    solver.reset_population()
    solver.evolve_until(max_nb_of_generations=1000, threshold_fitness=400)
    # cities.draw_cities(city_dict, solver.getBestIndiv().chromosome)
    cities.draw_cities(city_dict, solver.get_best_individual().chromosome)