"""
Function casual_number(s) should return an integer representing a number in s. If s does not look like a number the function should 
return None. Take out the commas that separate the thousands.
"""
def casual_number(s):
    if any(c.isalpha() for c in s): #if any character in the string is a letter, print "None"
        print ("None")
    elif any(c.isdigit() for c in s): #if any character in the string is a number, print the string and delete any comma
        print (s.replace(",",""))
