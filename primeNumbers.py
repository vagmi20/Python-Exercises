num = input("Enter a number: ")
isPrime = True
for i in range(2, int(num)):
	if int(num) % i == 0: 
		isPrime = False
		break
if isPrime:
	print("the number is prime")
else:
	print("the number is not prime")
