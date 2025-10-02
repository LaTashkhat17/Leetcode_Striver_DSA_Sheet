class Solution(object):
    def maxSubArray(self, nums):
        curr_sum = max_sum = nums[0]
        for i in nums[1:]:
            curr_sum = max(i, curr_sum + i)
            max_sum = max(curr_sum, max_sum)
        return max_sum
obj1 = Solution()
print(obj1.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
        