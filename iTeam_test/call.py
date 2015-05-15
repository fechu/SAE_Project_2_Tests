def main(x, y):
	return func3(func1(x), func1(func2(y)))

def func1(x):
	if (x < 0):
		return -1
	elif (x == 0):
		return 0
	else:
		return 1

def func2(x):
	z = 1
	if (x * x < 0):
		z = 0
	if (x > z):
		z = x
	else:
		z = -1
	return z

def func3(x, y):
	if (x*y < y*y):
		return True
	else:
		if (x*x > y):
			return False
		return False