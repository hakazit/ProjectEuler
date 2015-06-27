# Factorial of 100!, sum of digits
import math
easy_sum = 0
str_start = str(math.factorial(100))
for char in str_start:
	easy_sum += int(char)
print easy_sum