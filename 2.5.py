#2.5
def casual_number(s):
    if any(c.isalpha() for c in s): #if any character in the string is a letter, print "None"
        print ("None")
    elif any(c.isdigit() for c in s): #if any character in the string is a number, print the string and delete any comma
        print (s.replace(",",""))
