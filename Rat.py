#! /usr/bin/env/python
#f1=open("1.in","r")
#f2=open("1.out","w")
#list=(f1.read()).split("\n")
#f1.close()
#n=long(list[0])
#del list[0]
i=long(0)
n=input();
i=long(0)
list=list()
m=[[0 for x in xrange(n)] for x in xrange(n)]
while i<n:
	list.append(raw_input())
	for x in range(n):
		m[i][x]=list[x]
	i=i+1
R=input()
list=list()
k=0
while k<R:
	list.append(raw_input())
	x,y=list.split()
	m[i][j]="R"
	k=k+1
i=0
while i < R:
	if(x==0)
		
flag=1;
	
if(flag==1):
	print("Yes")
	#f2.write("Yes\n")
else:
	print("No")
#f2.write("No\n")
i=i+1
#f2.close()