"""
Assignment Qstn 1
Finds if a number is palindrome or not.

"""

num = int(input('Enter a number: '))
num_copy = num
reversed_num = 0

#print(num,num_copy,reversed_num)

#print("while loop starts")
while(num > 0):
  #print(num)
  digit = num % 10
  #print(digit)
  reversed_num = (reversed_num * 10) + digit
  #print(reversed_num)
  num = num // 10

if(num_copy == reversed_num):
  print(str(num_copy) + " is a palindrome number")
else:
  print(str(num_copy) + " is not a palindrome number")

