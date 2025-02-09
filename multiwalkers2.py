d = int(input("Get distance: "))
t = int(input("Get time: "))
speed = d/t
fastest = speed
walker = [1]
i = 1
while i <5:
    
    d = int(input("Get distance: "))
    t = int(input("Get time: "))
    speed = d/t

    if speed > fastest:
            fastest = speed
            walker = [i + 1]
    if speed == fastest:
            walker.append(i+1)
    i = i + 1

    

print("Fastest walker is :", walker)
