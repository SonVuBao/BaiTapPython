print ("nhap n")
#nhập n
n= int(input())
i = 2
#Kiểm tra xem số nào trong mảng là số nguyên tố bằng cách chia cho các số bé hơn số đó 
while i < n:
    j = 2
    while j <= i//2:
        if i % j == 0:
            break
        j = j + 1
    else:
        print (i)
    i = i + 1 
