import random
def randomSolution(tsp):
    cities=list(range(len(tsp)))
    solution=[]
    for i in range(len(tsp)):
        #here we select the random cities that are not visited in the list
        randomCity=cities[random.randint(0,len(cities)-1)]
        solution.append(randomCity)
        #append the visited city
        cities.remove(randomCity)#remove city form not visted list
    #return the solution genarated in random way
    return solution
def getpossibility(solution):#to get the possible ways from genarated solution of cities
    possibility=[]#new list to get possibilities
    for i in range(len(solution)):#swaping to get possibilities
        for j in range(i+1,len(solution)):
            possibleR=solution.copy()#coping the original solution
            possibleR[i]=solution[j]
            possibleR[j]=solution[i]
            possibility.append(possibleR)
    return possibility
def routeSales(tsp,solution):
    routeSales =0#to find cost on the route
    for i in range (len(solution)):
        routeSales+=tsp[solution[i-1]][solution[i]]#ex tsp[1][0] alike return expensise over the route
    return routeSales
def hillclimbing(tsp):
    currentsolution=randomSolution(tsp)#get solution on random starting point
    routes=getpossibility(currentsolution)#to get all routes over random routes
    bestRoute=bestroute(tsp,routes)#to get route and cost over the route
    return bestRoute
def bestroute(tsp,routes):
    #let routes[0] is the jbest solution for the given problem
    bestroute=routes[0]#primary route is the best routes
    bestSales=routeSales(tsp,routes[0])#primary price is the best price to asign
    for i in routes:#to check the cost over a each route
        sales=routeSales(tsp,i)
        if sales<bestSales:#if cost is lessthan best cost swaping route and cost over the solutions
            bestroute=i
            bestSales=sales
    return [bestSales,bestroute]#return best route and cost over the tsp
#main cost is declared in a nested list or in a array
tsp=[[0,35,45,60],
     [40,0,20,70],
     [47,72,0,15],
     [80,50,30,0]
      ]
route=hillclimbing(tsp)#calling function to find route over the best routes
print("genarated to best route is {0}".format(route[1]))
print(f"The less cost that can cover the cities is :{route[0]:.2f}")