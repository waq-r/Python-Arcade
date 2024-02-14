> ### Caravan of Collections

---

# Startup Name

#### Source: [codesignal.com](https://codesignal.com/) Python Arcade

---

You decided to found your own startup company and now want to choose a proper name for it. There are three large `companies` that you want to compete against, and since their names are quite popular you want to use their names as a starting point. You want to use only popular characters in the name of your company, but not too mainstream. You consider a character to be popular if it appears in at least two company names, and consider it to be mainstream if it appears in all three.

Given the names of the `companies`, return the list of characters that are popular but not mainstream sorted by their ASCII codes.

##### Example

For `companies = ["coolcompany", "nicecompany", "legendarycompany"]`,
the output should be
`solution(companies) = ['e', 'l']`.

Here's how the answer can be obtained:

these letters appear in all three company names and are thus mainstream: 'a', 'c', 'm', 'n', 'o', 'p', 'y';
these letters appear only in one of the company names and are thus not popular: 'd', 'g', 'i', 'r';
the remaining letters are popular and not mainstream: 'e', 'l'.
