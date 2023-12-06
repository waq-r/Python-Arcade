> ### Meet Python

---

# Collections Truthness

#### Source: [codesignal.com](https://codesignal.com/) Python Arcade

---

What would be the value of `res` after the folllowing snippet is exexuted:

```python
xe = [()]
res = [False] * 2
if xe:
    res[0] = True
if xe[0]:
    res[1] = True
```

### Notes

> - Python considers empty lists, tuples, dicts and strings as `False` values in conditionals.
> - Non-empty collections are considered `True`.
> - So the outer if evaluates `xe` as True since it is a non-empty list containing an empty tuple.
> - The inner if tries to evaluate the first element `xe[0]`, but it is an empty tuple which evaluates to `False`.
