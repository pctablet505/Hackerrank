class DisjointSet:
    def __init__(self,N):
        self.parent=[i for i in range(N+1)]
        self.rank=[1 for _ in range(N+1)]
    def find(self,i):
        aux=i
        while aux !=self.parent[aux]:
            aux=self.parent[aux]
        rep=aux
        aux=i
        while aux!=rep:
            parent=self.parent[aux]
            self.parent[aux]=rep
            aux=parent
        return rep
    def union(self,x,y):
        rep_x=self.find(x)
        rep_y=self.find(y)
        if rep_x!=rep_y:
            if self.rank[rep_x]>=self.rank[rep_y]:
                self.parent[rep_y]=rep_x
                self.rank[rep_x]+=self.rank[rep_y]
            else:
                self.parent[rep_x]=rep_y
                self.rank[rep_y]+=self.rank[rep_x]


        



N,Q=map(int,input().split())
d=DisjointSet(N)
for _ in range(Q):
    q=input().split()
    if q[0]=='Q':
        t=d.find(int(q[1]))
        print(d.rank[t])
    else:
        d.union(int(q[1]),int(q[2]))


