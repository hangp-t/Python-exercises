#2.2
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
