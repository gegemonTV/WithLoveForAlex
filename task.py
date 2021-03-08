# 149
print("x y z F")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            F = (not y or x) and (not z or y)
            F = int(F)
            print(x, y, z, F)


# 173

print("x y z w F")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = x or (z and not w) or (y and not w) or (y and not z)
                F = int(F)
                print(x, y, z, w, F)
# 186

print("x y z F")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            F = (x and y) or (not x and not z)
            F = int(F)
            print(x, y, z, F)
# 198

print("x y z w F")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = (not w or y) and ((not x or z) == (not y or x))
                F = int(F)
                print(x, y, z, w, F)
