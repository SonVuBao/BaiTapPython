import random
qty = 1000
randPoints = []
i = 0
while i<qty:
    x = random.randint(0,300)
    y = random.randint(0,400)
    if (x,y) not in randPoints:
    	randPoints.append((x,y))
    	i += 1
    else:
    	continue
print (str(randPoints))