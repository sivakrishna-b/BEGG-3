s=int(input())
b=[int(x) for x in input().split()]
b.sort()
for i in range(0,s):
		if(i<s-1):
				k=' '
		else:
				k=''
		print(b[i],end=k)
