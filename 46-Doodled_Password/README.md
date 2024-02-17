> ### Caravan of Collections

---

# Doodled Password

#### Source: [codesignal.com](https://codesignal.com/) Python Arcade

---

Your friend has been doodling during the lecture and wrote down several digits in a circle. You're wondering if these digits might form the password to your friend's computer. You're planning to prank him some time in the future, and hacking into his computer will definitely help. If the digits written in the clockwise order indeed form a password, all you need to do is figure out which digit comes in it first.

Given a list of digits as they are written in the clockwise order, find all other combinations the password could possibly have.

##### Example

For `digits = [1, 2, 3, 4, 5]`, the output should be

```py
solution(digits) = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2],
                    [4, 5, 1, 2, 3], [5, 1, 2, 3, 4]]
```
