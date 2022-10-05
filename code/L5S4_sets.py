# print sorted the distinct letters of a phrase
a_set = set()
for c in "Torture the data, and it will confess to anything.":
    if c.isalpha():
        a_set.add(c.upper())
print("".join(sorted(list(a_set))))
