import mastermind as mm

MATCH = mm.MastermindMatch(secret_size=9)
print(MATCH)

max_score = MATCH.max_score()
print(max_score)

chromosome = MATCH.generate_random_guess()
print(chromosome)

fitness = MATCH.rate_guess(chromosome)
print(fitness)

