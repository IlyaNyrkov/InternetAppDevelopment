import sys 

# 1 -10 9 // 3 -3 1 -1
# 1 -5 4 // 2 -2 1 -1
# 1 -25 144 // 4 -4 3 -3

def SolveBiquadricEquasion(A, B, C):
    result = []
    if (A != 0):
        D = B * B - 4 * A * C
        y1 = (-B + D**(1/2)) / 2 * A
        y2 = (-B - D**(1/2)) / 2 * A
        if (y1 > 0):
            result.append(y1**(1/2))
            result.append(-1 * y1**(1/2))
        if (y2 > 0 and y2 != y1):
            result.append(y2**(1/2))
            result.append(-1 * y2**(1/2))
    else:
        if B * C < 0:
            result.append((-1 * (C / B))**(1/2))
            result.append(-1 * (-1 * (C / B))**(1/2))
    return result

A = 0
B = 0
C = 0

if len(sys.argv) == 4:
    #first arg is program name
    if not sys.argv[1].lstrip('-').isdigit():
        print ("Wrong command line A argument")
        exit()
    A = float(sys.argv[1])
    if not sys.argv[2].lstrip('-').isdigit():
        print ("Wrong command line B argument")
        exit()
    B = float(sys.argv[2])
    if not sys.argv[3].lstrip('-').isdigit():
        print ("Wrong command C line argument")
        exit()
    C = float(sys.argv[3])
elif len(sys.argv) != 1:
    print("Invalid command line arguments count")
    exit()
else:
    condition = False
    #do while loop imitation, user keeps entering coefficient if it's wrong
    #other implementation could be through try catch 
    UserInput = ""
    while not condition:
        print("Enter A coefficient: ")
        UserInput = input()
        #condition becomes true in case of right input, loop ends
        #lstrip to remove '-', isdigit thinks input is string if first symbol is '-', but it's number
        condition = UserInput.lstrip('-').isdigit()
    A = float(UserInput)

    while not condition:
        print("Enter B coefficient: ")
        UserInput = input()
        condition = UserInput.lstrip('-').isdigit()
    B = float(UserInput)

    while not condition:
        print("Enter C coefficient: ")
        UserInput = input()
        condition = UserInput.lstrip('-').isdigit()
    C = float(UserInput)

print(A, B, C)
result = SolveBiquadricEquasion(A, B, C)
for i in range(len(result)):
    print("x", i + 1, "=", sep='', end='')
    print(result[i])
