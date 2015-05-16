def my_func(aa,bb):
    if (aa>2):
        return 200
    elif (aa==1):
        return 6
    else:
        return 1
def foo(x):
    if (x>10):
        return 1
    else:
        return 2

def main ( x ):
    #((a,b),c) = ((1,(1,20)),3)
    #(bb,bbb)=b
    bbbb = foo(foo(my_func(x,foo(x))))
    #return bbbb
    #return bbb
    #assert(my_func(x,x)>6)
    #y = my_func(x,20)
    y = my_func(x,20)
    #x = x + 10
    
    #assert(my_func(x,x)<200)
    
    yy = my_func(x,20)
    #bla = (my_func(x,x)==5)
    #assert(not bla)
    #return 0
    if (x>15):
        if (y>300):
            return 1
        else:
            return 2
    else:
        # doesn not yet reach that
        # todo
        return 2211122
    return 2


