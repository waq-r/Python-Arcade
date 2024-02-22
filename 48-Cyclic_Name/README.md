> ### Itertools Kit

---

# Cyclic Name

#### Source: [codesignal.com](https://codesignal.com/) Python Arcade

---

You've come up with a really cool `name` for your future startup company, and already have an idea about its logo. This logo will represent a circle, with the prefix of a cyclic string formed by the company name written around it.

The length n of the prefix you need to take depends on the size of the logo. You haven't yet decided on it, so you'd like to try out various options. Given the `name` of your company, return the prefix of the corresponding cyclic string containing n characters.

##### Cyclic String

We call a string cyclic if it can be obtained by concatenating another string to itself many times (for example, s2 = "abcabcabcabc..." is cyclic since it can be obtained from s1 = "abc" in such a way).

##### Example

For `name = "nicecoder"` and `n = 15`, the output should be
`solution(name, n) = "nicecoderniceco"`.
