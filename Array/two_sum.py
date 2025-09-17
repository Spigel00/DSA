class Solution(object):
    # ========================================
    # ORIGINAL SOLUTION BY USER
    # ========================================
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        Original approach: Brute Force (Nested Loops)
        Time: O(n²), Space: O(1)
        Straightforward approach - checks all pairs!
        """
        for i in range(len(nums)-1):
            for j in range(1,len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    return [i,j]

    # ========================================
    # ALTERNATIVE SOLUTIONS
    # ========================================
    
    def twoSum_hashmap_onepass(self, nums, target):
        """
        Alternative 1: Hash Map - One Pass (Most Optimal!)
        Time: O(n), Space: O(n)
        Best approach for interviews - single pass through array
        """
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        
        return []  # No solution found

    def twoSum_hashmap_twopass(self, nums, target):
        """
        Alternative 2: Hash Map - Two Pass
        Time: O(n), Space: O(n)
        Easier to understand - build map first, then search
        """
        # First pass: build the hash map
        num_map = {}
        for i, num in enumerate(nums):
            num_map[num] = i
        
        # Second pass: find complement
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map and num_map[complement] != i:
                return [i, num_map[complement]]
        
        return []  # No solution found

    def twoSum_brute_force_optimized(self, nums, target):
        """
        Alternative 3: Optimized Brute Force
        Time: O(n²), Space: O(1)
        Improved version of your approach - avoids redundant checks
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # Start from i+1 to avoid duplicates
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []  # No solution found

    def twoSum_sorting_twopointer(self, nums, target):
        """
        Alternative 4: Sorting + Two Pointers
        Time: O(n log n), Space: O(n)
        Good for finding if solution exists, but need to track original indices
        """
        # Create list of (value, original_index) pairs
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        # Sort by value
        indexed_nums.sort()
        
        left, right = 0, len(indexed_nums) - 1
        
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            
            if current_sum == target:
                # Return original indices
                return sorted([indexed_nums[left][1], indexed_nums[right][1]])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []  # No solution found


# ========================================
# TESTING THE SOLUTIONS
# ========================================
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([2, 5, 5, 11], 10, [1, 2]),
        ([1, 2, 3, 4, 5], 9, [3, 4]),
        ([-1, -2, -3, -4, -5], -8, [2, 4])
    ]
    
    print("Testing all Two Sum solutions:")
    print("=" * 60)
    
    for nums, target, expected in test_cases:
        print(f"\nTest: {nums}, target={target} -> Expected: {expected}")
        
        # Test original solution
        try:
            result1 = solution.twoSum(nums.copy(), target)
            if result1 is None:
                result1 = []
            # Sort for comparison since order might differ
            result1_sorted = sorted(result1) if result1 else []
            expected_sorted = sorted(expected) if expected else []
            print(f"Original (brute force):     {result1} ✅" if result1_sorted == expected_sorted else f"Original (brute force):     {result1} ❌")
        except:
            print(f"Original (brute force):     Error ❌")
        
        # Test alternative solutions
        result2 = solution.twoSum_hashmap_onepass(nums.copy(), target)
        result2_sorted = sorted(result2) if result2 else []
        print(f"Hash Map (one pass):        {result2} ✅" if result2_sorted == expected_sorted else f"Hash Map (one pass):        {result2} ❌")
        
        result3 = solution.twoSum_hashmap_twopass(nums.copy(), target)
        result3_sorted = sorted(result3) if result3 else []
        print(f"Hash Map (two pass):        {result3} ✅" if result3_sorted == expected_sorted else f"Hash Map (two pass):        {result3} ❌")
        
        result4 = solution.twoSum_brute_force_optimized(nums.copy(), target)
        result4_sorted = sorted(result4) if result4 else []
        print(f"Brute Force (optimized):    {result4} ✅" if result4_sorted == expected_sorted else f"Brute Force (optimized):    {result4} ❌")
        
        result5 = solution.twoSum_sorting_twopointer(nums.copy(), target)
        result5_sorted = sorted(result5) if result5 else []
        print(f"Sorting + Two Pointers:     {result5} ✅" if result5_sorted == expected_sorted else f"Sorting + Two Pointers:     {result5} ❌")

    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON:")
    print("=" * 60)
    print("1. Original (Brute Force):      O(n²) time, O(1) space")
    print("2. Hash Map (One Pass):         O(n) time, O(n) space   ⭐ BEST!")
    print("3. Hash Map (Two Pass):         O(n) time, O(n) space")
    print("4. Brute Force (Optimized):     O(n²) time, O(1) space")
    print("5. Sorting + Two Pointers:      O(n log n) time, O(n) space")