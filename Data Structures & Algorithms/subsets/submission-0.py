class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(current_path, start):
            res.append(current_path.copy())

            for i in range(start, len(nums)):
                current_path.append(nums[i])
                backtrack(current_path, i + 1)
                current_path.pop()
        backtrack([], 0)
        return res