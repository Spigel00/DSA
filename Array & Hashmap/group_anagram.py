class Solution(object):
    # ========================================
    # ORIGINAL SOLUTION BY USER
    # ========================================
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        
        Original approach: Sorting with Hash Map
        Time: O(n * m log m), Space: O(n * m)
        where n = number of strings, m = average length of strings
        Excellent approach using sorted tuples as keys!
        """
        map={}
        for word in strs:
            key=tuple(sorted(word))
           
            if key in map:
                map[key].append(word)
            else :
                map[key]=[word]
        return map.values()

    # ========================================
    # ALTERNATIVE SOLUTIONS
    # ========================================
    
    def groupAnagrams_defaultdict(self, strs):
        """
        Alternative 1: Using defaultdict (Cleaner Code)
        Time: O(n * m log m), Space: O(n * m)
        Same logic as original but with cleaner syntax using defaultdict
        """
        from collections import defaultdict
        
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Sort characters and use as key
            key = tuple(sorted(word))
            anagram_map[key].append(word)
        
        return list(anagram_map.values())

    def groupAnagrams_character_count(self, strs):
        """
        Alternative 2: Character Count as Key (No Sorting!)
        Time: O(n * m), Space: O(n * m)
        More efficient - avoids sorting by using character frequency
        """
        from collections import defaultdict
        
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Count frequency of each character
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            
            # Use character count tuple as key
            key = tuple(char_count)
            anagram_map[key].append(word)
        
        return list(anagram_map.values())

    def groupAnagrams_counter_key(self, strs):
        """
        Alternative 3: Using Counter for Key Generation
        Time: O(n * m), Space: O(n * m)
        Pythonic approach using Counter from collections
        """
        from collections import defaultdict, Counter
        
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Use sorted counter items as key
            key = tuple(sorted(Counter(word).items()))
            anagram_map[key].append(word)
        
        return list(anagram_map.values())

    def groupAnagrams_prime_product(self, strs):
        """
        Alternative 4: Prime Number Product (Mathematical Approach)
        Time: O(n * m), Space: O(n * m)
        Creative approach using prime numbers - each character maps to a prime
        """
        from collections import defaultdict
        
        # Map each character to a prime number
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
                 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Calculate product of primes for each character
            product = 1
            for char in word:
                product *= primes[ord(char) - ord('a')]
            
            anagram_map[product].append(word)
        
        return list(anagram_map.values())

    def groupAnagrams_string_signature(self, strs):
        """
        Alternative 5: Custom String Signature
        Time: O(n * m), Space: O(n * m)
        Create a unique signature for each anagram group
        """
        from collections import defaultdict
        
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Create signature: "a2b1c1" for "abc"
            char_count = {}
            for char in word:
                char_count[char] = char_count.get(char, 0) + 1
            
            # Sort by character and create signature
            signature = ''.join(f"{char}{count}" for char, count in sorted(char_count.items()))
            anagram_map[signature].append(word)
        
        return list(anagram_map.values())


# ========================================
# TESTING THE SOLUTIONS
# ========================================
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        (["eat","tea","tan","ate","nat","bat"], 
         [["bat"],["nat","tan"],["ate","eat","tea"]]),
        
        ([""], [[""]]),
        
        (["a"], [["a"]]),
        
        (["abc", "bca", "cab", "xyz", "zyx", "yxz", "def"],
         [["abc","bca","cab"], ["xyz","zyx","yxz"], ["def"]]),
        
        (["listen", "silent", "hello", "world", "enlist"],
         [["listen","silent","enlist"], ["hello"], ["world"]])
    ]
    
    def normalize_result(result):
        """Helper function to normalize results for comparison"""
        # Sort each group and then sort the groups for consistent comparison
        normalized = []
        for group in result:
            normalized.append(sorted(group))
        return sorted(normalized)
    
    print("Testing all Group Anagrams solutions:")
    print("=" * 70)
    
    for i, (strs, expected) in enumerate(test_cases, 1):
        print(f"\nTest {i}: {strs}")
        expected_normalized = normalize_result(expected)
        
        # Test original solution
        try:
            result1 = list(solution.groupAnagrams(strs.copy()))
            result1_normalized = normalize_result(result1)
            print(f"Original (sorting):         ✅" if result1_normalized == expected_normalized else f"Original (sorting):         ❌")
        except Exception as e:
            print(f"Original (sorting):         Error: {e} ❌")
        
        # Test alternative solutions
        result2 = solution.groupAnagrams_defaultdict(strs.copy())
        result2_normalized = normalize_result(result2)
        print(f"DefaultDict:                ✅" if result2_normalized == expected_normalized else f"DefaultDict:                ❌")
        
        result3 = solution.groupAnagrams_character_count(strs.copy())
        result3_normalized = normalize_result(result3)
        print(f"Character Count:            ✅" if result3_normalized == expected_normalized else f"Character Count:            ❌")
        
        result4 = solution.groupAnagrams_counter_key(strs.copy())
        result4_normalized = normalize_result(result4)
        print(f"Counter Key:                ✅" if result4_normalized == expected_normalized else f"Counter Key:                ❌")
        
        result5 = solution.groupAnagrams_prime_product(strs.copy())
        result5_normalized = normalize_result(result5)
        print(f"Prime Product:              ✅" if result5_normalized == expected_normalized else f"Prime Product:              ❌")
        
        result6 = solution.groupAnagrams_string_signature(strs.copy())
        result6_normalized = normalize_result(result6)
        print(f"String Signature:           ✅" if result6_normalized == expected_normalized else f"String Signature:           ❌")

    print("\n" + "=" * 70)
    print("PERFORMANCE COMPARISON:")
    print("=" * 70)
    print("1. Original (Sorting):          O(n*m log m) time, O(n*m) space")
    print("2. DefaultDict (Sorting):       O(n*m log m) time, O(n*m) space")
    print("3. Character Count:             O(n*m) time, O(n*m) space      ⭐ FASTEST!")
    print("4. Counter Key:                 O(n*m) time, O(n*m) space")
    print("5. Prime Product:               O(n*m) time, O(n*m) space      🧮 CREATIVE!")
    print("6. String Signature:            O(n*m) time, O(n*m) space")
    print("\nWhere n = number of strings, m = average string length")