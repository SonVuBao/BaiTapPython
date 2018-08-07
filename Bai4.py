import threading

print ("nhap n")
n = int(input())
i=1
x= n/2
Sum1 =0
Sum2 =0
#thread 1 tính từ 1-n/2
def Thread1():
   global i
   global Sum1
   while i<n/2:
      Sum1 = Sum1+i
      i=i+1

   print("Thread1:", Sum1)
#thread 2 tính từ n/2-n
def Thread2():
   global x
   global Sum2
   while x<=n:
      Sum2= Sum2 + x
      x= x +1
   print("Thread2:",Sum2)

#Gắn hành động cho các thread
thread1 = threading.Thread(target=Thread1)
thread2 = threading.Thread(target=Thread2)

#Bắt đầu thread
thread1.start()
thread2.start()

#thread 1 và thread 2 bị ngắt
thread1.join()
thread2.join()
print("Tong",Sum1 + Sum2)

