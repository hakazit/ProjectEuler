# Index of the 1000 digit fibonacci number
def check_num_length(check_num):
	if(len(str(check_num)) == 1000):
		return True
	return False

fib_index = 2
number1 = 1
number2 = 1
while(True):
	number1 += number2
	fib_index += 1
	if(check_num_length(number1)):
		#print number1
		print fib_index
		break
	number2 += number1
	fib_index += 1
	if(check_num_length(number2)):
		#print number2
		print fib_index
		break