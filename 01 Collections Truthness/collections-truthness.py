# Collections Truthness
xe = [()]
print(xe == True)
res = [False] * 2
print(res)
if xe:
    res[0] = True
if xe[0]:
    res[1] = True

print(res)

# outputs
# False
# [False, False]
# [True, False]