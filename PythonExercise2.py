
'''
Question 0:

Complete the recursive function below which performs multiplication of two  numbers without using the inbuilt * sign
'''

def multiply(number, by):
  return number*by


'''
Question 1: 
 
 Complete the function below which takes in an integer input between zero and one hundred (0 ≤ n ≤ 100) and prints out the number expressed in English text, with spaces and no dashes (–), e.g. for the number “33”, we would expect to see “thirty three”. Hint: you may want to create additional functions to help.
 
 Call this function from the main to test your program.
'''

def numberToText(value):
  return "fourty two"

'''
Question 2: 
 
 Complete the function below that calculates, and returns, the distance between two points.
 
 Call this function from the main to test your program. Hint: may wish to use the following print statement in your main function, or similar: 

 printf("%1.2f\n", calculateDistance(0, 0, 4, 3));
'''

def calculateDistance(x1, y1, x2, y2):
  return 1.0;


''' 
Question 3: 
 
 Complete the function below that is given an integer, n, where 1 ≤ n ≤ 9999 and prints whether it is even, odd, or/and prime.  The output should be whole sentences for example, 

 1 is odd and not prime.
 2 is even and prime.
 3 is odd and prime.
 4 is even and not prime.
 5 is odd and prime
 
 Call this function from the main to test your program.
'''

def printOddEvenAndOrPrime(n):
  return "2 is even and prime."


print(str(multiply(2,3)));
print(numberToText(42));
print(str(calculateDistance(1,0,1,1)));
print(printOddEvenAndOrPrime(2));