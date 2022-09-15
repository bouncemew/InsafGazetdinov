num = [x for x in range(100) if x%2 !=0]
cube = [x**3 for x in range (100) if  x%2 != 0]
i = 0
for char in range(len(cube)):
    print(num[i] , cube[i])
    i += 1