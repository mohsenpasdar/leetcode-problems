from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.build_graph(numCourses, prerequisites)
        state = [0] * numCourses
        output = []
        
        for course in range(numCourses):
            if state[course] == 0 and self.has_cycle(course, graph, state, output):
                return []
        
        output.reverse()
        return output

    def build_graph(self, numCourses: int, prerequisites: List[List[int]]):
        graph = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        return graph

    def has_cycle(self, u: int, graph, state, output) -> bool:
        state[u] = 1
        
        for v in graph[u]:
            if state[v] == 1:
                return True
            if state[v] == 0 and self.has_cycle(v, graph, state, output):
                return True

        state[u] = 2
        output.append(u)
        return False 
        
        
solution = Solution()
# print(solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))


class Solution2:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
            
             
        queue = deque()
        output = []
            
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
                
        while queue:
            course = queue.pop()
            output.append(course)
            
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.appendleft(neighbor)
        
        if len(output) == numCourses:
            return output
        else:
            return []

        
solution2 = Solution2()
print(solution2.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))