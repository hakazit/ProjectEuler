# Smallest Multiple 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

counter = 1
iftrue = 0
while iftrue == 0:
	for num in range(1,21):
		if(counter % num != 0):
			break
		if(num == 20):
			print counter
			iftrue = 1
			break
	counter +=1