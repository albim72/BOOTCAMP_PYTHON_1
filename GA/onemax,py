#populacja wektorów 100 elementowych wypełnionych wartościami 0 i 1
#celem jest utworzenie populacji wypełnionej jak największą liczbą jednynek,
#sukcesem będzie osiągnięcie przynajmniej jedngo osobnika zawierającego  wszystkie 1
#ile pokoloń potrzebujesz na wykonanie tego zadania?

import random
from deap import base
from deap import creator
from deap import tools

creator.create("FitnessMax",base.Fitness,weights=(1.0,))
creator.create("Individual",list,fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_bool",random.randint,0,1)
#utworzenie osobnika populacji
toolbox.register("individual",tools.initRepeat,creator.Individual, toolbox.attr_bool,100)

#utworzenie populacji
toolbox.register("population",tools.initRepeat,list,toolbox.individual)

def evalOneMax(individual):
    return sum(individual),

#proces ewaluacji
toolbox.register("evaluate",evalOneMax)

#operator krzyżowania
toolbox.register("mate",tools.cxTwoPoint)

#operator mutacji
toolbox.register("mutate",tools.mutFlipBit,indpb=0.05)

#operator selekcji -> selekcja turniejowa
toolbox.register("select",tools.selTournament,tournsize=3)

def main():

    random.seed(64)

    pop = toolbox.population(n=300)

    CXPB, MUTPB = 0.5, 0.2
    print("Start Ewolucji")

    fitness = list(map(toolbox.evaluate,pop))
    for ind,fit in zip(pop,fitness):
        ind.fitness.values = fit

    print(f"Ewaluacja {pop} osobników")
    fits = [ind.fitness.values[0] for ind in pop]
    #generacja osobników
    g = 0

    while max(fits) < 100 and g <1000:
        g=g+1
        print(f"-- Generacja {g} --")

        offspring = toolbox.select(pop,len(pop))
        offspring = list(map(toolbox.clone, offspring))

        for child1,child2 in zip(offspring[::2],offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1,child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        #ewaluacja osobników
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind,fitnesses):
            ind.fitness.values = fit

        print(f"Sprawdzono {invalid_ind} osobników")

        pop[:] = offspring

        fits = [ind.fitness.values[0] for ind in pop]
        length = len(pop)
        mean = sum(fits)/length
        sum2 = sum(x**2 for x in fits)
        std = abs(sum2/length - mean**2)**0.5


        print(f"  Min {min(fits)}")
        print(f"  Max {max(fits)}")
        print(f"  Avg {mean}")
        print(f"  StdDev {std}")

    print("---- Koniec ewolucji (zakończono sukcesem) ------")

    best_ind = tools.selBest(pop,1)[0]
    print(f"najlepiej dopasowany osobnik to {best_ind}, {best_ind.fitness.values}")

if __name__ == "__main__":
    main()
