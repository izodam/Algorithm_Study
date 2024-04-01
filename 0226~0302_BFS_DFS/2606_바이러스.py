# 2606번
def dfs(v):
    stack = [v]
    visited[v] = 1

    while stack:
        n = stack.pop()
        for next_node in graph[n]:
            if not visited[next_node]:
                visited[next_node] = 1
                stack.append(next_node)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    # 양방향
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
dfs(1)

# 방문한 노드는 1로 표시했으므로
# 연결된 컴퓨터는 visit의 합 - 1 (1번 컴퓨터 빼고)
print(sum(visited)-1)