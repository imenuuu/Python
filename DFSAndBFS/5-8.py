# DFS 예제, 스택을 이용
def dfs( graph, v, visited):
    # 현재 노드를 방문처리
    visited[v]=True
    print(v, end=' ')
    print(graph[v],visited)

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

graph = [
    [], # 0
    [2, 3, 8], # 1
    [1, 7], # 2
    [1, 4, 5], # 3
    [3, 5], # 4
    [3, 4], # 5
    [7], # 6
    [2, 6, 8], # 7
    [1, 7] # 8
]
# 1차원 리스트 초기화
visited = [False]*9

dfs(graph, 1, visited)