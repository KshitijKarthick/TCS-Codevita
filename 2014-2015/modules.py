def dfs(v):
	i=1
	visited[i]=1
	while i<=n:
		if m[v][i]==1 and (not visited[i]):
			l.append(i)
			#print v,"->",i
			dfs(i)
		i=i+1
n=long(0)
e=long(0)
u=0
v=0
list=list()
list=(raw_input()).split()
n=long(list[0])
e=long(list[1])
visited=[0 for x in xrange(n+1)]
m=[[0 for x in xrange(n+1)] for x in xrange(n+1)]
for x in range(1,e+1):
	list=(raw_input()).split()
	u=long(list[0])
	v=long(list[1])
	m[u][v]=1
e=long(raw_input())
list=(raw_input()).split()
l=[]
for x in range(e):
	dfs(long(list[x]))
list=[]
for x in range(1,n+1):
	if l.count(x) == e:
		list.append(x)
list.sort()
for x in list:
	print x,


