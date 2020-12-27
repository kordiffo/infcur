# Код без комментариев
s,n = map(int, input().split())
a = []
for i in range(n):
	a.append(int(input()))
a.sort()
b=[]
for i in range(n):
	if sum(b) + a[i] < s:
		b.append(a[i])
	elif (sum(b) - a[i-1] + a[i] < s) and i > 0:
		del(b[-1])
		b.append(a[i])
	else:
		break
print (len(b), b[-1])
