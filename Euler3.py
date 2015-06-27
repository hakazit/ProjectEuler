# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

import math
def check_prime(check_num):
	#print "checking prime: %d" % check_num
	int_sqrt = int(math.sqrt(check_num))
	#print "intsqrt: %d" % int_sqrt
	for num in range(2, int_sqrt+1):
		if(check_num % num == 0):
	#		print "problem num: %d" % num
			return False
	return True

# King of the hill style logic
sqrt_imp = int(math.sqrt(600851475143))
current_answer = 2
for num in range(3, sqrt_imp+1, 2):
	if(check_prime(num) and 600851475143 % num == 0):
		if(current_answer < num):
			current_answer = num
print current_answer
