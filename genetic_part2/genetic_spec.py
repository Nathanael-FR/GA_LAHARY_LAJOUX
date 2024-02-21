# -*- coding: utf-8 -*-
import random 
import cities 

"""
Created on Mon Feb 21 11:24:15 2022

@author: agademer & tdrumond

Template for exercise 1
(genetic algorithm module specification)
"""


class Individual:
    """Represents an Individual for a genetic algorithm"""

    def __init__(self, chromosome: list, fitness: float):
        """Initializes an Individual for a genetic algorithm 

        Args:
            chromosome (list[]): a list representing the individual's chromosome
            fitness (float): the individual's fitness (the higher, the better the fitness)
        """
        self.chromosome = chromosome
        self.fitness = fitness

    def __lt__(self, other):
        """Implementation of the less_than comparator operator"""

        return self.fitness < other.fitness

    def __repr__(self):
        """Representation of the object for print calls"""
        return f'Indiv({self.fitness:.1f},{self.chromosome})'


class GASolver:
    def __init__(self, selection_rate=0.5, mutation_rate=0.1):
        """Initializes an instance of a ga_solver for a given GAProblem

        Args:
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []

    def reset_population(self, pop_size=50):
        """ Initialize the population with pop_size random Individuals """
        
        for i in range(pop_size):    
            chromosome = cities.default_road(city_dict)
            random.shuffle(chromosome)
            fitness = cities.road_length(city_dict, chromosome)
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

        # Keep only the upper half of the Individuals i.e: the ones with the best fitness score

        self._population.sort() # The lower the fitness is, the best (shortest) the path is, so we order in ascending order
        self._population = self._population[0:int(self._selection_rate*len(self._population))]  
        
        mutants = []

        possible_cities = cities.default_road(city_dict)

        for i in range(len(self._population)):

            selection_point = 0
            selection_point_2 = 0

            while (selection_point == selection_point_2):   
                selection_point = random.randrange(0, len(self._population))
                selection_point_2 = random.randrange(0, len(self._population))

            parent_a = self._population[selection_point]
            parent_b = self._population[selection_point_2]

            # print(f' Parent A : {parent_a}\n')
            # print(f' Parent B : {parent_b}')

            x_point = random.randrange(0, len(parent_a.chromosome))

            new_chrom = parent_a.chromosome[0:x_point] + parent_b.chromosome[x_point:]
            new_chrom = list(set(new_chrom))    # Remove duplicated cities (genes) 

            # Complete the chromosome with remaining cities until he has a valid length
            while len(new_chrom) != len(parent_a.chromosome) :
                cities_available = [city for city in possible_cities if city not in new_chrom]
                new_chrom.append(random.choice(cities_available))

            new_indiv = Individual(new_chrom, cities.road_length(city_dict, new_chrom))

            number = random.random()

            if number < self._mutation_rate :
                mutation_point = 0
                mutation_point_2 = 0

                while (mutation_point == mutation_point_2):   
                    mutation_point = random.randrange(0, len(new_chrom))
                    mutation_point_2 = random.randrange(0, len(new_chrom))
                

                new_chrom[mutation_point], new_chrom[mutation_point_2] = new_chrom[mutation_point_2], new_chrom[mutation_point]
                new_indiv = Individual(new_chrom, cities.road_length(city_dict, new_chrom))

            print(f'New chrom : {new_indiv.chromosome} \n path length : {new_indiv.fitness}')
            mutants.append(new_indiv)

        self._population = self._population + mutants 


    def show_generation_summary(self):
        """ Print some debug information on the current state of the population """
        pass  # REPLACE WITH YOUR CODE

    def get_best_individual(self):
        """ Return the best Individual of the population """
        self._population.sort()
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
                print(f'Found : {i}')
                break

seed = random.seed()
city_dict = cities.load_cities("cities.txt")
solver = GASolver()
solver.reset_population()
solver.evolve_until(1000, 392)    # Best obtainted : 391.79348316719285
best = solver.get_best_individual()
print(best.chromosome)
cities.draw_cities(city_dict, best.chromosome)