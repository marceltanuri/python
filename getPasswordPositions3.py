import sys

# Reads params from console:
#   1: Password
#   2, 3 and 4: Positions of password
# Prints:
#   Password positions
def printPositions3():
    password = sys.argv[1]
    
    x = int(sys.argv[2][0]) - 1
    y = int(sys.argv[2][1]) - 1
    z = int(sys.argv[2][2]) - 1
    print("Your code: ", "\n"+password[x], password[y], password[z])

# Validates params existence
if len(sys.argv) < 3:
    print("Missing params. You should enter your password and 3 numeric digits for positions")
else:
    printPositions3()
    
