def main (x):
	#bool is subtype of int, where True == 1 and False == 0
	x = True
	y = False
	if (x - 1 == y):
		return 1
	return -1

def expected_results():
	return [1]