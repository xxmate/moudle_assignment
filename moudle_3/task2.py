"""Write a function that does the following task.
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.
You must write an algorithm that runs in linear time and uses linear extra space.
Example 1:
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:
Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0."""

nums = [3,6,9,1]

def max_diff(nums):
    nums.sort()
    temp_max = 0
    if len(nums) < 2:
        return 0

    else:
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > temp_max:
                temp_max = nums[i+1] - nums[i]
        return temp_max

print(max_diff(nums))
