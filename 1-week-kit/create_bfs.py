#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#


def bfs(n, m, edges, s):
    from collections import deque

    # Build graph
    graph = {}
    for num in range(1, n+1):
        graph[num] = set()
    for l, r in edges:
        graph[l].add(r)
        graph[r].add(l)
    
    reached = {}
    # Explore graph once
    frontier = deque([(s, 0)])
    seen = {s}

    while frontier:
        curr_node, curr_cost = frontier.popleft()
        for nbour in graph[curr_node]:
            if nbour not in seen:
                seen.add(nbour)
                reached[nbour] = curr_cost+6
                frontier.append((nbour, curr_cost+6))

    result = []
    for node in range(1, n+1):
        if s != node:
            result.append(reached.get(node, -1))
    
    return result
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()


def bfs(number_of_nodes, number_of_edges, edges, start_node):
    # Build graph as a dictionary where each key is a node and the value is a set of neighbors
    graph = {node: set() for node in range(1, number_of_nodes + 1)}
    for edge_start, edge_end in edges:
        graph[edge_start].add(edge_end)
        graph[edge_end].add(edge_start)
    
    # Dictionary to keep track of reached nodes and their costs
    reached = {}
    # Initialize the list as a queue with a tuple containing the start node and initial cost of 0
    queue = [(start_node, 0)]
    # Set to keep track of seen nodes
    seen = {start_node}

    # Process nodes in the queue
    while queue:
        current_node, current_cost = queue.pop(0)  # Replace deque popleft with list pop(0)
        # Go through the neighbors of the current node
        for neighbor in graph[current_node]:
            # If the neighbor hasn't been seen yet
            if neighbor not in seen:
                seen.add(neighbor)  # Mark as seen
                reached[neighbor] = current_cost + 6  # Update the cost to reach this neighbor
                queue.append((neighbor, current_cost + 6))  # Add to queue with updated cost

    # Prepare the result based on reached nodes, or -1 if not reachable
    result = []
    for node in range(1, number_of_nodes + 1):
        if node != start_node:
            result.append(reached.get(node, -1))  # Get the cost or -1 if not reachable
    
    return result
