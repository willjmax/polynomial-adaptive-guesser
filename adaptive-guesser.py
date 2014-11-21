import sys

def polynomial(coeffs, x):
	sum = 0
	degree = 0
	first = True
	for num in sys.argv:
		if not first:
			sum += int(num) * (x**degree)
			degree = degree + 1
		else:
			first = False	
		
	return sum

poly_array = []
N = polynomial(sys.argv, 1) + 1 #solving the polynomial at 1 gives the summation of the coefficients
pN = polynomial(sys.argv, N) #pN = a_0 + a_1N + a_2N^2 ...
a = pN % N #this equals a_0, as a_0 is the only term not divisible by N (N bigger than all coefficients
#poly_array.append(a)

y = pN
while y > 0:
	poly_array.append(a)
	y = (y - a) / N #subtract off current coefficient, divide by N to factor the next coefficient
	a = y % N


print poly_array
	







