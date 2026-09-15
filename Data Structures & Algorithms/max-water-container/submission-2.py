class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxA = 0

        while l < r:
            length = min(heights[l],heights[r])
            width = r - l
            area = length * width
            maxA = max(maxA, area)
            if heights[l] > heights[r]:
                r -=1
            else:
                l +=1
        return maxA
