"""
Assignment Qstn 2

Program to find the sum of the following series
	Series: 1/1! + 2/2! +3/3! + …. + N/N!

"""
 
def seriesSum(number):
  result = 0
  factorial = 1

  for i in range(1, num+1):
    factorial = factorial * i
    result = result + (i / factorial)
  return result

num = int(input('Enter the series limit: '))
print("Sum of the series with limit ", num, "is", seriesSum(num))


"""
def sumOfSeries(num):
     
    res = 0
    fact = 1
     
    for i in range(1, num+1):   
        fact *= i
        res = res + (i/ fact)

         
    return res

n = int(input('Enter a number: '))     
#n = 5
print("Sum: ", sumOfSeries(n))
"""