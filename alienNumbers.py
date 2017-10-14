"""
Return 1024 for each T
Return 598 for each y
Return 121 for each !
Return 42 for each a
Return 6 for each N
Return 1 for each U
Add total of the string
"""

def alienNumbers(s):
    alienNumbers = str(s) #s must be a string
    return 1024*alienNumbers.count("T") + 598*alienNumbers.count("y") + 121*alienNumbers.count("!") + 42*alienNumbers.count("a") + 6*alienNumbers.count("N") + 1*alienNumbers.count("U")


