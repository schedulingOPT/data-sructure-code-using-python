def solve1(a,b):
    for x in range(0,a+1):
        for y in range(0,a+1):
            if x+y==a and 2*x+4*y==b:
                print("x=%d,y=%d"%(x,y))


def solve2(a,b):
    for x in range(0,min(a,b//2)+1):
        for y in range(0,min(a,b//4)+1):
            if x+y==a and 2*x+4*y==b:
                print("x=%d,y=%d"%(x,y))

def solve3(a,b):
    for x in range(0,min(a,b//2)+1):    
        if 2*x+4*(a-x)==b:
            print("x=%d,y=%d"%(x,a-x))

a=3
b=8
solve2(a,b)               