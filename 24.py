s=int(input())
c=[int(x) for x in input().split()]
c.sort()
for i in range(0,s):
		if(i<s-1):
				k=' '
		else:
				k=''
		print(c[i],end=k)
