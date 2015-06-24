# Sum of even valued fibonacci sequence whose values don't exceed 4million
# answer starts at 2 because with this logic 2 is an edge case so by starting at 2
# it allows for num3 to be a unique even check
num1,num2,answer = 1,2,2
while(num1 < 4000000 and num2 < 4000000):
	num3=num1+num2
	if(num3 %2 == 0):
		answer+=num3
	#print "Num1: %d, Num2: %d, Num3: %d" % (num1,num2,num3) # This line is to check that fib seq is working correctly
	num1,num2=num2,num3
print answer