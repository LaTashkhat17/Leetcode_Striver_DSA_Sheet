class Solution(object):
    def func(self, nums):
        t = -1
        for i in range(len(nums) - 2, -1, -1):
            print(i)
            if(nums[i] < nums[i + 1]):
                t = i
                break
        nums[t + 1:len(nums)] = nums[t + 1:len(nums)][::-1]
        for i in range(t + 1, len(nums)):
            if(nums[i] > nums[t]):
                tmp = nums[t]
                nums[t] = nums[i]
                nums[i] = tmp
                break
        

        return t, nums

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

