> ### Lambda Illusions

---

# Sort Students

#### Source: [codesignal.com](https://codesignal.com/) Python Arcade

---

You are given a list of `students` who want to apply to the internship at CodeSignal. For the `ith` student you know their full name `students[i]`, which can consist of up to `5` words (where a word is a set of consecutive letters). It is guaranteed that the surname is always the last name of student's full name.

Your task is to sort the students lexicographically by their surnames. If two students happen to have the same surname, their order in the result should be the same as in the original list.

##### Example

For

`````python
students = ["John Smith", "Jacky Mon Simonoff",
            "Lucy Smith", "Angela Zimonova"]
            ```
the output should be

````python
solution(students) = ["Jacky Mon Simonoff", "John Smith",
                      "Lucy Smith", "Angela Zimonova"]
`````
