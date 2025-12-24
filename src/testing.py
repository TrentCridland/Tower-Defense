import math
from sympy import sqrt, simplify, Integer

#d = sqrt(8)
#print(simplify(d))

# step 1: move all non-variables to right-side

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
print("")

#print(k.as_coeff_Mul())

def gcd(number_one : int, number_two : int):
    highest_selection = 0
    smallest_number = 0
    if number_one >= number_two:
        smallest_number = number_two
    else:
        smallest_number = number_one

    loop = 1
    for i in range(int(smallest_number)):
        if number_one%loop == 0 and number_two%loop == 0:
            highest_selection = loop
        loop += 1
    return highest_selection

def equation(a : int, b : int, c : int):
    print(b*b-4*a*c)
    highest_selection = gcd(abs(int((b*-1)+math.sqrt((b*b-4*a*c)))), abs(2*a))
    if ((b*-1)+math.sqrt((b*b-4*a*c))).is_integer():
        print("positive:", ((b*-1)+math.sqrt((b*b-4*a*c)))/highest_selection, "/", (2*a)/highest_selection)
    else:
        #print("positive:", round((b*-1)+math.sqrt((b*b-4*a*c)), 2), "/", (2*a))
        highest_selection = gcd(int(sqrt(b*b-4*a*c).as_coeff_Mul()[0]), 2*a)
        print("positive:", str(b*-1/(2*a))+" + ("+str(sqrt(b*b-4*a*c).as_coeff_Mul()[0]/highest_selection)+"*"+str(sqrt(b*b-4*a*c).as_coeff_Mul()[1])+")", "/", str((2*a)/highest_selection)+")")


    highest_selection = gcd(abs(int((b*-1)-math.sqrt((b*b-4*a*c)))), abs(2*a))
    if math.sqrt((b*b-4*a*c)).is_integer():
        print("negative:", ((b*-1)-math.sqrt((b*b-4*a*c)))/highest_selection, "/", (2*a)/highest_selection)
    else:
        highest_selection = gcd(int(sqrt(b*b-4*a*c).as_coeff_Mul()[0]), 2*a)
        print("negative:", str(b*-1/(2*a))+" - ("+str(sqrt(b*b-4*a*c).as_coeff_Mul()[0]/highest_selection)+"*"+str(sqrt(b*b-4*a*c).as_coeff_Mul()[1])+")", "/", str((2*a)/highest_selection)+")")

equation(a, b, c)
