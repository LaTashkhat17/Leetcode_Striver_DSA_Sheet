class Solution(object):
    def twoSum(self, nums, target):
        arr = nums[:]
        arr.sort()
        l = 0
        r = len(arr) - 1
        while(l < r):
            if((arr[l] + arr[r]) < target): l += 1
            elif((arr[l] + arr[r]) > target): r -= 1
            else : 
                f = arr[l]
                s = arr[r]
                break
        r = len(nums)
        if(f == s):
            for i in range(0, r):
                if(nums[i] == f): 
                    fi = i
                    break
            for i in range(0, r):
                if(nums[i] == s and fi != i): 
                    si = i
                    return fi, si
        for i in range(0, r):
            if(nums[i] == f): fi = i
            if(nums[i] == s): si = i
        return fi,si
    def twoSumalt(self, nums, target):
        mp = {}
        for i in range(0, len(nums)):
            mp[i] = nums[i]
        for i in range(0, len(nums)):
            val = target - mp[i]
            for j in range(i + 1, len(nums)):
                if mp[j] == val:
                    return i, j
        
obj1 = Solution()
print(obj1.twoSum([2,7,11,15], 9))
print(obj1.twoSum([4,2,3], 6))
print(obj1.twoSum([3,2,4], 6))
print(obj1.twoSum([2,5,5,11], 10))