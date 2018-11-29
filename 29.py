c=int(input(" "))
k=0
v=c
for i in range(0,c+1):
		if(i%60==0 and i>=60):
				k+=1
				v-=60
print(k,v)
