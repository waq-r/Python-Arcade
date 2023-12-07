# Special Conditional
a = True
b = True

print(not a == b)
print(a ==(not b))
print(not (a == b))
print(a == not b)

# outputs
#  line 7
#     print(a == not b)
#                ^
# SyntaxError: invalid syntax