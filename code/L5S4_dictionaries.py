# count occurrences of each letter in a phrase
a_dict = {}
a_phrase = "The goal is to turn data into information, and information into insight."
for c in a_phrase:
    if c.isalpha():
        c = c.lower()
        a_dict[c] = a_dict.get(c, 0) + 1
for c in sorted(a_dict.keys()):
    print(c, a_dict[c])
