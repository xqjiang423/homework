
class MaxHeap:
    def __init__(self):
        self.H=[-1]
        self.D=[10000]
        self.n=0

    def Max(self):
        if self.n==0:
            return("the heap is empty")
        else:
            return (self.H[1],self.D[1])

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
        self.n += 1
        i=self.n
        while self.D[int(i/2)]<self.D[i] and i>1:#push up
            self.swap(int(i/2),i)
            i=int(i/2)

    def Delete(self, h):
        h = self.H.index(h)
        self.H[h] = self.H[self.n]
        self.D[h] = self.D[self.n]
        del self.H[self.n]
        del self.D[self.n]
        if h<self.n:
            if self.n >= 1:
                self.n -= 1
            self.fixHeap2(h, self.n)
        else:
            self.n-=1


    def fixHeap2(self, h, end):
        if h>1 and self.D[int(h/2)]<self.D[h]:
            while self.D[int(h / 2)] < self.D[h]:
                self.swap(int(h / 2), h)
                h = int(h / 2)
        else:
            while 2 * h <= end:
                if 2 * h < end and (self.D[h] < self.D[2 * h] or self.D[h] < self.D[2 * h + 1]):
                    if (self.D[2 * h] > self.D[2 * h + 1]):
                        self.swap(h, 2 * h)
                        h = h * 2
                    else:
                        self.swap(h, 2 * h + 1)
                        h = h * 2 + 1
                elif (2 * h == end):
                    self.swap(h, 2 * h)
                    h = h * 2
                else:
                    break

    def fixHeap(self,h,end):
        maxVal = h
        left = 2 * h
        right = 2 * h + 1

        if (left < end and self.D[left]> self.D[maxVal]):
            maxVal = left
        if (right < end and self.D[right] > self.D[maxVal]):
            maxVal = right
        if (maxVal != h):
            self.swap(maxVal,h)
            self.fixHeap(maxVal, end)
    def HeapSort(self):
        L=self.D
        L_length = len(L)-1
        first_sort_count = int(L_length / 2)
        #first build a maxheap
        for i in range(first_sort_count):
            self.fixHeap(first_sort_count - i, L_length)
        #print(self.D)
        for i in range(L_length - 1):
            self.swap(1, L_length - i)
            self.fixHeap(1, L_length - i - 1)

#
# a=MaxHeap()
# a.Insert([0,1],2)
# a.Insert([0,2],3)
# a.Insert([0,4],1)
# a.Insert([0,3],4)
# print(a.H)
# a.Delete([0,1])
# print(a.H)
# print(a.D)
# print(a.Max())
