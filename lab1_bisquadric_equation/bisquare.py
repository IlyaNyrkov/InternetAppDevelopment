import sys 
import cmath
# 1 -10 9 // 3 -3 1 -1
# 1 -5 4 // 2 -2 1 -1
# 1 -25 144 // 4 -4 3 -3

def numListToString(s):
    return ' '.join([str(elem) for elem in s])

def IsNumber(number):
    try:
        val = float(number)
        return True
    except ValueError:
        return False    

#===================================TASK==================================================
def SolveBiquadricEquasion(A, B, C):
    result = []
    if (A != 0):
        D = B * B - 4 * A * C
        y1 = (-B + cmath.sqrt(D)) / 2 * A
        y2 = (-B - cmath.sqrt(D)) / 2 * A
        result.append(y1**(1/2))
        result.append(-1 * y1**(1/2))
        result.append(y2**(1/2))
        result.append(-1 * y2**(1/2))
    else:
        if B * C < 0:
            result.append((-1 * (C / B))**(1/2))
            result.append(-1 * (-1 * (C / B))**(1/2))
    return result

def PrintCoefficients(coefficients):
    if len(coefficients) == 0:
        print("Equation doesn't have any solutions")
    else:
        print("Equation has", len(coefficients), "solutions:")
        for i in range(len(coefficients)):
            print("x", i + 1, "=", sep='', end='')
            print(coefficients[i])

#=======================================TESTING============================================
def Test1():
    A = 1
    B = -10
    C = 9
    answer = [3, -3, 1, -1]
    result = SolveBiquadricEquasion(A, B, C)
    assert answer == result, "wrong answer, expected " + numListToString(answer) + " but got " + numListToString(result)


def Test2():
    A = 1
    B = -5
    C = 4
    answer = [2, -2, 1, -1]
    result = SolveBiquadricEquasion(A, B, C)
    assert answer == result, "wrong answer, expected " + numListToString(answer) + " but got " + numListToString(result)

def Test3():
    A = 1
    B = -25
    C = 144
    answer = [4, -4, 3, -3]
    result = SolveBiquadricEquasion(A, B, C)
    assert answer == result, "wrong answer, expected " + numListToString(answer) + " but got " + numListToString(result)

def TestAll():
    Test1()
    Test2()
    Test3()
    print("ALL TESTS PASSED")


#======================================PROGRAM=============================================

#TestAll()

A = 0
B = 0
C = 0


if len(sys.argv) == 4:
    #first arg is program name
    if not IsNumber(sys.argv[1]):
        print ("Wrong command line A argument")
        exit()
    A = float(sys.argv[1])
    if not IsNumber(sys.argv[2]):
        print ("Wrong command line B argument")
        exit()
    B = float(sys.argv[2])
    if not IsNumber(sys.argv[3]):
        print ("Wrong command C line argument")
        exit()
    C = float(sys.argv[3])
elif len(sys.argv) != 1:
    print("Invalid command line arguments count")
    exit()
else:
    correctInput = False
    #do while loop imitation, user keeps entering coefficient if it's wrong
    #other implementation could be through try catch 
    UserInput = ""

    while not correctInput:
        print("Enter A coefficient: ")
        UserInput = input()
        #condition becomes true in case of right input, loop ends
        #lstrip to remove '-', isdigit thinks input is string if first symbol is '-', but it's number
        correctInput = IsNumber(UserInput)
    A = float(UserInput)

    correctInput = False
    while not correctInput:
        print("Enter B coefficient: ")
        UserInput = input()
        correctInput = IsNumber(UserInput)
    B = float(UserInput)

    correctInput = False
    while not correctInput:
        print("Enter C coefficient: ")
        UserInput = input()
        correctInput = IsNumber(UserInput)
    C = float(UserInput)

result = SolveBiquadricEquasion(A, B, C)
PrintCoefficients(result)
