def solution(graph, start):
    stack = [start]  # Initialize stack with the starting node
    visited = set()  # To keep track of visited nodes
    traversal = []   # To store the order of visited nodes

    while stack:
        node = stack.pop()  # Pop a node from the stack

        if node not in visited:
            visited.add(node)      # Mark the node as visited
            traversal.append(node) # Add it to the traversal order

            # Add unvisited neighbors to the stack
            # We use reversed() to ensure we visit nodes in the correct order
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal
