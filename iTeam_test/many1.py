def foo(a,b,c,d):
	if (a>b):
		return c
	else:
		return d

def bar(e,f):
	if (e>f):
		return e
	else:
		return f

def baz(g):
	return 3*g+1

def same(x):
	return x

def main(x,y):
	h = baz(x)
	i = foo(x,y,h,x)

	if (bar(x,y)==same(h)):
		# for x=1 and y=4, we get h=4 and bar(1,4)=4 so we return 1
		return 1
	else:
		# else
		return 2

def expected_result():
	return [1,2]