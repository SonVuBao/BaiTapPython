import random
qty = 1000
randPoints = [(131,328)]
i = 0
#lấy random các điểm nằm trong mặt phẳng lặp đi lặp lại 1000 lần 
while i<qty:
    x = random.randint(0,300)
    y = random.randint(0,400)
   	#nếu điểm random mời trùng với random cũ thì random lại cho đến khi không lặp
    if (x,y) not in randPoints:
    	randPoints.append((x,y))
    	i += 1
    else:
    	continue
print (str(randPoints))
