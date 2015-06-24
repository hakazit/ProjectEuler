# Largest Palindrome made from 3 products, ex. largest 2 digit is 9009 = 91 * 99
# 999 * 999 = 998001 so 6 characters is most we will have to deal with
# Warning, sloppy code ahead
num1, num2 = 999,999
answers = []
while num1 > 0:
	while num2 > 0:
		product = num1 * num2
		if str(product)[:3] == str(product)[-3:][::-1]:
			answers.append(product)
			break
		num2-=1
	# Next round
	num2=999
	num1-=1
answers.sort()
print answers[-1] # need last item (largest) since we sorted them