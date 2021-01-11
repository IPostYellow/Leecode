def choice(d, ans_set):
    min, minpos = float('inf'), -1
    for i in range(1, len(d)):
        if d[i] < min and ans_set[i] == False:
            min = d[i]
            minpos = i
    return minpos


def dijstral(Edge, start):
    # eadge是邻接矩阵
    d = [0] * len(Edge)
    path = [-1] * len(Edge)
    ans_set = [False] * len(Edge)
    for i in range(len(d)):
        d[i] = Edge[start][i]
        if (i != start and d[i] < float('inf')):
            path[i] = d[i]
    ans_set[start] = True
    for i in range(1, len(Edge)):
        postion = choice(d, ans_set)
        ans_set[postion] = True
        for j in range(len(Edge)):
            if ans_set[j] == False and (d[postion] + Edge[postion][j] < d[j]):
                d[j] = d[postion] + Edge[postion][j]
                path[j] = postion


Edge = [
    [0, 50, 10, float('inf'), 70, float('inf')],
    [float('inf'), 0, 15, float('inf'), 10, float('inf')],
    [20, float('inf'), 0, 15, float('inf'), float('inf')],
    [float('inf'), 20, float('inf'), 0, 35, float('inf')],
    [float('inf'), float('inf'), float('inf'), 30, 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), 3, float('inf'), 0]
]
dijstral(Edge, 0)
from collections import defaultdict

dic = defaultdict(dict)
for i in range(len(Edge)):
    for j in range(len(Edge)):
        if i != j and Edge[i][j] != float('inf'):
            dic[i][j] = Edge[i][j]
print(dic)


def dijstrals(start, dic,n):
    d=[0]*len()