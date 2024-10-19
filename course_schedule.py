"""
How to find a problem is graph? Draw it.
Once the problem type is graph. Build the graph.
We can use in-degree array where ith index is the node number (or dependent node), and the value at ith index is
in-degree of that node, meaning how many courses need to be finished to finish that node.
For the BFS, we need to start with independent courses, that is whose in-degree is 0. And add them to the BFS queue.
Process a node means, the course is complete, and the in-degree of courses dependent on that current course is reduced by
1. Once the queue is empty, process the next batch of independent nodes.
Since it is the search, we could use hmap (or adjacent list), with independent course is the key and list of dependent courses
are the value. Independent course is the search term.
This is called topological sort:
    Compute the in-degree (number of incoming edges) for each vertex.
    Start with nodes that have an in-degree of 0 (no dependencies).
    Remove these nodes from the graph, add them to the result, and reduce the in-degree of their neighbors.
    Repeat until all nodes are processed.
If all the nodes are not processed, then there is a cycle in the graph.
To answer in how many semesters will you be able to complete the course? then keep track of level.
TC: O(E) to process prerequisites + O(V) number of courses + O(V+E) BFS queue  and SC: O()
"""

from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0 for _ in range(numCourses)]
        hmap = {}

        for pre in prerequisites:
            # pre[0] is dependent and pre[1] is independent

            # identify the dependencies for each course
            in_degree[pre[0]] += 1

            # we search for independent course thus that would be key
            # and list of dependent course would be value
            if pre[1] not in hmap:
                hmap[pre[1]] = []
            hmap[pre[1]].append(pre[0])

        q = deque()
        count = 0
        # go over all the courses
        for i in range(numCourses):
            # add nodes whose in-degree is 0
            if in_degree[i] == 0:
                q.append(i)
                # increment count since this course is processed
                count += 1

        # check if all coureses can be completed
        if count == numCourses:
            return True
        if not q:
            return False

        while q:
            curr = q.popleft()
            # Find dependent course of current independent course
            # it is possible that key does not exists in hmap
            # for that define the list and update it if found
            depe_course = []
            if curr in hmap:
                depe_course = hmap[curr]
            # if have dependencies then decrement the in-degree
            if depe_course:
                for d in depe_course:
                    in_degree[d] -= 1
                    # if in-degree is 0, add to queue
                    if in_degree[d] == 0:
                        q.append(d)
                        count += 1
                        if count == numCourses:
                            return True

        return False
