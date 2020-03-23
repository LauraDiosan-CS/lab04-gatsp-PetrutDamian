from random import seed

from src import Utils
from src.FileParser import FileParser
from src.GA import GA


class Console:
    def run(self):
        file = input("Input file:")
        nrGen = input("Number of generations:")
        nrPop = input("Population number:")
        self.compute(file, int(nrGen), int(nrPop))

    def compute(self, file, nrGen, nrPop):
        matrix, n = FileParser.parseMatrix(file)

        problParam = {}
        problParam['noNodes'] = n
        problParam['matrix'] = matrix
        problParam['function'] = Utils.evaluateTsp

        gaParam = {}
        gaParam['noGen'] = nrGen
        gaParam['popSize'] = nrPop
        seed(1)

        ga = GA(gaParam,problParam)
        ga.initialisation()
        ga.evaluation()

        allBestFitnesses = []
        for g in range(gaParam['noGen']):
            ga.oneGenerationElitism()
            bestSolY = ga.bestChromosome().fitness
            allBestFitnesses.append(bestSolY)

        print("Best fitnesses across all generations:")
        print(allBestFitnesses)
        print("\nBest current chromosome")
        print(ga.bestChromosome().repres)
        print("Best fitness")
        print(ga.bestChromosome().fitness)




