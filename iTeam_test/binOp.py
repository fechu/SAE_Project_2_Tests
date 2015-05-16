def main(x):
	z = 0
	if (x * 2 - x == x):
		z = z + 1
	if (2 / 2 == 0 + 1):
		z = z+ 1
	if (4 % 2 == 0):
		z = z + 1
	if (4 ** 2 == 16):
		z = z + 1
	if ((x << 2) == x*4):
		z = z + 1
	if ((x << 2) >> 2 == x):
		z = z + 1
	if ((x**3) == 8):
		z = 10

	return z

def expected_result():
	return [6,10]