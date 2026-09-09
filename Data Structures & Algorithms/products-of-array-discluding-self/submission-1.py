class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1 for i in range(len(nums))]
        post = [1 for i in range(len(nums))]
        res  = [1 for i in range(len(nums))]
        # create pre
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]
       
        for i in range(len(nums)):
            res[i] = pre[i] * post[i]
        return res

