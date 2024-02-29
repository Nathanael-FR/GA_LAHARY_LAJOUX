# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(generic genetic algorithm module)
"""
import random
import time
import matplotlib
import matplotlib.pyplot as plt

class Individual:
    """Represents an Individual for a genetic algorithm"""

    def __init__(self, chromosome: list, fitness: float):
        """Initializes an Individual for a genetic algorithm

        Args:
            chromosome (list[]): a list representing the individual's
            chromosome
            fitness (float): the individual's fitness (the higher the value,
            the better the fitness)
        """
        self.chromosome = chromosome
        self.fitness = fitness

    def __lt__(self, other):
        """Implementation of the less_than comparator operator"""
        return self.fitness < other.fitness

    def __repr__(self):
        """Representation of the object for print calls"""
        return f'Indiv({self.fitness:.1f},{self.chromosome})'


class GAProblem:
    """Defines a Genetic algorithm problem to be solved by ga_solver"""
    def __init__(self):
        pass

    def generate(self):
        pass

    def score(self, chromosome):
        pass

    def reproduction(self, chromosome_parent_a, chromosome_parent_b):
        pass 
    
    def mutation(self, chromosome):
        pass

    def reversed_sort(self):
        return self._reverse



    


class GASolver:
    def __init__(self, problem: GAProblem, selection_rate=0.5, mutation_rate=0.1):
        """Initializes an instance of a ga_solver for a given GAProblem

        Args:
            problem (GAProblem): GAProblem to be solved by this ga_solver
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        
        self._problem = problem
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []
        self._new_generations = []
        self._total_nb_gen = 0

    def reset_population(self, pop_size=50):
        """ Initialize the population with pop_size random Individuals """
        for i in range(pop_size):
            chromosome = self._problem.generate()
            fitness = self._problem.score(chromosome)
            new_individual = Individual(chromosome, fitness)
            self._population.append(new_individual)

    def evolve_for_one_generation(self):
        """ Apply the process for one generation : 
            -	Sort the population (Descending order)
            -	Selection: Remove x% of population (less adapted)
            -   Reproduction: Recreate the same quantity by crossing the 
                surviving ones 
            -	Mutation: For each new Individual, mutate with probability 
                mutation_rate i.e., mutate it if a random value is below   
                mutation_rate
        """
        self._population.sort(reverse = self._problem.reversed_sort())
        # Keep the upper half based on fitness score.
        self._population = self._population[0:int(self._selection_rate*len(self._population))]

        mutants = [] 


        # REPRODUCTION (1/2) :  between 2 parents randomly chosen.
        for i in range(len(self._population)): 
            
            selection_point = 0 
            selection_point_2 = 0 


            while (selection_point == selection_point_2):   
                selection_point = random.randrange(0, len(self._population)) 
                selection_point_2 = random.randrange(0, len(self._population)) 


            parent_a = self._population[selection_point] 
            parent_b = self._population[selection_point_2] 

            x_point = random.randrange(0, len(parent_a.chromosome)) 
            new_chrom = parent_a.chromosome[0:x_point] + parent_b.chromosome[x_point:] 
            
            new_chrom = self._problem.reproduction(parent_a, parent_b, new_chrom)
            
            new_indiv = Individual(new_chrom, self._problem.score(new_chrom)) 

            # MUTATION (2/2) : 
            number = random.random() 

            if number < self._mutation_rate : 

                new_chrom_mutated = self._problem.mutation(new_chrom)
                new_indiv = Individual(new_chrom_mutated, self._problem.score(new_chrom_mutated)) 
            
            self._new_generations.append(new_indiv.fitness)
            self._total_nb_gen += 1

            mutants.append(new_indiv) 
            print(f'New generation : {new_indiv.fitness}')

        self._population = self._population + mutants 


    def show_generation_summary(self):
        """ Print some debug information on the current state of the population """

        pass  # REPLACE WITH YOUR CODE

    def get_best_individual(self):
        """ Return the best Individual of the population """
        self._population.sort(reverse = self._problem.reversed_sort())
        print(self._population[0].fitness)
        return self._population[0]

    def evolve_until(self, max_nb_of_generations=500, threshold_fitness=None):
        """ Launch the evolve_for_one_generation function until one of the two condition is achieved : 
            - Max nb of generation is achieved
            - The fitness of the best Individual is greater than or equal to
              threshold_fitness
        """
        for i in range(max_nb_of_generations):
            self.evolve_for_one_generation()
            best_individual = self.get_best_individual()
            if (threshold_fitness != None) and (best_individual.fitness <= threshold_fitness) :
                print(f'Found : {best_individual}')
                break
        print(f"Best individual : {self.get_best_individual()}")