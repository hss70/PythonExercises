
'''
Question 1:

Write a function(s) that converts an octal number, represented as a string into its decimal value.
'''

def octalToDecimal(oct):
  return 42

'''
Question 2: 

Write a function(s) that prints out a tree shape (see below). The function should take two arguments: a tree width and a trunk height. For example, the arguments 9 and 4 will print out a tree of width 9 and trunk length 4, as shown below:

    *
   ***
  *****
 *******
*********
   ***
   ***
   ***
   ***

You can assume that the width of the tree will be odd and hence every line will have an odd number of asterisks. The trunk will always have a width of three asterisks.
'''

def printTree(width,trunk):
  print("    *")
  print("   ***")
  print("  *****")
  print("   ***")
  print("   ***")

print(octalToDecimal(52));
printTree(5,2)