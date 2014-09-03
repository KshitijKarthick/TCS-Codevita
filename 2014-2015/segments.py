k=[]
input=raw_input()
input=input.strip()
input=input.rstrip()
input=input.lower()
s=""
for x in input:
	if x!='.' and x!='!' :
		s=s+x
words=s.split()
l=(raw_input()).split()
w1=(raw_input()).lower()
w2=(raw_input()).lower()
count=0
for x in range(words.__len__()):
	if words[x] == w1:
		y=0
		while y<l.__len__(): 
			if ((x+int(l[y])<words.__len__()) and (words[x+int(l[y])] == w1)) or ((x+int(l[y])<words.__len__()) and ((words[x+int(l[y])] == w2))) :
				count=count+1
				z=x
				while z<int(l[y])+1:
					print words[z]
					z=z+1
				break
			y=y+1
	elif words[x] == w2:
		y=0
		while y<l.__len__(): 
			if words[x+int(l[y])] == w1 or words[x+int(l[y])] == w2 :
				count=count+1
				print words[x],y,words[x+int(l[y])]
				z=x
				while z<int(l[y])+1:
					print words[z]
					z=z+1
				break
			y=y+1
print count

