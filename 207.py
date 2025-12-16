from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.build_graph(numCourses, prerequisites)
        state = [0] * numCourses

        for course in range(numCourses):
            if state[course] == 0 and self.has_cycle(course, graph, state):
                return False

        return True

    def build_graph(self, numCourses: int, prerequisites: List[List[int]]):
        graph = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        return graph

    def has_cycle(self, u: int, graph, state) -> bool:
        state[u] = 1

        for v in graph[u]:
            if state[v] == 1:
                return True
            if state[v] == 0 and self.has_cycle(v, graph, state):
                return True

        state[u] = 2
        return False 
        
        
solution = Solution()
print(solution.canFinish(2, [[1,0]]))
