from collections import OrderedDict
def find(u,parent):
    if parent[u]!=u:
        parent[u] = find(parent[u],parent)
    return parent[u]

def union(u,v,parent):
    pu = find(u,parent)
    pv = find(v,parent)
    if pu == pv:
        return
    parent[pv] = pu
def solve():
    n= int(input())
    parent = [i for i in range(int(1e5)+1)]
    # ranks = [0]*(int(1e5)+1)
    mapStrToNum = {}
    mapNumToStr ={}
    startTime = 0
    for _ in range(n):
        s1,s2 = input().split()    
        if s1 not in mapStrToNum:
            mapStrToNum[s1] = startTime
            mapNumToStr[startTime] = s1
            startTime+=1
        if s2 not in mapStrToNum:
            mapNumToStr[startTime] = s2
            mapStrToNum[s2] = startTime
            startTime+=1
        u = find(mapStrToNum[s1],parent)
        v = find(mapStrToNum[s2],parent)
        if u<v:
            union(u,v,parent)
        elif u>v:
            union(v,u,parent)
    counter = {}
    for key in mapStrToNum:
        leader = find(mapStrToNum[key],parent)
        if leader not in counter:
            counter[leader] = 0
        counter[leader] +=1
    print(len(counter))
    for e in OrderedDict(sorted(counter.items())):
        print(mapNumToStr[e], counter[e])

        
solve()
