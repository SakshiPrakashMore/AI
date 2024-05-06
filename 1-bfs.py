# BFS algorithm in Python


import collections

# BFS algorithm
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {1: [ 2,3,4], 2: [1,5], 3: [1,6], 4: [1, 7],5:[2,8],6:[3,9],7:[4,10],8:[5],9:[6],10:[7]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 1)
    



