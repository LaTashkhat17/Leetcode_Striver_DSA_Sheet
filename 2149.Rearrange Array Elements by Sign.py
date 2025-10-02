class Solution(object):
    def func(self, nums):
        arr = [x for x in nums if x > 0]
        index = 1
        vis = [False] * len(nums)
        i = 0
        while(i < len(nums)):
            if(nums[i] < 0 and vis[i] == False):
                tmp = nums[i]
                nums[i] = nums[index]
                nums[index] = tmp
                vis[index] = True
                if(nums[i] >= 0): i += 1
                index += 2
                #print(nums)
            else: i += 1
        i = 0
        ind = 0
        for i in range(len(arr)):
            nums[ind] = arr[i]
            ind += 2


        return nums

# Read input from input.txt
with open('input.txt', 'r') as infile:
    # Read the numbers from the file and convert them into a list of integers
    nums = list(map(int, infile.read().split()))

# Create an instance of Solution
obj1 = Solution()

# Call the maxSubArray method with the input numbers
result = obj1.func(nums)

# Write the result to output.txt
with open('output.txt', 'w') as outfile:
    outfile.write(f"{result}\n")

