import array
import random
import numpy
import pandas as pd
from deap import algorithms
from deap import base
from deap import creator
from deap import tools

#leemos los datos provenientes del dataset

data=pd.read_csv("haberman.csv",sep=",")
creator.create("FitnessMax", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)
toolbox = base.Toolbox()

#colocamos en el grupo de mujeres que se someten a una operación por cancer de mama entre 21 y 50 años
toolbox.register("attr_bool", random.randint, 21, 80)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 10)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evacancer(individual,edad,t_opera,ganglios_auxiliares):

        #vemos cuantas mujeres sometidas a operación generaron ganglios cancerosos en el grupo de 10 mujeres
        aux=0
        gnp=numpy.array(ganglios_auxiliares)
        enp=numpy.array(edad)
        indi=numpy.array(individual)
        for a in range(0,len(individual)-1):
            if individual[a] in edad and t_opera[a]>60 and edad[a]<35:
                #print(individual)
                aux+=gnp[a]
        #ya definido los ganglios generados entre todas las mujeres podemos decir que si 
        # sumados todos los ganglios cancerosos el numero es mayo o igual que 10 
        # el conjunto de mujeres que no estaba en el rango de edad para generar ganglios cancerosos, generara 1 
        # caso contrario no generara ningun ganglio
        # y en un caso devolvemos la mujer de mas edad o la mas joven 
        if aux>=10:
            return indi.max(),
        else:
            return indi.min(),
                

toolbox.register("evaluate", evacancer,edad=data["edad"],t_opera=data["year"],ganglios_auxiliares=data["auxilia"])
toolbox.register("mate", tools.cxUniform, indpb=0.5)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    #random.seed(64)
    
    pop = toolbox.population(n=1000)
    #print(pop)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    
    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=20, 
                                   stats=stats, halloffame=hof, verbose=True)
    
    

    return pop, log, hof

if __name__ == "__main__":
    main()