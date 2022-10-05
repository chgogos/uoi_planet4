# for each person a tuple is created consisting of name, age, height
person1 = ("Nick", 32, 1.80)
person2 = ("Kate", 28, 1.60)
persons = (person1, person2, ("Jim", 25, 190))
for name, age, height in persons:
    print(name, age, height)
