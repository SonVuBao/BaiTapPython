import threading

print ("nhap n")
n = int(input())
i=1
x= n/2
Sum =0
#thread 1 tính từ 1-n/2
def Thread(z,y):
   global Sum
   while z<y:
      Sum = Sum+z
      z=z+1

   print("Thread:", Sum)

#Gắn hành động cho các thread
thread1 = threading.Thread(target=Thread,args=(i,n/2))
thread2 = threading.Thread(target=Thread,args=(x,n+1))

#Bắt đầu thread
thread1.start()
thread2.start()

#thread 1 và thread 2 bị ngắt
thread1.join()
thread2.join()
print("Tong",Sum)
