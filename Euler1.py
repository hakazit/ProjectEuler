# Sum of all multiples of 3 or 5 below 1000 -- Project Euler 1
sum  = 0
for num in range(1,1000):
	if(num%5 == 0 or num%3 == 0):
		sum += num
print sum