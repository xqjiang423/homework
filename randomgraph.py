import Graph
import random

def generatefirst(vnum):
    #vnum = 5000
    g = Graph.Graph(vnum)
    g.randominit()
    while (g.e < vnum*6/2):
        u = random.randint(0, vnum - 1)
        v = random.randint(0, vnum - 1)
        if u!=v and not g.edgeexist(u,v):
            w=(random.random()+0.01)*1000
            g.addedge(u,v,w)
    degree=0
    for value in g.adjlist.values():
        degree += len(value)
    # a = random.randint(0, vnum - 1)
    # print(a)
    # print(g.adjlist[a])
    # print(len(g.alledges()))
    # print(g.getdegree()/vnum)
    return g

def generatesecond(vnum):
    #vnum = 5000
    g = Graph.Graph(vnum)
    g.randominit()
    for i in range(vnum):
        #print(i)
        for j in range(i+1,vnum):
            prob=random.randint(0,100)
            if prob <= 20 and not g.edgeexist(i,j):
                w=(random.random() + 0.01) * 1000
                g.addedge(i,j,w)
    # a = random.randint(0, vnum - 1)
    # print(a)
    # print(len(g.adjlist[a]))
    # print(g.getdegree()/vnum)
    return g

#generatefirst(7)
#generatesecond()

