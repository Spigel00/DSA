

# 🚀 ARRAY & HASH MAP CHEAT SHEET

## 🧠 QUICK MENTAL CHECKLIST

### 📊 When to use HASH MAP?

```
❓ Do I need to COUNT something?          → Use frequency map (key = item, value = count)
❓ Do I need to GROUP items?              → key = property, value = list of items
❓ Do I need FAST LOOKUPS?                → key = item, value = anything
❓ Do I need KEY-VALUE associations?      → direct mapping
❓ Do I need MEMOIZATION / caching?      → store precomputed results

If YES to any → Think HASHMAP first! 🎯
```

---

### 📊 When to use ARRAY / LIST?

```
❓ Need ordered data or sequential access?   → Use array/list
❓ Need index-based lookup?                  → array[index] is O(1)
❓ Need prefix/suffix computations?          → use array for cumulative sums/products
❓ Need sliding window or two pointers?      → array is ideal
❓ Need sorting or rearrangement?            → array/list works best
❓ Dynamic programming grid?                  → use 1D/2D array
❓ Subarray/subsequence problems?            → array for sequence manipulation
```

---

## 🔥 COMMON HASHMAP PATTERNS

| **Pattern**                 | **What it means / key idea**                       | **Example Use Cases**                                             |
| --------------------------- | -------------------------------------------------- | ----------------------------------------------------------------- |
| **Frequency Counting**      | key = item, value = count                          | Find duplicates, most frequent element, anagrams                  |
| **Grouping**                | key = property, value = list of items              | Group anagrams, categorize items                                  |
| **Two Sum / Complement**    | key = item, value = index or existence             | Find pair/tuple that sums to target                               |
| **Sliding Window Tracking** | key = element, value = count in current window     | Longest substring without repeating characters, subarray problems |
| **Prefix Sum Tracking**     | key = cumulative sum, value = count of occurrences | Subarray sum equals target, continuous subarray sum               |
| **Memoization / Caching**   | key = state, value = precomputed result            | Fibonacci, DP problems                                            |
| **Fast Existence Check**    | key = element, value = dummy / True                | Detect duplicates quickly                                         |

---

## ⚡ COMMON ARRAY PATTERNS

| **Pattern / Technique**        | **Key Idea / Concept**                                 | **Example Use Cases**                                            |
| ------------------------------ | ------------------------------------------------------ | ---------------------------------------------------------------- |
| **Two Pointers**               | Use left & right indices to traverse array efficiently | Sorted array problems, palindrome check, two sum on sorted array |
| **Sliding Window**             | Fixed or variable-size window to process subarrays     | Max sum subarray, longest substring problems                     |
| **Prefix / Cumulative Sum**    | Precompute sums or products to answer subarray queries | Subarray sum, range sum queries                                  |
| **Dynamic Programming Arrays** | 1D or 2D array storing state or subproblem solutions   | Longest increasing subsequence, edit distance                    |
| **Index-based Access**         | Direct access via array\[index]                        | Lookup by position, array manipulation                           |
| **Reordering / Sorting**       | Change order or sort for easier processing             | Merge intervals, sort colors                                     |

---

## 🏆 PROBLEM RECOGNITION GUIDE

| **Problem Type**        | **Key Indicators**                       | **Pattern / Tool**                     |
| ----------------------- | ---------------------------------------- | -------------------------------------- |
| **Anagrams**            | “Same letters, different order”          | Grouping with HashMap                  |
| **Two Sum / Pair**      | “Find pair that sums to X”               | HashMap complement lookup              |
| **Duplicates**          | “Find repeated elements”                 | HashMap / HashSet                      |
| **Grouping**            | “Categorize items by property”           | HashMap (key = property, value = list) |
| **Subarray Sum**        | “Continuous elements sum to target”      | Prefix sum + HashMap                   |
| **Frequency**           | “Count occurrences”                      | HashMap (key = item, value = count)    |
| **Fast Lookup**         | “Check existence quickly”                | HashSet / HashMap                      |
| **Sequence / Order**    | “Preserve order, iterate by index”       | Array / List                           |
| **Sliding Window**      | “Longest/shortest substring or subarray” | Array + HashMap                        |
| **Dynamic Programming** | “Optimal subproblem solution required”   | Array for storing DP states            |

---

## 🎮 COMPLEXITY CHEAT SHEET

| **Operation**   | **Hash Map / Dictionary** | **Array / List**            |
| --------------- | ------------------------- | --------------------------- |
| Insert / Update | O(1) average, O(n) worst  | O(n) for arbitrary position |
| Lookup / Search | O(1) average, O(n) worst  | O(1) by index, O(n) search  |
| Delete          | O(1) average              | O(n) for arbitrary position |
| Memory / Space  | O(n)                      | O(n)                        |

---

## 🧩 COMMON TIPS & GOTCHAS

**HashMap:**

* ✅ Initialize empty lists or default counts when needed
* ✅ Use `defaultdict` for cleaner code
* ✅ Keys must be immutable (tuple, string, int)
* ❌ Don’t try to `.append()` to a non-list value
* ❌ Avoid returning inside the loop when building a map

**Array:**

* ✅ Use indices and slices effectively
* ✅ Precompute prefix sums when needed
* ❌ Forgetting bounds when using two pointers or sliding window

---

## 🎯 QUICK DECISION TREE

```
Need to solve problem?
├─ Need fast lookup or mapping → HashMap
├─ Need counting / grouping → HashMap
├─ Need sequential / ordered access → Array
├─ Need subarray / substring → Array + Sliding Window
├─ Need cumulative sums → Array + Prefix Sum
├─ Need DP storage → Array
```


