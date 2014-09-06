"""
the goal of this code is to find the square root of a number using a weird method I figured out with some friends of mine
many years ago (high school).  It's not efficent or anything, it's just something of a curiosity to me
"""

q = 1 # this is going to become the resultant number
target = input("What number do you want the square root of? ")
tolerance = .0000000000000001 #how close does it have to be to the real value of the square root to quit out
y = 1.1 # y is arbitrary, but I choose 1.1 for testing
# u = 1.0
count = 0
k = target - ((y**2)/4.0)
k = float(k)
target = float(target)
y = float(y)

while count <999999:
    q = (k / q) + y
    u = q - (y/2.0)
    count = count + 1
    #print u*u
    #print target
    float(target)
    float(u*u)
    if target - u*u < tolerance:
        print "should be done now"
		count = 9999999999999

print "square root of ", target, " is ", u

"""
print "q: ", q
print "k: ", k
print "y: ", y
print "u: ", u
print "u**2: ", u*u
"""