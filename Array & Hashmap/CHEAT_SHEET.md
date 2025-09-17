# 🚀 ARRAY & HASH MAP CHEAT SHEET

## 🧠 QUICK MENTAL CHECKLIST

### 📊 When to use HASH MAP?
```
❓ Do I need to COUNT something?          → Use frequency map
❓ Do I need to GROUP items?              → key = property, value = list
❓ Do I need FAST LOOKUPS?                → key = item, value = anything
❓ Do I need to store KEY-VALUE pairs?    → direct mapping
❓ Do I need MEMOIZATION?                 → cache results

If YES to any → Think HASHMAP first! 🎯
```

---

## 🔥 COMMON PATTERNS & TEMPLATES

### 1️⃣ **FREQUENCY COUNTING**
```python
# Pattern: Count occurrences
freq = {}
for item in array:
    freq[item] = freq.get(item, 0) + 1

# Or using defaultdict
from collections import defaultdict
freq = defaultdict(int)
for item in array:
    freq[item] += 1
```
**Use for:** Find duplicates, most frequent element, anagrams

### 2️⃣ **TWO SUM PATTERN**
```python
# Pattern: Find pair that sums to target
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```
**Use for:** Two sum, three sum, complement finding

### 3️⃣ **GROUPING PATTERN**
```python
# Pattern: Group items by some property
groups = defaultdict(list)
for item in items:
    key = get_property(item)  # e.g., sorted(item) for anagrams
    groups[key].append(item)
return list(groups.values())
```
**Use for:** Group anagrams, group by sum, categorization

### 4️⃣ **SLIDING WINDOW + HASHMAP**
```python
# Pattern: Track elements in current window
window_count = {}
left = 0
for right in range(len(array)):
    # Add right element
    window_count[array[right]] = window_count.get(array[right], 0) + 1
    
    # Shrink window if needed
    while condition_violated():
        window_count[array[left]] -= 1
        if window_count[array[left]] == 0:
            del window_count[array[left]]
        left += 1
```
**Use for:** Longest substring problems, subarray problems

### 5️⃣ **PREFIX SUM + HASHMAP**
```python
# Pattern: Track cumulative sums
prefix_sum = 0
sum_count = {0: 1}  # Important: initialize with 0
for num in nums:
    prefix_sum += num
    if (prefix_sum - target) in sum_count:
        # Found subarray with sum = target
        count += sum_count[prefix_sum - target]
    sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
```
**Use for:** Subarray sum equals K, continuous subarray sum

---

## ⚡ ARRAY TECHNIQUES

### 🎯 **TWO POINTERS**
```python
# Pattern: Converging pointers
left, right = 0, len(arr) - 1
while left < right:
    if condition_met():
        # Process and move both
        left += 1
        right -= 1
    elif need_larger_sum():
        left += 1
    else:
        right -= 1
```
**Use for:** Sorted arrays, palindromes, two sum on sorted array

### 🔄 **SLIDING WINDOW**
```python
# Pattern: Fixed size window
window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(k, len(arr)):
    window_sum = window_sum - arr[i-k] + arr[i]
    max_sum = max(max_sum, window_sum)
```
**Use for:** Max sum subarray of size K, moving averages

---

## 🏆 PROBLEM RECOGNITION GUIDE

| **Problem Type** | **Key Indicators** | **Solution Pattern** |
|------------------|-------------------|---------------------|
| **Anagrams** | "Same characters, different order" | Sort string OR character frequency |
| **Two Sum** | "Find pair that sums to X" | HashMap (complement lookup) |
| **Duplicates** | "Find repeated elements" | HashSet OR frequency map |
| **Grouping** | "Categorize by property" | HashMap with property as key |
| **Subarray Sum** | "Continuous elements sum to X" | Prefix sum + HashMap |
| **Frequency** | "Count occurrences" | Frequency map |
| **Fast Lookup** | "Check if exists quickly" | HashSet |

---

## 🎮 COMPLEXITY CHEAT SHEET

### **Hash Map Operations:**
- **Insert/Delete/Search:** O(1) average, O(n) worst case
- **Space:** O(n) for n elements

### **Array Operations:**
- **Access by index:** O(1)
- **Search:** O(n) unsorted, O(log n) sorted
- **Insert/Delete:** O(n) for arbitrary position

---

## 🧩 COMMON GOTCHAS & TIPS

### ✅ **DO:**
- Initialize HashMap with default values when needed
- Consider using `defaultdict` for cleaner code
- Use `enumerate()` when you need both index and value
- Remember that HashSets are just HashMaps with dummy values

### ❌ **AVOID:**
- Forgetting to handle empty arrays/strings
- Not considering duplicate keys in HashMap
- Using lists when HashSets would be more efficient
- Nested loops when HashMap can give O(1) lookup

---

## 🎯 QUICK DECISION TREE

```
Need to solve array problem?
├─ Need fast lookups? → HashMap/HashSet
├─ Need to count? → Frequency Map
├─ Array is sorted? → Two Pointers
├─ Need subarray/substring? → Sliding Window
├─ Need cumulative sum? → Prefix Sum + HashMap
└─ Need grouping? → HashMap with custom keys
```

---

## 🔥 LEETCODE PATTERNS

| **Pattern** | **Problems** |
|-------------|-------------|
| **Frequency Map** | Valid Anagram, Group Anagrams, Top K Frequent |
| **Two Sum** | Two Sum, 3Sum, 4Sum |
| **Sliding Window** | Longest Substring, Max Sum Subarray |
| **Prefix Sum** | Subarray Sum Equals K, Continuous Subarray Sum |
| **Grouping** | Group Anagrams, Group Shifted Strings |

---

*💡 Remember: When in doubt, ask yourself "Can a HashMap make this O(1)?" - if yes, use it!*