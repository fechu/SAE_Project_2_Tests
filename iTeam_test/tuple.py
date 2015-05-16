def main(x, y):
	z = ((x, y), 0)
	if (z == ((y, x), x)):
		return x == 0
	elif (z == func(x)):
		return x == y
	else:
		return x != y

def func(x):
	return ((x, x), 0)

def expected_results():
	return [True]