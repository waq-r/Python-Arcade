> ### Lurking in Lists

---

# Lists Concatenation

#### Source: [codesignal.com](https://codesignal.com/) Python Arcade

---

Given two lists `lst1` and `lst2`, your task is to return a list formed by the elements of `lst1` followed by the elements of `lst2`.

Note: this is a bugfix task, which means that the function is already implemented but there is a bug in one of its lines. Your task is to find and fix it.

##### Example

For `lst1 = [2, 2, 1]` and `lst2 = [10, 11]`, the output should be
`solution(lst1, lst2) = [2, 2, 1, 10, 11]`.

##### Notes

- Python lists have a built-in `+` operator that concatenates two lists.
- We are given that a function to concatenate two lists already exists but contains a bug.
- Based on the example given, the expected output is a single list containing the elements of the first list followed by the elements of the second list.
- The Python extend() list function is used to add elements of an iterable (such as string, list, tuple, set, etc.) to the end of another list.
