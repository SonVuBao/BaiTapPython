print ("nhap n")
#nhập n
n= int(input())
i = 2
#Kiểm tra xem số nào là số nguyên tố
while(i < n):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : 
   	print (i)
   i = i + 1
