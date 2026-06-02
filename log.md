
***Date: 26-01-26***
***Topic:*** **Arrays**
***Problem:*** **Contains duplicate**
***Questions raised:***
1. **Why use set instead of tuple/list?**
	- 1. - The problem asks **“have I seen this value before?”**, not how many times it appears.
        
    - A **set** allows **instant membership checking** (`is this value already present?`) in constant time.
        
    - A **list or tuple** must check elements one by one, which becomes slower as the array grows.
        
    - Using a set lets us **stop immediately** when a duplicate is found instead of scanning the entire array.
        
    - The “no duplicate storage” property of a set is secondary; the **real reason is fast lookup**.

2. **Existence vs Counting problems**

	- Learned to distinguish between problems that ask **“does something exist?”** and those that ask **“how many times?”**
	    
	- For existence problems, counting occurrences is unnecessary; detection and early exit is enough.



Here you go — clean, crisp, **DSA-learning-log style**, same tone and structure as your example.
I’ll keep it precise and reflective, not fluffy.

---

***Date: 27-01-26***
***Topic:*** **Strings / Hashing Basics**
***Problem:*** **Valid Anagram**

***What I learned:***

* How to decide **when two pointers make sense and when they don’t**
* Why **order-independent problems** require frequency-based thinking
* Why **maps / dictionaries exist** and when they are the right tool

---

***Questions raised & insights:***

1. **Why two pointers do NOT work directly for anagram problems?**

   * Two pointers rely on **order or symmetry** (e.g., sorted arrays, palindromes).
   * Anagrams allow characters to appear in **any order**, so index-based comparison is unreliable.
   * Without sorting, pointers may compare unrelated characters.
   * Conclusion:
     👉 Two pointers are useful only **after normalization** (like sorting), not on raw strings.

---

2. **What invariant defines an anagram?**

   * Order does not matter.
   * What must remain the same is the **frequency of each character**.
   * Two strings are anagrams **iff every character appears the same number of times in both strings**.
   * This shifts the problem from *comparison* → *counting*.

---

3. **Why use a map / dictionary instead of separate variables?**

   * Characters are **unknown and dynamic**; we cannot predefine variables like `count_a`, `count_b`, etc.
   * A dictionary allows:

     * Dynamic key creation (new characters handled automatically)
     * Mapping **character → frequency**
     * Constant-time updates and lookups
   * The dictionary grows only as needed, adapting to the input string.

---

***Key takeaway:***

> **When order does not matter, stop thinking in terms of positions and start thinking in terms of counts.**


Here you go — **same format, same tone, clean DSA learning log**, focused on **Two Sum + HashMap + enumerate**.

---

***Date: 03-02-26***
***Topic:*** **Arrays / Hashing**
***Problem:*** **Two Sum**

***Questions raised:***

1. **Why is brute force (two nested loops) not the best approach?**

   * The brute-force approach checks **all possible pairs**, leading to **O(n²)** time complexity.

   * Even though it works for small inputs, it **does not scale well** as the array grows.

   * The problem guarantees **exactly one valid pair**, so checking all pairs is unnecessary.

   * This pushed me to think:
     **“Can I remember past values instead of rechecking them?”**

---

2. **What is the real pattern behind Hash map and ?**

   * Trigger words identified:

     * *pair*
     * *sum equals target*
     * *indices*
     * *exists exactly once*

   * These signals indicate a **complement lookup problem**.

   * For each value `x`, the real question is:
     **“Have I already seen `target - x`?”**

   * This maps directly to using a **HashMap / Dictionary**.

---

3. **What exactly is stored in the dictionary?**

   * The dictionary stores:

     **number → index**

   * It does **not** store sums or pairs.

   * The purpose of the dictionary is **memory**, not computation.

   * Storing indices is essential because the problem asks for **indices**, not values.

---

4. **Why use `enumerate` instead of a normal loop?**

   * `enumerate` provides **both index and value at the same time**.

   * This is necessary because:

     * The **value** is used to compute the complement
     * The **index** is required for the output

   * Using `enumerate` avoids:

     * Extra indexing logic
     * Confusion between values and positions

   * Mental rule formed:

     👉 **If the solution or output depends on indices, use `enumerate`.**

---

***Key takeaways:***

* Two Sum is **not** a two-pointer problem on an unsorted array.
* It is a **HashMap + complement lookup** problem.
* The dictionary is used to **remember past elements**, not to store results.
* `enumerate` is a **DSA tool**, not just a Python convenience.
* Core invariant remembered:

> **As I traverse the array, I ask:
> “Have I already seen the number that completes my sum?”**

---

***Date: 02-06-26***
***Topic:*** **Arrays / Nested Loops**
***Problem:*** **3633. Earliest Finish Time for Land and Water Rides**

***Questions raised:***

1. **Why use nested loops?**

   * Needed to check every land ride with every water ride.
   * Mental trigger:

     👉 **"Every A with Every B" → Nested Loops**

---

2. **Indices vs Values**

   * Initially used:

     ```python
     for i in landStartTime:
     ```

   * Learned that `i` became values, not ride numbers.

   * Correct approach was using indices to access related data:

     ```python
     landStartTime[i]
     landDuration[i]
     ```

---

3. **Why use a global answer variable?**

   * Each iteration produces one possible finish time.
   * Needed to track the best answer across all combinations.

     ```python
     answer = min(answer, current_finish_time)
     ```

---

***Why I got stuck:***

* Confused indices with values.
* Struggled translating "try every combination" into nested loops.
* Didn't initially realize a global minimum variable was required.

---

***Key takeaway:***

> **The challenge was Python loop/index fluency and variable tracking, not the algorithm itself.**
