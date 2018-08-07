print ("nhap n")
#nhập n
n= int(input())
i = 2
#Kiểm tra xem số nào là số nguyên tố
while i < n:
    j = 2
    while j <= i // j:
        if i % j == 0:
            break
        j = j + 1
    else:
        print (i)
    i = i + 1
 