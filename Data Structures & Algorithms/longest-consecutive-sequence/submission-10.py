class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maximum_count = 0
        count = 0
        numset = set(nums)
        def dfs(n):
            length = 1
            while n + 1 in numset:
                n += 1
                length += 1
            return length
        
        for i in range(len(nums)):
            if nums[i] - 1 not in numset:
                count = dfs(nums[i])
                maximum_count = max(maximum_count, count)
        return maximum_count