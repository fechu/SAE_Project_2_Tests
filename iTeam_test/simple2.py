def main(x):
	if (x>0):
		y = a() + b()
		return y
	elif (x==-3):
		return 0
	else:
		return b()-a()

def a():
	return 1


def b():
	return 2

def expected_result():
	return [0,3,1]