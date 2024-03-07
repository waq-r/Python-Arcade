> ### Drilling the Lists

---

# Fix Tree

#### Source: [codesignal.com](https://codesignal.com/) Python Arcade

---

Not long ago a young Christmas elf asked you to implement a function that creates Christmas trees made of asterisks ('\*') similar to the one below:

```
    *
    *
   ***
  *****
 *******
*********
   ***
```

Unfortunately because of the extreme coldness the tree that you sent over was corrupted: although its lines are given in the correct order, but are not aligned properly. Now your task is to fix the given tree by centering the asterisks in each line.

##### Example

For

```py
tree = [
  "      *  ",
  "    *    ",
  "***      ",
  "    *****",
  "  *******",
  "*********",
  " ***     "
]
```

the output should be

```py
solution(tree) = [
  "    *    ",
  "    *    ",
  "   ***   ",
  "  *****  ",
  " ******* ",
  "*********",
  "   ***   "
]
```
