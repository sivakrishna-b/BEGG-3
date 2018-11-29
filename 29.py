a=int(input(" "))
b=0
v=a
for i in range(0,a+1):
		if(i%60==0 and i>=60):
				b+=1
				v-=60
print(b,v)
