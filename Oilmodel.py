from gurobipy import *
def solve(Olive,oil,a,s,c,l,u,p,d):

    # Model
    m=Model("Production of Olive Oil")

    #Decision Variables
    x={}
    for j in oil:
        for i in Olive:
            x[i,j]=m.addVar(vtype=GRB.CONTINUOUS, name='x_%s,%s' %(i,j))
    y={}
    for j in oil:
        y[j]=m.addVar(vtype=GRB.CONTINUOUS, name='y_%s' %j)


    m.update()

    #Objective
    m.setObjective(quicksum(p[j]*y[j] for j in oil)-(quicksum(quicksum(c[i]*x[i,j] for i in mixture)for j in oil)),GRB.MAXIMIZE)

    # Add Constraints
    for j in oil:
        m.addConstr(quicksum(a[i]*x[i,j] for i in Olive)>=l[j]*y[j])

    for j in oil:
        m.addConstr(quicksum(s[i]*x[i,j] for i in Olive)<=u[j]*y[j])

    for j in oil:
        m.addConstr(quicksum(c[i]*x[i,j] for i in Olive)<=p[j]*y[j])

    for j in oil:
        m.addConstr(y[j]>=d[j])

    for i in Olive:
        m.addConstr(quicksum(x[i,j] for j in oil)<=1200)

    m.addConstr(quicksum(y[j] for j in oil)<=10000)

    m.optimize()

    print("Profit %g" %m.objVal)

    for j in oil:
        print("Amount of olive oil %s= %g" %(j,y[j].x)
