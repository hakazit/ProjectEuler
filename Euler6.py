# Squares of first 100 natural numbers
sumsquare1, sumsquare2 = 0, 0

for num in range(1,101):
	sumsquare1 += num **2
	sumsquare2 += num
sumsquare2 = sumsquare2 **2
print(sumsquare2 - sumsquare1)