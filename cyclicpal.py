def pal():
	if word==word[::-1]:
		return 1
	else:
		return 0
def rshift():
	k=[]
	for x in word:
		k.append(x)
	k.insert(0,k.pop())
def lshift():
	k=[]
	for x in word:
		k.append(x)
	k.insert(word.__len__(),word[0])
	k.remove(word[0])
n=input()
l=[]
count1=0
count2=0
sol=[]
for x in range(n):
	l.append(raw_input())
	word=l[x]
	check1=-1
	check2=-1
	count1=count2=0
	for y in range(word.__len__()-1):
		rshift()
		check1=pal()
		count1=count1+1
		if check1==1:
			flag=count1
			break
		
	word=l[x]
	for y in range(word.__len__()-1):
		lshift()
		check2=pal()
		count2=count2+1
		if check2==1:
			flag=count1
			break
	if check1==-1 and check2==-1:
		sol.append(-1)
	elif count1<count2 and check1!=-1:
		sol.append(count1)
	elif count1<count2 and check1==-1:
		sol.append(count2)
	elif count2<count1 and check2!=-1:
		sol.append(count2)
	elif count2<count1 and check2==-1:
		sol.append(count1)
	else:
		sol.append(-1)
	print sol
for x in sol:
	print x,


