> ### Slithering in Strings

---

# String Definition

#### Source: [codesignal.com](https://codesignal.com/) Python Arcade

---

### Which of the following are incorrect string definitions in Python:

s0 = "hello world"

s1 = 'hello world'

s2 = """hello world"""

s3 = ""hello world""

s4 = ''hello world''

The first three are corect string definitions in Python. Single ('') and double ("") quotes can be used to define strings in Python. Triple quotes (""") can also be used to define multi-line strings. The last two definitions s3 and s4 use incorrect quoting by using single/double quotes inside another set of single/double quotes, which results in a syntax error.

```python
s0 = "hello world 0"
print(s0)
s1 = 'hello world 1'
print(s1)
s2 = """hello world 2"""
print(s2)
s3 = ""hello world 3""
print(s3)
s4 = ''hello world 4''
print(s4)
```

#### Outputs

The first three print statements will output the strings as defined. The last two will result in a syntax error as shown in the error message below.

```shell
hello world 0
hello world 1
hello world 2
```

Error : s3 and s4 are invalid string definitions in Python due to mixing single and double quotes

```shell
  Cell In[4], line 7
    s3 = ""hello world 3""
           ^
SyntaxError: invalid syntax
```
