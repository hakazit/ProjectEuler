# 10,001st prime number
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

prime_counter = 0
num_a = 2
while(prime_counter != 10001):
	if(check_prime(num_a)):
		#print "Prime: ", num_a
		prime_counter += 1
		if(prime_counter == 10001):
			print num_a
	num_a+=1
