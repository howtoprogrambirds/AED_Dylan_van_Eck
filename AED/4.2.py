import random

while(1):
    dct = {}
    for i in range(0,10000):
        broken_number = random.uniform(0, 1)
        dct[broken_number] = hash(broken_number)

    tempSet = set(dct.values())
    if len(tempSet) < len(dct.values()):
        break

print("start")
lst = list(dct.keys())
def find_hash_Couple():
    for hashed in dct:
        count = 0
        for i in range(0, 10000):
            if dct[hashed] == dct[lst[i]]:
                count += 1
            if count > 1 and hashed != lst[i]:
                print("hash(",(repr(hashed)), ") == hash(", lst[i],") == ", dct[hashed])
                break
find_hash_Couple()
print("done")