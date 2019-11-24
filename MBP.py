import Graph
import randomgraph
import Heap

def DijkstraNoheap(g,s,t):
    n=g.v
    status={}#unseen, intree, fringe
    wt={}
    dad={}
    for v in range(n):
        status[v]="unseen"
    status[s]="intree"
    for edge in g.adjlist[s]:
        status[edge[0]]="fringe"
        wt[edge[0]]=edge[1]
        dad[edge[0]]=s
    while status[t]!="intree":
        #pick the max wt[v]
        max=0
        for v,w in wt.items():
            if w>max and status[v]=="fringe":
                max=w
                maxv=v
        status[maxv]="intree"
        edges=g.adjlist[maxv]
        for edge in edges:
            w=edge[0]
            if status[w]=="unseen":
                status[w]="fringe"
                dad[w]=maxv
                wt[w]=min(wt[maxv],edge[1])
            elif status[w]=="fringe" and wt[w]<min(wt[maxv],edge[1]):
                dad[w]=maxv
                wt[w]=min(wt[maxv],edge[1])
    print("using Dijkstra without heap")
    print("the max bandwidth path of vertex%d is : %d"%(t,wt[t]))
    # path=[]
    # repath=[]
    # while t!=s:
    #     path.append(t)
    #     t=dad[t]
    # path.append(s)
    # while(path):
    #     repath.append(path.pop(-1))
    # print(repath)

def Dijkstraheap(g,s,t):
    n=g.v
    status={}#unseen, intree, fringe
    wt={}
    dad={}
    heap=Heap.MaxHeap()
    for v in range(n):
        status[v]="unseen"
    status[s]="intree"

    for edge in g.adjlist[s]:
        status[edge[0]]="fringe"
        wt[edge[0]]=edge[1]
        dad[edge[0]]=s
        heap.Insert(edge[0],edge[1])
    while status[t]!="intree":
        #pick the max wt[v]
        maxv=heap.Max()[0]
        status[maxv]="intree"
        heap.Delete(maxv)
        edges=g.adjlist[maxv]
        for edge in edges:
            w=edge[0]
            if status[w]=="unseen":
                status[w]="fringe"
                dad[w]=maxv
                wt[w]=min(wt[maxv],edge[1])
                heap.Insert(w, wt[w])
            elif status[w]=="fringe" and wt[w]<min(wt[maxv],edge[1]):
                dad[w]=maxv
                wt[w]=min(wt[maxv],edge[1])
                heap.Delete(w)
                heap.Insert(w, wt[w])
    print("using Dijkstra with heap")
    print("the max bandwidth path of vertex%d is : %d"%(t,wt[t]))
    # path=[]
    # repath=[]
    # while t!=s:
    #     path.append(t)
    #     t=dad[t]
    # path.append(s)
    # while(path):
    #     repath.append(path.pop(-1))
    # print(repath)

def Kruskal(g,s,t):
    rank={}
    dad={}
    def Union(u,v):
        if rank[u]>rank[v]:
            dad[v]=u
        elif rank[u]<rank[v]:
            dad[u]=v
        else:
            dad[v]=u
            rank[u]+=1
    def Find(v):
        w=v
        while dad[w]!=-1:
            w=dad[w]
        return w
    def MakeSet(v):
        dad[v]=-1
        rank[v]=0

    #Build heap
    heap = Heap.MaxHeap()
    for edge,w in g.alledges().items():
        heap.Insert(edge,w)
    #sort
    sorted_edge=[]
    for i in range(heap.n):
        max=heap.Max()
        sorted_edge.append(max)
        heap.Delete(max[0])

    for i in range(g.v):
        MakeSet(i)
    T=[]
    MST=Graph.Graph(g.v)
    while(len(sorted_edge)):
        edge=sorted_edge.pop(0)
        u=edge[0][0]
        v=edge[0][1]
        w=edge[1]
        ru=Find(u)
        rv=Find(v)
        if ru!=rv:
            Union(ru,rv)
            MST.addedge(u,v,w)
    Path=path(MST,s,t)
    print("using Kruskal")
    print("the max bandwidth path of vertex%d is : %d"%(t,Path[1]))
    # print(Path[0])

def path(g,s,t):
    path=[]
    color={}
    wt={}
    for i in range(g.v):
        color[i]="white"
        wt[i]=10000
    path.append(s)
    DFS(g,s,t,color,path,wt)
    return path,wt[t]

def DFS(g,v,t,color,path,wt):
    if v==t:
        #path.append(t)
        #wt[t] = min(wt[v],g.alledges())
        return path,wt[t]
    color[v]="grey"
    for edge in g.adjlist[v]:
        #if edge[0]==v:
            if color[edge[0]]=="white":
                wt[edge[0]] = min(wt[v], edge[1])
                path.append(edge[0])
                path,wt[t]=DFS(g,edge[0],t,color,path,wt)
                if t in path:
                    return path,wt[t]
    color[v]="black"
    path.remove(v)
    return path,wt[t]

# g=Graph.Graph(7)
# g.adjlist={0:[[1,12],[5,16],[6,14]],
#                      1:[[0,12],[2,10],[5,7]],
#                      2:[[1,10],[3,3],[5,6],[4,5]],
#                      3:[[2,3],[4,4]],
#                      4:[[3,4],[5,2],[6,8],[2,5]],
#                      5:[[0,16],[1,7],[2,6],[4,2],[6,9]],
#                      6:[[0,14],[5,9],[4,8]]}
# DijkstraNoheap(g,1,5)
# Dijkstraheap(g,1,5)
# Kruskal(g,1,5)
