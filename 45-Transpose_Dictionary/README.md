> ### Caravan of Collections

---

# Transpose Dictionary

#### Source: [codesignal.com](https://codesignal.com/) Python Arcade

---

You're implementing a plugin for your favorite code editor. This plugin launches various scripts depending on the open file extension. Each script is associated with exactly one extension, and the information about which script should be launched for each extension is stored in a dictionary `scriptByExtension`.

You are planning to add more supported extensions for some scripts, so now you would also like to store information about the extensions which each script supports. As a starting point, you'd like to obtain the `(extension, script)` pairs from the dictionary, sorted lexicographically by the extensions.

Implement a function that will do the job.

##### Example

For

```py
scriptByExtension = {
  "validate": "py",
  "getLimits": "md",
  "generateOutputs": "json"
}
```

the output should be

```python
solution(scriptByExtension) = [["json", "generateOutputs"],
                               ["md", "getLimits"],
                               ["py", "validate"]]
```
