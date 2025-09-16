class Solution(object):
    # ========================================
    # ORIGINAL SOLUTION BY USER
    # ========================================
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        
        Original approach: Sorting method
        Time: O(n log n), Space: O(n)
        Simple and intuitive solution!
        """
        if sorted(s) == sorted(t):
            return True
        return False

    # ========================================
    # ALTERNATIVE SOLUTIONS
    # ========================================
    
    def isAnagram_hashmap(self, s, t):
        """
        Alternative 1: Character Frequency Counter (Hash Map)
        Time: O(n), Space: O(k) where k is unique characters
        More efficient for larger inputs
        """
        if len(s) != len(t):
            return False
        
        char_count = {}
        
        # Count characters in s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Subtract characters in t
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
        
        return len(char_count) == 0

    def isAnagram_counter(self, s, t):
        """
        Alternative 2: Using Counter from collections
        Time: O(n), Space: O(k)
        Pythonic and very clean approach
        """
        from collections import Counter
        return Counter(s) == Counter(t)

    def isAnagram_array(self, s, t):
        """
        Alternative 3: Character Array (for lowercase letters only)
        Time: O(n), Space: O(1) - Most efficient!
        Best for problems with only lowercase English letters
        """
        if len(s) != len(t):
            return False
        
        char_count = [0] * 26  # For lowercase a-z
        
        for i in range(len(s)):
            char_count[ord(s[i]) - ord('a')] += 1
            char_count[ord(t[i]) - ord('a')] -= 1
        
        return all(count == 0 for count in char_count)

    def isAnagram_sorted_optimized(self, s, t):
        """
        Alternative 4: Optimized version of your approach
        Time: O(n log n), Space: O(n)
        One-liner version of your solution
        """
        return sorted(s) == sorted(t)


# ========================================
# TESTING THE SOLUTIONS
# ========================================
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("listen", "silent", True),
        ("hello", "bello", False),
        ("", "", True)
    ]
    
    print("Testing all solutions:")
    print("=" * 50)
    
    for s, t, expected in test_cases:
        print(f"\nTest: '{s}' and '{t}' -> Expected: {expected}")
        
        # Test original solution
        result1 = solution.isAnagram(s, t)
        print(f"Original (sorting):     {result1} ✅" if result1 == expected else f"Original (sorting):     {result1} ❌")
        
        # Test alternative solutions
        result2 = solution.isAnagram_hashmap(s, t)
        print(f"Hash Map:               {result2} ✅" if result2 == expected else f"Hash Map:               {result2} ❌")
        
        result3 = solution.isAnagram_counter(s, t)
        print(f"Counter:                {result3} ✅" if result3 == expected else f"Counter:                {result3} ❌")
        
        # Only test array method for lowercase letters
        if s.islower() and t.islower() and s.isalpha() and t.isalpha():
            result4 = solution.isAnagram_array(s, t)
            print(f"Array (lowercase only): {result4} ✅" if result4 == expected else f"Array (lowercase only): {result4} ❌")
        
        result5 = solution.isAnagram_sorted_optimized(s, t)
        print(f"Sorted (optimized):     {result5} ✅" if result5 == expected else f"Sorted (optimized):     {result5} ❌")