# 207. Course Schedule

def canFinish1(self, numCourses, prerequisites):
    forward = {i: set() for i in xrange(numCourses)}
    backward = collections.defaultdict(set)
    for i, j in prerequisites:
        forward[i].add(j)
        backward[j].add(i)
    queue = collections.deque([node for node in forward if len(forward[node]) == 0])
    while queue:
        node = queue.popleft()
        for neigh in backward[node]:
            forward[neigh].remove(node)
            if len(forward[neigh]) == 0:
                queue.append(neigh)
        forward.pop(node)
    return not forward  # if there is cycle, forward won't be None


def canFinish3(self, numCourses, prerequisites):
    forward = {i: set() for i in xrange(numCourses)}
    backward = collections.defaultdict(set)
    for i, j in prerequisites:
        forward[i].add(j)
        backward[j].add(i)
    stack = [node for node in forward if len(forward[node]) == 0]
    while stack:
        node = stack.pop()
        for neigh in backward[node]:
            forward[neigh].remove(node)
            if len(forward[neigh]) == 0:
                stack.append(neigh)
        forward.pop(node)
    return not forward


# Topological Sort
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        n = numCourses
        pos = [[] for i in range(n)]
        degree = [0]*n
        for j,i in prerequisites:
            pos[i].append(j)
            degree[j] += 1

        l = []
        for i in range(n):
            if degree[i] == 0:
                l.append(i)

        for i in l:
            for j in pos[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    l.append(j)
        return len(l) == n


# 210. Course Schedule II

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        n = numCourses
        forward = {i:set() for i in range(n)}
        backward = collections.defaultdict(set)
        for i,j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)

        queue = collections.deque([])
        for i in range(n):
            if len(forward[i]) == 0:
                queue.append(i)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for i in backward[node]:
                forward[i].remove(node)
                if len(forward[i]) == 0:
                    queue.append(i)
            backward.pop(node)
        if len(res) == n:
            return res
        else:
            return []
