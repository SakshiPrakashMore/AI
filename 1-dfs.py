# DFS algorithm in Python


# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'1': set(['2', '3','4']),
         '2': set(['1', '5']),
         '3': set(['1','6']),
         '4': set(['1','7']),
         '5': set(['2','8']),
         '6': set(['3','9']),
         '7': set(['10', '4']),
         '8': set(['5']),
         '9': set(['6']),
         '10': set(['7'])}





dfs(graph, '1')



