from collections import Counter
file=open("C:\\Users\\Dell\\Desktop\\New folder\\input.txt","r+")
wordcount= Counter(file.read().split())
for word in file.read().split():
	if word not in wordcount:
		wordcount[word] =1
	else:
	    wordcount[word] +=1
file.close()
fo = open("output.txt","w+")
fo.write(str(wordcount))
fo.close()