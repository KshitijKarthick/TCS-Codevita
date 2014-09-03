#! /usr/bin/env/python
#f1=open("2.in","r")
#f2=open("2.out","w")
#list=(f1.read()).split("\n")
#f1.close()
n=int(raw_input());
i=long(0)
list=list()
while i<n*3:
	list.append(raw_input())
	#print list
	i=i+1
i=0
j=long(0)
while i<n :
	N,T=list[j].split()
	j=j+1
	E=list[j].split()
	j=j+1
	P,D=list[j].split()
	j=j+1
	k=0
	E.sort()
	while k<int(N) and k<int(T):
		if(P>int(E[k])):
			P=int(P)+(int(P)-int(E[k]))
		k=k+1
	if(int(P)>=int(D)):
		print("Yes")
		#f2.write("Yes\n")
	else:
		print("No")
		#f2.write("No\n")
	i=i+1
#f2.close()