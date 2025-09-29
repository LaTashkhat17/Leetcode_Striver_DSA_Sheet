class Solution(object):
    def fib(self, nums):
        cnt = 0
        size = len(nums)
        for i in range(size - 1):
            if nums[i] > nums[i + 1]:
                cnt += 1
        if nums[size - 1] > nums[0]:
            cnt += 1
        if cnt > 1:
            return False
        else:
            return True

    
obj1 = Solution()
nums = [3,4,5,1,2]
print(obj1.fib(nums))
        