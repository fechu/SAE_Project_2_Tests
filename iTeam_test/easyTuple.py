def main (x, y):
	w = func(x)
	z = func(x)
	if ((w,z) == (func(x), func(y))):
		return 1
	else:
		return 2

def func (x):
	return x + 1

def expected_results():
	return [1]