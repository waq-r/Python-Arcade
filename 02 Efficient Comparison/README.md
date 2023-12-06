> ### Meet Python

---

# Efficient Comparison

#### Source: [codesignal.com](https://codesignal.com/) Python Arcade

---

You would like to write a function which takes integer numbers x, y, L and R as parametres and returns True if x^y or (x \*\* y) is between L and R. Out of these three which option would be efficient in terms of execution time?

1. if L < x \*\* y < R:
2. if x ** y > L and x ** y < R:
3. if x \*\* y in range(L+1, R+1)

### Notes

My initial thought was to use option 3 since:

> - Exponentiation (\*\*) is an expensive operation.
> - Avoid repeated exponentiation by calculating x\*\*y once.
> - range(L,R) allows direct membership check which is more efficient than multiple comparisons.
> - Therefore, option 3 is the most efficient.

However, option 3 turned out to be incorrect. I ran all three options on sample inputs and found that option 1 performed the best. Maybe, because range also has overhead of generating a list, option 2 uses `and`,` whereas option 1 does direct comparisons.

````python
import time

start_time = time.time()

def is_between1(x, y, L, R):
 return L < x ** y < R

print(is_between1(99,9,0,9999999999999999999))

print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()```
````

Outputs of all three options were:

```shell
True
--- 0.0 seconds ---
True
--- 0.0009999275207519531 seconds ---
True
--- 0.0009999275207519531 seconds ---
```
