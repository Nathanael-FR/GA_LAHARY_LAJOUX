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

    def generate(self) -> list:
        """Generate a chromosome.

        Returns:
            list: chromosome as a list of genes.
        """
        pass

    def score(self, chromosome) -> float:
        """ Return a fitness score associated to a chromosome.

        Args:
            chromosome (list): A chromosome.

        Returns:
            float: the fitness score.
        """
        pass

    def reversed_sort(self) -> bool:
        """ True if the highest fitness score defines the best chromosome. False instead.

        Returns:
            bool: A boolean used when we sort chromosomes by their fitness score.
        """
        pass

    def reproduction(self, chromosome_parent_a, chromosome_parent_b) -> list:
        """ The reproduction of 2 chromosomes to give a new one.

        Args:
            chromosome_parent_a (list): A parent chromosome used for the reproduction
            chromosome_parent_b (list): A second parent chromosome used for the reproduction

        Returns:
            list: The child chromosome from the reproduction of chromosome A and B.
        """
        pass 
    
    def reproduction_point(self, chromosome) -> int:
        """ Defines where we cut the parents chromosomes. By default a random a point.

            i.e : We keep only the length of parent A to this point, and only from this point for parent B,
                  then concatenate them.

        Args:
            chromosome (_type_): A chromosome used to know the length of a chromosome.

        Returns:
            int: The index of the reproduction point.
        """
        pass

    def mutation(self, chromosome) -> list:
        """ Mutate a chromosome to give a different one.

        Args:
            chromosome (list): The chromosome ready to be mutated.

        Returns:
            list: The mutated chromosome
        """
        pass

    


    


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
        self._population_disparity = []
    def reset_population(self, pop_size=50) -> None:
        """ Initialize the population with pop_size random Individuals

        Args:
            pop_size (int, optional): Size of the population of chromosomes that will
                                      evolve through generations. Defaults to 50.
        """
        for i in range(pop_size):
            chromosome = self._problem.generate()
            fitness = self._problem.score(chromosome)
            new_individual = Individual(chromosome, fitness)
            self._population.append(new_individual)

    def evolve_for_one_generation(self) -> None:
        """ Apply the process for one generation : 
            -	Sort the population (Descending order)
            -	Selection: Remove x% of population (less adapted)
            -   Reproduction: Recreate the same quantity by crossing the 
                surviving ones 
            -	Mutation: For each new Individual, mutate with probability 
                mutation_rate i.e., mutate it if a random value is below   
                mutation_rate
        """
        chromosomes = []
        for i in range(len(self._population)):
            chromosomes.append(self._population[i].chromosome)

        disparity = len(list(set(tuple(i) for i in chromosomes)))/len(chromosomes)
        print(disparity)
        
        self._population_disparity.append(disparity)

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

            x_point = self._problem.reproduction_point(parent_a.chromosome)
            if x_point == None :
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
            mutants.append(new_indiv) 

        self._population = self._population + mutants 


    def show_generation_summary(self, nb_gen, best_individuals) -> None:
        """ Print some debug information on the current state of the population """
        fig, (ax1, ax2) = plt.subplots(2)

        # Plot the evolution of population disparity
        ax1.plot(range(nb_gen), self._population_disparity)
        ax1.set_xlabel('Number of Generations')
        ax1.set_ylabel('Population disparity')
        ax1.set_title('Evolution of Population disparity')

        # Plot the evolution of the best individual score through generations
        ax2.plot(range(nb_gen), best_individuals)
        ax2.set_xlabel('Number of Generations')
        ax2.set_ylabel('Fitness Score of Best Individual')
        ax2.set_title('Evolution of Best Individual Fitness')
        if not self._problem.reversed_sort():
            ax2.invert_yaxis()  # Inverse the y-axis

        plt.tight_layout()  # Adjust layout to prevent overlap
        plt.show()


    def get_best_individual(self) -> object:
        """ Return the best Individual of the population """
        self._population.sort(reverse = self._problem.reversed_sort())
        return self._population[0]

    def evolve_until(self, max_nb_of_generations=500, threshold_fitness=None) -> None:
        """ Launch the evolve_for_one_generation function until one of the two condition is achieved : 
            - Max nb of generation is achieved
            - The fitness of the best Individual is greater than or equal to
              threshold_fitness
        """
        total_best_ind = []
        for i in range(max_nb_of_generations):
            self.evolve_for_one_generation()
            best_individual = self.get_best_individual()
            total_best_ind.append(best_individual.fitness)
            if (threshold_fitness != None) and (best_individual.fitness <= threshold_fitness) :
                print(f'Found : {best_individual}')
                break
        print(f"Best individual : {self.get_best_individual()}")
        self.show_generation_summary(i+1, total_best_ind)