"""
Write a function called series_sum() that prompts the user for an non-negative integer n. If the user enters a negative
integer the function should return None otherwise the function should return the sumer of the following series 1000 +
1=12 + 1=22 + 1=32 + 1=42 + ::: + 1=n2 for the given integer n.
"""

def series_sum(n):
    if n < 0:
        print ("None")
    elif n == 0:
        print (1000)
    elif n > 0:
        sum = 1000 #starts at 1000 and then adds
        for i in range (1, n+1, 1): # range (start at 1, ends at n+1, step of 1)
            sum += (1/(i**2)) 
        print (sum)

n=int(input("Please enter a non-negative integer: "))
series_sum(n)
