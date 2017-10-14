# Python-exercises
Playing around with some exercises/quiz/assignments

#####
#Math Quiz Generator

1) Create a math quiz generator. Here are specifications:

primary_school_quiz(flag, n):
If flag is 0, the quiz helps practice subtraction. 
If flag is 1, the quiz helps practice exponentiation. 

The student will select the number of questions to answer(n).For each question, it generates two random positive, single-digit numbers and asks the student for the answer to the math problem with those two numbers (either subtract the second number from the first, or raise the first number to the power of the second number). 

At the end of n questions, performTest returns the number of questions answered correctly.

high_school_eqsolver: This function has three parameters a, b and c which are the coefficients of the quadratic equation ax2 + bx + c = 0. The function displays/prints the equation frist and then prints its solutions.
The function must display correct and meaningful solutions given any three real numbers for coefficients a, b and c.

2) Make it user-friendly:
primary_school_quiz(flag,n):
When it returns the number of correct answers, display a message to the student:
 If she did 90% or better, display on screen: Congratulations [name]! You’ll probably get an A tomorrow. Now
go eat your dinner and go to sleep. Good bye [name]!
 If she did 70% or better, but worse than 90%, display on screen: You did well [name], but I know you can do
better. Good bye [name]!
 If she did worse than 70%, display on screen: I think you need some more practice [name]. Good bye [name]!

high_school_eqsolver:
For high school students, in the main part of your program, you need to write some code that asks the pupil for the coefficients a, b and c. Then you need to make the call to high_school_eqsolver to display the solutions. After that your program should ask them if they would like another quadratic equation solved. If they says anything but yes the program terminates by printing a good bye message as in the examples.
