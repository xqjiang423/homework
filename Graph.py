import random

class Graph:
    def __init__(self,vnum):
        self.v=vnum
        self.adjlist={}
        self.e = 0

    def randominit(self):
        for i in range(self.v):
            weight = random.randint(1, 1000)
            self.adjlist.setdefault(i,[]).append([(i+1)%self.v,weight])
            self.adjlist.setdefault((i+1)%self.v,[]).append([i,weight])
            self.e+=1

    def addedge(self,u,v,weight=random.randint(1, 1000)):
        #pass
        if self.v==0:
            raise ValueError("can not add edge to the empty graph!")
        self.adjlist.setdefault(u,[]).append([v,weight])
        self.adjlist.setdefault(v,[]).append([u,weight])
        self.e+=1

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

    def alledges(self):
        edges={}
        for key, item in self.adjlist.items():
            for edge in item:
                if (edge[0], key) not in list(edges.keys()):
                    edges[key,edge[0]]=edge[1]
        return edges