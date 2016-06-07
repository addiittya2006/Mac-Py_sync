def power(x, y):
	if y == 0:
		return 1
	else:
		return x*power(x, y-1)

def pow1(x, y):
	if y==0:
		return 1
	elif y==1:
		return x
	else:
		if y%2==0:
			return pow1(x*x,y/2)
		else:
			return x*pow1(x*x,y/2)

print power(3,2)
print pow1(4,2)