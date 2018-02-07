import math
count = 0
n = int(input())
while n > 1:
	f = True 
	for i in range(2, round(math.sqrt(n))+1):
		if n % i == 0:
			f = False
	if f:
		count += 1
	n = int(input())
 
print("Было введено", count, "простых чисел")