class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # build prereq map
        premap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            premap[crs].append(pre)

        #store all visited courses, to catch cycles
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                #cycle detected
                return False
            if premap[crs] == []:
                #if it has no preq
                return True
           # Store courses currently being explored, so we can detect cycles
            visiting.add(crs)
            #traverse preq
            for pre in premap[crs]:
                if not dfs(pre):
                    return False #if cycle deted
            visiting.remove(crs) #that traversal is complete, incase there is a breakage and we are checking a disconnected course
            premap[crs] = [] # Mark this course as completely processed so we don't need to explore it again
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True