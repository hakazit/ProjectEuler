# Euler 16
# Sum of digits of 2 ** 1000
easy_sum = 0
str_start = str(2**1000)
for char in str_start:
	easy_sum += int(char)
print easy_sum
