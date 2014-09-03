#! /usr/bin/env/python
#f1=open("3.in","r")
#f2=open("3.out","w")
#list=(f1.read()).split("\n")
#f1.close()
n=input();
i=long(0)
list=list()
while i<n:
	list.append(input())
	i=i+1
i=0
flag=1
while i<n :
	N=int(list[i])
	while N>0:
		if(N>4):
			N=N-4
			flag=1
		else:
			N=N-1
			flag=1
		if(N==1):
			flag=0
		if(N>4):
			N=N-4
		else:
			N=N-1
	if(flag==1):
		print("Yes")
		#f2.write("Yes\n")
	else:
		print("No")
		#f2.write("No\n")
	i=i+1
#f2.close()