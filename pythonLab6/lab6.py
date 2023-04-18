import math

#Question 1
n = int(input("Enter value of n: "))
x = int(input("Enter value of x: "))

terms = [(lambda i: n**i/math.factorial(i))(i) for i in range(x+1)]

result = sum(terms)

result += 1

print(f"e^{n} = {result}")

#Question 2
sum = 0
first_input = int(input("Please enter a number : "))
def calculateSum(n):
    global sum
    if n == 0:
        return
    else:
        sum += (-1)**(n+1)/n
        calculateSum(n-1)

calculateSum(first_input)
print("Sum: ",sum)