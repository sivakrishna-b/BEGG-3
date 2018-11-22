n=int(input())
c=[int(x) for x in input().split()]
k=int((n+1)/2)
if(k%2==0):
		print(c[k-1],c[k])
else:
		print(c[k-1])
