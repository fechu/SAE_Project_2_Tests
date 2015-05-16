def main(x, y):
	z = 0

	if ((x < y) != z):
		#x < y
		return not(y >= x) #False
	elif (x == y):
		return x > y #False
	elif (x > y):
		return x <= y #False

def expected_results():
	return [0]