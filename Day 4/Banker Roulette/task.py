import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

payee = random.randint(0,4)

#Option 1
if payee == 0:
    print(friends[0])
elif payee == 1:
    print(friends[1])
elif payee == 2:
    print(friends[2])
elif payee == 3:
    print(friends[3])
else:
    print(friends[4])

#Option 2
print(friends[payee])

#Option 3
print(random.choice(friends))

