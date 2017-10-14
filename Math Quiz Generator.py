import random
import cmath

###############################################
#Primary School Code
def primary_school_quiz(flag, n):
    final_score = 0  #score starts at 0
    count = 0        #count starts at 0
    if flag == 0:    #if student selects substraction
        for count in range(n):
            print ("Question ", count+1)
            num1 = random.randint(0, 9)
            num2 = random.randint(0, 9)

            correct_result = num1 - num2

            print ("What is", num1, "-", num2,"?")
            user_answer= int(input("Your answer: "))

            if user_answer == correct_result:
                final_score += 1    #adds one point if answer is correct
                print ("Correct!")
                
            else:
                print ("You did well " + name + ", but I know you can do better.")

    elif flag == 1:  #if student selects exponentiation
        for count in range (n):
            print ("Question ", count+1)
            num1 = random.randint(0, 9)
            num2 = random.randint(0, 9)

            correct_result = num1 ** num2

            print ("What is", num1, "to the power of", num2,"?")
            user_answer= int(input("Your answer: "))

            if user_answer == correct_result:
                final_score += 1    #adds one point if answer is correct
                print ("Correct!")
                
            else:
                print ("You did well " + name + ", but I know you can do better.")
                
    else:
        print("Choose either 0 or 1.")

    return final_score


#############################################
#High School Code
def high_school_eqsolver(a,b,c):
    # find two solutions
    x1 = (-b+cmath.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-cmath.sqrt(b**2-4*a*c))/(2*a)
    print ("The quadratic equation\n", a, "*x^2 + ", b,"*x + ", c, " = 0\n has the following two complex roots:\n", x1,"\nand\n", x2)
    while question == ('yes' or 'y' or 'ye' or 'Yes' or 'yeah' or 'Yeah'):
        return


################################################
#Code for welcome message and option selection
name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for primary school\n2 for high school or\n3 for none of the above?\n")


################################################
#Welcome for primary school quiz
if status =='1':
    
    #Welcome plaque for primary school
    print(5*"*" + 59*"*" + len(name)*"*" + 5*"*")
    print("*" + 67*" " + len(name)*" " + "*")
    print("*  __" + name + ", welcome to my quiz-generator for primary school students.__  *")
    print("*" + 67*" " + len(name)*" " + "*")
    print(5*"*" + 59*"*" + len(name)*"*" + 5*"*")

    #Choose substraction or exponention
    flag=int(input(name+" what would you like to practice? Enter \n0 for substraction\n1 for exponentiation\n"))

    #Must enter valid number of questions to practice which is either 0 or 1
    while True:
        n=int(input("How many practice questions would you like to do?\n"))
        try:
            n = int(n)
            if int(n) < 0:
                print ("You must enter a positive number! Try again")
                continue
            break
        except ValueError:
                print("That's not an integer! Try again")
    print (name + ", here are your " + str(n) + " questions")

#############################################
#Score board
    final_score = primary_school_quiz(flag, n)
    score_percent = round(final_score/n,2)
    if final_score >= 0.9:
        print("Congratulations" +name+"! You’ll probably get an A tomorrow. Now go eat your dinner and go to sleep.")

    elif final_score >= 0.7:
        print("You did well" +name+ "Ena, but I know you can do better.")

    elif final_score < 0.7:
        print("I think you need some more practice "+name+" .")


##################################################
#Welcome for high school quiz
elif status =='2':
    #Welcome plaque for high school
    print(5*"*" + 52*"*" + len(name)*"*" + 5*"*")
    print("*" + 60*" " + len(name)*" " + "*")
    print("*  __quadratic equation, a*x^2 + b*x + c = 0, solver for " + name + "__  *")
    print("*" + 60*" " + len(name)*" " + "*")
    print(5*"*" + 52*"*" + len(name)*"*" + 5*"*")

    #Want to solve a quadratic equation
    while True:
        question = input(name+", would you like a quadratic equation solved?\n")
        try:
            if question in {'yes', 'y','ye','Yes','yeah','ok','okay'}:
                print ("Good choice!")
                a = float(input("Enter a number the coefficient a:"))
                b = float(input("Enter a number the coefficient b:"))
                c = float(input("Enter a number the coefficient c:"))
                high_school_eqsolver(a,b,c)
                continue
            break
        except ValueError:
            print("Good bye "+name+"!")


###################################################            
#You are not in primary school or high school    
else:
    print(name+" you are not a target audience for this software.")
    pass
print("Good bye "+name+"!")
