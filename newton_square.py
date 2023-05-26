def squareRoot(n, l) :

	x = n

	count = 0

	while (1) :
		count += 1

		root = 0.5 * (x + (n / x))

		if (abs(root - x) < l) :
			break

		x = root

	return root

if __name__ == "__main__" :

	n = int(input("Enter the number for calculating the square root :"))
	l = 0.00001

	print(squareRoot(n, l))

