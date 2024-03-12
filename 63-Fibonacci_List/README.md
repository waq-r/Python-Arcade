> ### Drilling the Lists

---

# Fibonacci List

#### Source: [codesignal.com](https://codesignal.com/) Python Arcade

---

No time to explain! The World Government made contact with intelligent alien life, and needs you to send a message to the outer space. The aliens only receive messages that are stored in a sequence of lists of sizes `0, 1, 1, 2, 3, 5, ...`, in other words those whose length increase according to the Fibonacci sequence.

The Government is too busy composing the message, and needs you to prepare the list in which the message should be sent. Given an integer `n`, return a list of `n` lists, where the first element consists is empty (consists of `0` zeros), the second element consists of `1` zero, and so on.

##### Fibonacci sequence

Fibonacci sequence is defined as follows:
`F0 = 0`, `F1 = 1`. For each `i > 1`: `Fi = Fi - 1 + Fi - 2`.
Here is the beginning of this sequence: `0, 1, 1, 2, 3, 5, 8, 13, 21,`

##### Example

For `n = 6`, the output should be

```
solution(n) = [[],
               [0],
               [0],
               [0, 0],
               [0, 0, 0],
               [0, 0, 0, 0, 0]]
```
