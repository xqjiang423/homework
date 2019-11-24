
class MaxHeap:
    def __init__(self):
        self.H=[]
        self.D=[]
        self.n=0

    def Max(self):
        if self.n==0:
            return("the heap is empty")
        else:
            return (self.H[0],self.D[0])

    def swap(self,i,j):
        temp = self.D[i]
        self.D[i] = self.D[j]
        self.D[j] = temp

        temp = self.H[i]
        self.H[i] = self.H[j]
        self.H[j] = temp

    def Insert(self,x,w):
        self.H.append(x)
        self.D.append(w)
        i=self.n
        self.n += 1
        while self.D[int(i/2)]<self.D[i] and i>=1:#push up
            self.swap(int(i/2),i)
            i=int(i/2)

    def Delete(self,h):
        h=self.H.index(h)
        self.H[h]=self.H[self.n-1]
        self.D[h]=self.D[self.n-1]
        if self.n>=1:
            self.n-=1
        self.fixHeap(h)
        del self.H[self.n]
        del self.D[self.n]

    def fixHeap(self,h):
        # if h>=1 and self.D[int(h/2)]<self.D[h]:
        while self.D[int(h / 2)] < self.D[h]:
            self.swap(int(h / 2), h)
            h = int(h / 2)
        # else:
        while 2 * h <= self.n - 1 and (self.D[h] < self.D[2 * h] or self.D[h] < self.D[2 * h + 1]):
            if (2 * h == self.n - 1) or (self.D[2 * h] > self.D[2 * h + 1]):
                self.swap(h, 2 * h)
                h = h * 2
            else:
                self.swap(h, 2 * h + 1)
                h = h * 2 + 1


#a=MaxHeap()
#a.Insert([0,1],2)

#print(a.H)
#a.Delete([0,1])
#print(a.H)
#print(a.D)
#print(a.Max())
