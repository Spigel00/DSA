"""
LeetCode Problem: 217. Contains Duplicate
Difficulty: Easy
URL: https://leetcode.com/problems/contains-duplicate/

Problem Description:
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        Approach: Hash Set
        
        Time Complexity: O(n) - where n is the length of nums
        Space Complexity: O(n) - for the set to store elements
        
        Algorithm:
        1. Use a set to keep track of seen numbers
        2. Iterate through the array
        3. If current number is already in set, return True (duplicate found)
        4. Otherwise, add the number to the set
        5. If we finish the loop without finding duplicates, return False
        
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Alternative Solutions:

class AlternativeSolutions:
    def containsDuplicate_sorting(self, nums):
        """
        Approach: Sorting
        Time Complexity: O(n log n)
        Space Complexity: O(1) if sorting in-place
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    
    def containsDuplicate_builtin(self, nums):
        """
        Approach: Using built-in functions
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return len(nums) != len(set(nums))
       