import time
import MBP
import randomgraph
import Graph
import Heap
import random
def main():
    vnum=5000
    g=randomgraph.generatefirst(vnum)
    #g=randomgraph.generatesecond(vnum)
    print("finish generate")
    s=random.randint(0,vnum-1)
    t=random.randint(0,vnum-1)
    if s!=t:
        start_time=time.time()
        MBP.DijkstraNoheap(g,s,t)
        end_time = time.time()
        print("time1:%f" % (end_time - start_time))
        start_time = time.time()
        MBP.Dijkstraheap(g, s, t)
        end_time = time.time()
        print("time2:%f" % (end_time - start_time))
        start_time = time.time()
        MBP.Kruskal(g, s, t)
        end_time = time.time()
        print("time3:%f" % (end_time - start_time))

if __name__=="__main__":
    main()
