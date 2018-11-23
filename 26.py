s=int(input())
e=[int(x) for x in input().split()]
e.sort()
for i in range(0,s):
		if(i<s-1):
				k=' '
		else:
				k=''
		print(e[i],end=k)
