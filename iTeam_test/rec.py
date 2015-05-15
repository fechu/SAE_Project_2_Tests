def main ( x ):
	return rec_func(x)

def rec_func ( x ):
	if (x == 0):
		return 1
	elif (x < 0):
		return -1
	else:
		return rec_func(x - 1)
	#unreachable
	return 2

def expected_results():
	return [-1, 1]