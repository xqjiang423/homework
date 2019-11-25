import time
import MBP
import randomgraph
import random
import sys
import csv
import datetime
def main():
    vnum=5000
    g=randomgraph.generatefirst(vnum)
    menu = int(sys.argv[1])
    trials = int(sys.argv[2])
    graphs = int(sys.argv[3])
    nowTime = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    # menu=1
    # trials=5
    f = open('graph'+str(menu)+nowTime+'.csv', 'w', encoding="utf-8",newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["graphNo","from","to","Dijkstra without heap", "Dijkstra with heap", "kruskal","flag"])
    for i in range(graphs):

        if menu==1:
            g = randomgraph.generatefirst(vnum)
        elif menu==2:
            g=randomgraph.generatesecond(vnum)
        print("finish generate")
        for i in range(trials):
            #print("---------------------------------------------------------")
            s=random.randint(0,vnum-1)
            t=random.randint(0,vnum-1)

            if s!=t:
                start_time=time.time()
                table1=MBP.DijkstraNoheap(g,s,t)
                end_time = time.time()
                time1=end_time - start_time
                #print("time1:%f" % (end_time - start_time))
                start_time = time.time()
                table2=MBP.Dijkstraheap(g, s, t)
                end_time = time.time()
                time2 = end_time - start_time
                #print("time2:%f" % (end_time - start_time))
                start_time = time.time()
                table3=MBP.Kruskal(g, s, t)
                end_time = time.time()
                time3 = end_time - start_time
                #print("time3:%f" % (end_time - start_time))
                if table1[2]==table2[2]==table3[2]:
                    flag="True"
                else:
                    flag="False"
                csv_writer.writerow([i,s,t,time1,time2,time3,flag])
    f.close()



if __name__=="__main__":
    main()
