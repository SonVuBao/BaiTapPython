import threading

print ("nhap n")
n = int(input())
i=1
x= n/2
Sum =0
#thread 1 tính từ 1-n/2
def Thread1():
   global i
   global Sum
   while i<n/2:
      Sum = Sum+i
      i=i+1

   print("Thread1:", Sum)
#thread 2 tính từ n/2-n
def Thread2():
   global x
   global Sum
   while x<=n:
      Sum= Sum + x
      x= x +1
   print("Thread2:",Sum)

#Gắn hành động cho các thread
thread1 = threading.Thread(target=Thread1)
thread2 = threading.Thread(target=Thread2)

#Bắt đầu thread
thread1.start()
thread2.start()

#thread 1 và thread 2 bị ngắt
thread1.join()
thread2.join()
print("Tong",Sum)

