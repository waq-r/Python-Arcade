> ### Fumbling in Functional

---

# Create Histogram

#### Source: [codesignal.com](https://codesignal.com/) Python Arcade

---

You noticed that one of your employees has a weird performance rate: although his performance is usually good and stable, from time to time it drops drastically. You suspect it has something to do with the famous Code of Clones series: new episodes started to come out recently, and everyone watches and rewatches them every so often.

To confirm your theory, you'd like to create a histogram showing the number of assignments he completed each day in the given period. Given this `assignments`, return a list representing a horizontal histogram, where each bar is formed by the given character `ch`.

##### gitExample

For `ch = '*' and assignments = [12, 12, 14, 3, 12, 15, 14]`,
the output should be

```python
solution(ch, assignments) = ["************",
                             "************",
                             "**************",
                             "***",
                             "************",
                             "***************",
                             "**************"]
```
