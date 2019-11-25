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
    print("the max bandwidth path from vertex%d to vertex%d is : %s"%(s,t,wt[t]))
    return s,t,wt[t]
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
        #print(maxv)
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
    print("the max bandwidth path from vertex%d to vertex%d is : %s"%(s,t,wt[t]))
    return s, t, wt[t]
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
        s=[]
        while dad[w]!=-1:
            w=dad[w]
        #     s.append(w)
        # while(len(s)):
        #     v=s.pop()
        #     dad[v]=w
        return w
    def MakeSet(v):
        dad[v]=-1
        rank[v]=0

    #Build heap
    heap = Heap.MaxHeap()
    edges=g.alledges.items()
    #print(edges)
    for edge,w in edges:
        heap.H.append(edge)
        heap.D.append(w)
        heap.n+=1
    #print("finish init")
    #sort
    sorted_edge=[]
    heap.HeapSort()
    for i in range(1,heap.n+1):
        sorted_edge.append((heap.H[i],heap.D[i]))
    #print(sorted_edge)
    for i in range(g.v):
        MakeSet(i)
    #print("finish heap sort")
    MST=Graph.Graph(g.v)
    while(len(sorted_edge)):# and t not in path(MST,s,t)[0]:
        edge=sorted_edge.pop(-1)
        u=edge[0][0]
        v=edge[0][1]
        w=edge[1]
        ru=Find(u)
        rv=Find(v)
        if ru!=rv:
            Union(ru,rv)
            MST.addedge(u,v,w)
    #print(MST.adjlist)
    Path=path(MST,s,t)
    print("using Kruskal")
    print("the max bandwidth path from vertex%d to vertex%d is : %s"%(s,t,Path[1]))
    return s, t, Path[1]
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
            return path,wt[t]
        color[v]="grey"
        for edge in g.adjlist[v]:
                if color[edge[0]]=="white":
                    wt[edge[0]] = min(wt[v], edge[1])
                    path.append(edge[0])
                    path,wt[t]=DFS(g,edge[0],t,color,path,wt)
                    if t in path:
                        return path,wt[t]
        color[v]="black"
        path.remove(v)
        return path,wt[t]
#
# g=Graph.Graph(7)
# g.adjlist={0:[[1,12],[5,16],[6,14]],
#                      1:[[0,12],[2,10],[5,7]],
#                      2:[[1,10],[3,3],[5,6],[4,5]],
#                      3:[[2,3],[4,4]],
#                      4:[[3,4],[5,2],[6,8],[2,5]],
#                      5:[[0,16],[1,7],[2,6],[4,2],[6,9]],
#                      6:[[0,14],[5,9],[4,8]]}
# g.alledges[0,1]=12
# g.alledges[0,5]=16
# g.alledges[0,6]=14
# g.alledges[1,2]=10
# g.alledges[1,5]=7
# g.alledges[2,5]=6
# g.alledges[2,3]=3
# g.alledges[3,4]=4
# g.alledges[4,6]=8
# g.alledges[5,6]=9
# g.alledges[4,5]=2
# g.alledges[2,4]=5
# DijkstraNoheap(g,2,3)
# Dijkstraheap(g,2,3)
# Kruskal(g,2,3)
