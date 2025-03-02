import random

selectList = ["Option A", "Option B", "Option C", "Option D"]

x = 0

while x != 1:
    print(selectList[random.randint(0, len(selectList)-1)])
    rng = input("Here's a selection!")