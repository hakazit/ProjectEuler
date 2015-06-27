# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

my_sum = 0
linecount = 0
with open("onehundred50digitnumbers.txt", "r") as test:
	for line in test:
		line = line.strip()
		my_sum += int(line)
		#print line
		#linecount += 1
#print linecount
print(my_sum)
print(str(my_sum)[:10])