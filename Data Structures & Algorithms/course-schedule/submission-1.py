class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if premap[crs] == []:
                return True
            visited.add(crs)
            for preq in premap[crs]:
                if not dfs(preq):
                    return False
            visited.remove(crs)
            premap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True


'''
1. Build a prerequisites mapp {crs: [preq]}
2. visited - to catch cycles
3. DFS(course)
    check if course in visited  to detect cyles
    then base case to check if it has any preq, if it doesnt return, true. menaning it can be completed
    then mark course has visited
    Traverse through the preqrequisites of that course:
        then call dfs on each preq, if its not dfs(cycle was detected), return False
    remove course from visted -- because traversal for that course has been completed
    mark course has completed, so if we check in hashmap for another traversal, makes it quicker rather than repeated



'''