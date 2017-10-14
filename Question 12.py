"""
Challenge:
Create a time formatter that takes time of day in hours (h, integer 0 to 23)
and minutes (m, integer 0 to 59). It should round the minutes to the nearest 5,
say "o'clock" when it's 0 minutes, "half-past" when it's 30 minutes.
For less than 30 minutes, it has to use "past" format and more than 30 minutes,
it uses "to" format.
"""

def time_format(h, m):
    if h < 0 or h >= 24 or m < 0 or m >= 60:
      print('Please enter a valid time.')
    if m == 0: 
      print ("It is",h,"o'clock")
    elif m == 30:
      print ("It is half-past", h)
    elif m < 30:
      print ("It is",round(m/5)*5, "minutes past",h)
    elif m > 30:
      print ("It is", 60-m, "minutes to", h+1)
