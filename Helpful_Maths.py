MathEquation = input()
Equation = MathEquation.split('+')
Equation.sort()
XeniaMath = ""

for element in Equation[:-1]:
    XeniaMath += element + "+"
XeniaMath = XeniaMath + str(Equation[-1])


print(XeniaMath)
