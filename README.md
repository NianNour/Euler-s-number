# Euler-s-number
It calculates an approximation of Euler's number e raised to the power of a user-inputted value x.
calculates an approximation of Euler's number e raised to the power of a user-inputted value x. Here's a breakdown of what each part does:

Functions:

power(num1, num2): This function simply calculates the power of num1 raised to num2 using the built-in ** operator (for example, 2**3 would return 8).

factorial(number): This function calculates the factorial of a non-negative integer number. The factorial of a number is the product of all positive integers less than or equal to that number. For example, factorial(5) would return 120 (5 * 4 * 3 * 2 * 1).

e_func(x): This function is the core of the code, and it calculates an approximation of e^x. It does this by using a series expansion, which is a way of writing a complex function as an infinite sum of simpler functions. In this case, the series expansion used is:

e^x = 1 + x + x^2/2! + x^3/3! + ...
where n! represents the factorial of n. The function iterates through 100 terms of this series to get an approximation of e^x.

main(): This function is the entry point of the program. It prompts the user to enter a value for x, calls the e_func(x) function to calculate the approximation, and then prints the result.

P.S: I just read about PEP 8. and now i can tell the diffrances between my previous programs. :)  I hope my next programms be  better than this. Keep going!!
