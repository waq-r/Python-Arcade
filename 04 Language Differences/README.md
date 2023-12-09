> ### Meet Python

---

# Language Differences

#### Source: [codesignal.com](https://codesignal.com/) Python Arcade

---

The differnce between integer division in Python vs Java/C++. Python round towards negative infinity using // operator while Java and C++ round towards zero.

### Notes

Both Java and C++ perform integer division, rounding towards zero.

In Python, it uses true division by default, which means it returns a floating-point result even if the operands are integers. To perform integer division in Python like in C++ and Java, use the floor division operator //.
If we want Python to perform integer division, we can use the double-slash operator.
Python uses the floor division // operator to round towards negative infinity.

```c++
int result = 15 / -4;  // Result: -3
```

```java
int result = 15 / -4;  // Result: -3
```

```python
result = 15 // -4  # Result: -4
result = 15 / -4  # Result: -3.75
```
