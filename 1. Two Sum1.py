class Solution(object):
    def twoSum(self, nums, target):
        arr = nums
        arr.sort()
        l = 0
        r = len(arr) - 1
        while(l < r):
            if((arr[l] + arr[r]) < target): l += 1
            elif((arr[l] + arr[r]) > target): r -= 1
            else : 
                f = arr[l]
                s = arr[r]
                return f,s
        for i in range(r + 1):
            if(nums[i] == f): fi = i
            if(nums[i] == s): si = i
        return fi,si


        
obj1 = Solution()
print(obj1.twoSum([2,7,11,15], 9))