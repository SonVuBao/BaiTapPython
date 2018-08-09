from collections import Counter
#Mở kết nối tới file input.txt
file=open("input.txt","r+")
#Đọc file và tách từng từ và đếm số lần xuất hiện của từ
wordcount= Counter(file.read().split())
for word in file.read().split():
	if word not in wordcount:
		wordcount[word] =1
	else:
	    wordcount[word] +=1
file.close()
#Tạo file output.txt và lưu kết quả vào đó
fo = open("output.txt","w+")
fo.write(str(wordcount))
fo.close()
