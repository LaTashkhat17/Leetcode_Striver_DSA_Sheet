class Solution(object):
    def sortColors(self, nums):
        l = 0
        for i in range(l, len(nums)):
            
            if(nums[i] == 0):
                nums[i] = nums[l]
                nums[l] = 0
                l += 1
        for i in range(l, len(nums)):
            
            if(nums[i] == 1):
                nums[i] = nums[l]
                nums[l] = 1
                l += 1
        return nums  
    def sortColorsalt(self, nums):  
        c0 = nums.count(0)
        c1 = nums.count(1)
        c2 = nums.count(2)
        nums[:]  = [0] * c0 + [1] * c1  + [2] * c2
        return nums;  

obj1 = Solution()
print(obj1.sortColorsalt([2,0,1]))