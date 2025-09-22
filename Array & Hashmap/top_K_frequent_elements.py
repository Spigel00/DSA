class Solution(object):
    # ========================================
    # ORIGINAL SOLUTION BY USER
    # ========================================
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        
        Original approach: Frequency Count + Sorting
        Time: O(n log n), Space: O(n)
        Clean and straightforward approach using sorting!
        """
        count ={} 
        for val in nums:
            if val in count:
                count[val]+=1
            else: 
                count[val]=1
        return sorted(count, key=lambda x: count[x], reverse=True)[:k]

    # ========================================
    # ALTERNATIVE SOLUTIONS
    # ========================================
    
    def topKFrequent_heap(self, nums, k):
        """
        Alternative 1: Min Heap (Most Optimal!)
        Time: O(n log k), Space: O(n + k)
        Best approach for large datasets - only keeps k elements in heap
        """
        import heapq
        from collections import Counter
        
        # Count frequencies
        count = Counter(nums)
        
        # Use min heap to keep track of k most frequent elements
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Extract elements from heap
        return [num for freq, num in heap]

    def topKFrequent_counter_most_common(self, nums, k):
        """
        Alternative 2: Counter.most_common() (Pythonic!)
        Time: O(n log n), Space: O(n)
        Most concise solution using built-in Counter method
        """
        from collections import Counter
        
        count = Counter(nums)
        return [num for num, freq in count.most_common(k)]

    def topKFrequent_bucket_sort(self, nums, k):
        """
        Alternative 3: Bucket Sort (Linear Time!)
        Time: O(n), Space: O(n)
        Most efficient for specific constraints - frequency-based bucketing
        """
        from collections import defaultdict
        
        # Count frequencies
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        # Bucket sort by frequency
        # bucket[i] contains all numbers with frequency i
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)
        
        # Collect top k elements from highest frequency buckets
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result

    def topKFrequent_quickselect(self, nums, k):
        """
        Alternative 4: QuickSelect Algorithm
        Time: O(n) average, O(n²) worst, Space: O(n)
        Advanced approach using partition-based selection
        """
        from collections import Counter
        import random
        
        count = Counter(nums)
        unique_nums = list(count.keys())
        
        def quickselect(left, right, k_smallest):
            """Find the k_smallest element in the range [left, right]"""
            if left == right:
                return
            
            # Random pivot for better average performance
            pivot_idx = random.randint(left, right)
            pivot_freq = count[unique_nums[pivot_idx]]
            
            # Partition around pivot
            unique_nums[pivot_idx], unique_nums[right] = unique_nums[right], unique_nums[pivot_idx]
            store_idx = left
            
            for i in range(left, right):
                if count[unique_nums[i]] < pivot_freq:
                    unique_nums[store_idx], unique_nums[i] = unique_nums[i], unique_nums[store_idx]
                    store_idx += 1
            
            unique_nums[store_idx], unique_nums[right] = unique_nums[right], unique_nums[store_idx]
            
            # Recursively select
            if k_smallest == store_idx:
                return
            elif k_smallest < store_idx:
                quickselect(left, store_idx - 1, k_smallest)
            else:
                quickselect(store_idx + 1, right, k_smallest)
        
        # Find the k largest elements (n-k smallest in frequency)
        n = len(unique_nums)
        quickselect(0, n - 1, n - k)
        return unique_nums[n - k:]

    def topKFrequent_max_heap(self, nums, k):
        """
        Alternative 5: Max Heap (Intuitive Approach)
        Time: O(n log n), Space: O(n)
        Uses max heap to always get the most frequent element first
        """
        import heapq
        from collections import Counter
        
        count = Counter(nums)
        
        # Create max heap (negate frequencies for max heap behavior)
        max_heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(max_heap)
        
        # Extract top k elements
        result = []
        for _ in range(k):
            neg_freq, num = heapq.heappop(max_heap)
            result.append(num)
        
        return result


# ========================================
# TESTING THE SOLUTIONS
# ========================================
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([1,1,1,2,2,3], 2, [1,2]),  # Most common case
        ([1], 1, [1]),  # Single element
        ([1,2], 2, [1,2]),  # All elements have same frequency
        ([1,1,1,2,2,3,3,3,4,4,4,4], 3, [4,1,3]),  # Multiple frequencies
        ([5,5,5,5,2,2,1], 2, [5,2]),  # Clear frequency differences
        ([3,0,1,0], 1, [0])  # With zeros
    ]
    
    def normalize_result(result, expected):
        """Helper function to check if results match (order may vary for equal frequencies)"""
        return len(result) == len(expected) and set(result) == set(expected)
    
    print("Testing all Top K Frequent Elements solutions:")
    print("=" * 80)
    
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        print(f"\nTest {i}: nums={nums}, k={k}")
        print(f"Expected: {expected}")
        
        # Test original solution
        try:
            result1 = solution.topKFrequent(nums.copy(), k)
            print(f"Original (sorting):         {result1} ✅" if normalize_result(result1, expected) else f"Original (sorting):         {result1} ❌")
        except Exception as e:
            print(f"Original (sorting):         Error: {e} ❌")
        
        # Test alternative solutions
        try:
            result2 = solution.topKFrequent_heap(nums.copy(), k)
            print(f"Min Heap:                   {result2} ✅" if normalize_result(result2, expected) else f"Min Heap:                   {result2} ❌")
        except Exception as e:
            print(f"Min Heap:                   Error: {e} ❌")
        
        try:
            result3 = solution.topKFrequent_counter_most_common(nums.copy(), k)
            print(f"Counter most_common:        {result3} ✅" if normalize_result(result3, expected) else f"Counter most_common:        {result3} ❌")
        except Exception as e:
            print(f"Counter most_common:        Error: {e} ❌")
        
        try:
            result4 = solution.topKFrequent_bucket_sort(nums.copy(), k)
            print(f"Bucket Sort:                {result4} ✅" if normalize_result(result4, expected) else f"Bucket Sort:                {result4} ❌")
        except Exception as e:
            print(f"Bucket Sort:                Error: {e} ❌")
        
        try:
            result5 = solution.topKFrequent_quickselect(nums.copy(), k)
            print(f"QuickSelect:                {result5} ✅" if normalize_result(result5, expected) else f"QuickSelect:                {result5} ❌")
        except Exception as e:
            print(f"QuickSelect:                Error: {e} ❌")
        
        try:
            result6 = solution.topKFrequent_max_heap(nums.copy(), k)
            print(f"Max Heap:                   {result6} ✅" if normalize_result(result6, expected) else f"Max Heap:                   {result6} ❌")
        except Exception as e:
            print(f"Max Heap:                   Error: {e} ❌")

    print("\n" + "=" * 80)
    print("PERFORMANCE COMPARISON:")
    print("=" * 80)
    print("1. Original (Sorting):          O(n log n) time, O(n) space")
    print("2. Min Heap:                    O(n log k) time, O(n+k) space    ⭐ BEST FOR LARGE DATA!")
    print("3. Counter most_common:         O(n log n) time, O(n) space      🐍 MOST PYTHONIC!")
    print("4. Bucket Sort:                 O(n) time, O(n) space            🚀 FASTEST!")
    print("5. QuickSelect:                 O(n) avg time, O(n) space        🧠 ADVANCED!")
    print("6. Max Heap:                    O(n log n) time, O(n) space")
    print("\nChoose based on:")
    print("• Large datasets + small k → Min Heap")
    print("• Need linear time → Bucket Sort")
    print("• Pythonic code → Counter.most_common()")
    print("• Learning algorithms → QuickSelect")
