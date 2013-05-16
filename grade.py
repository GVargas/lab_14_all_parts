"""
grade.py
=====
Translate a numeric grade to a letter grade.
1. Ask the user for a numeric grade.
2. Use the table below to calculate the corresponding letter:
    90-100 - A
    80-89  - B
    70-79  - C
    60-69  - D
     0-59  - F
3. Print out both the number and letter grade.
4. If the value is not numeric, allow the error to happen.
5. However, if the number is not within the ranges specified in the table, output:
    "Could not translate %s into a letter grade" where %s is the numeric grade"

Example Output (consider text after the ">" user input):

Run 1:
-----
What grade did you get?
> 59
Number Grade: 59
Letter Grade: F

Run 2:
-----
What grade did you get?
> 89
Number Grade: 89
Letter Grade: B

Run 3:
-----
What grade did you get?
> 90
Number Grade: 90
Letter Grade: A

Run 4:
-----
What grade did you get?
> -12
Couldn't translate -12 into a letter grade
"""

grade = raw_input('What grade did you get? \n>')

if int(grade) <= 100 and int(grade) >=90:
	print('Number Grade:' + grade)
	print('Letter Grade: A')

elif int(grade) <= 89 and int(grade) >=80:
	print('Number Grade:' + grade)
	print('Letter Grade: B')

elif int(grade) <= 79 and int(grade) >=70:
	print('Number Grade:' + grade)
	print('Letter Grade: C')

elif int(grade) <= 69 and int(grade) >=60:
	print('Number Grade:' + grade)
	print('Letter Grade: D')

elif int(grade) <= 59 and int(grade) >=0:
	print('Number Grade:' + grade)
	print('Letter Grade: F')

else:
	print('Sorry! can\'t translate that to a letter grade')