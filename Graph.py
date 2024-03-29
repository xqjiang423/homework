import random

class Graph:
    def __init__(self,vnum):
        self.v=vnum
        self.adjlist={}
        for i in range(self.v):
            self.adjlist.setdefault(i,[]).append(0)
            self.adjlist[i].remove(0)
        self.e = 0
        self.alledges={}

    def randominit(self):
        for i in range(self.v):
            weight = (random.random()+0.01)*1000
            self.adjlist.setdefault(i,[]).append([(i+1)%self.v,weight])
            self.adjlist.setdefault((i+1)%self.v,[]).append([i,weight])
            self.e+=1
            self.alledges[i, (i+1)%self.v] = weight

    def addedge(self,u,v,weight):
        #pass
        if self.v==0:
            raise ValueError("can not add edge to the empty graph!")
        self.adjlist.setdefault(u,[]).append([v,weight])
        self.adjlist.setdefault(v,[]).append([u,weight])
        self.e+=1
        self.alledges[u,v]=weight

    def edgeexist(self,u,v):
        flag=False
        for edges in self.adjlist[v]:
            if u == edges[0]:
                flag=True
        return flag

    def edgenum(self):
        return self.e

    def getdegree(self):
        degree = 0
        for value in self.adjlist.values():
            degree += len(value)
        return degree
