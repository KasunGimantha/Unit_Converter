print(
    "********************[Welcome to Unit Conversion programme]********************")
print("Enter")
print("L for Length")
print("W for Weight")
print("T for Temperature")
print()
main_choice = str(input("Enter option: "))


def length(l):

    # convert all units to one unit
    m = 1  # m to m
    k = 0.001  # m to km
    mi = 0.0006213  # m  to miles
    f = 3.2808  # m to feet

    a = l

    def miles(x):
        print(f"In Kilometers : {k/mi*x}")
        print(f"In Meters : {m/mi*x}")
        print(f"In Foot : {f/mi*x}")

    def feet(x):
        print(f"In Kilometers : {k/f*x}")
        print(f"In Meters : {m/f*x}")
        print(f"In Miles : {mi/f*x}")

    def kilometers(x):
        print(f"In Meters : {m/k*x}")
        print(f"In Miles : {mi/k*x}")
        print(f"In Foot : {f/k*x}")

    def meters(x):
        print(f"In Kilometers : {k*x}")
        print(f"In Miles : {mi*x}")
        print(f"In Foot : {f*x}")

    if (lunit == "mi"):
        miles(a)
    elif (lunit == "m"):
        meters(a)
    elif (lunit == "k"):
        kilometers(a)
    elif (lunit == "f"):
        feet(a)
    else:
        print("Enter valid unit! (m/k/f/mi)")


def weight(w):

    # convert all units to one unit
    g = 1  # g to g
    kg = 0.001  # g to kg
    p = 0.002204  # gram  to pounds
    o = 0.03527  # g to founces

    a = w

    def kilogram(x):
        print(f"In Grams : {g/kg*x}")
        print(f"In Pounds : {p/kg*x}")
        print(f"In Ounces : {o/kg*x}")

    def pounds(x):
        print(f"In Grams : {g/p*x}")
        print(f"In Kilograms: {kg/p*x}")
        print(f"In Ounces : {o/p*x}")

    def ounces(x):
        print(f"In Grams : {g/o*x}")
        print(f"In Kilograms : {kg/o*x}")
        print(f"In pounds : {p/o*x}")

    def grams(x):
        print(f"In Kilograms : {kg*x}")
        print(f"In Pounds : {p*x}")
        print(f"In Ounces : {o*x}")

    if (wunit == "k"):
        kilogram(a)
    elif (wunit == "g"):
        grams(a)
    elif (wunit == "o"):
        ounces(a)
    elif (wunit == "p"):
        pounds(a)
    else:
        print("Enter valid unit! (k/g/o/p)")


def Temperature(t):

    a = t

    def celsius(x):
        print(f"In Kelvin : {x + 273.15}")
        print(f"In Fahrenheit : {(x * 9/5) + 32}")

    def kelvin(x):
        print(f"In Celsius : {x - 273.15}")
        print(f"In Fahrenheit: {(x - 273.15) * 9/5 + 32}")

    def fahrenheit(x):
        print(f"In Celsius : {(x - 32) * 5/9}")
        print(f"In Kelvin : {(x - 32) * 5/9 + 273.15}")

    if (tunit == "c"):
        celsius(a)
    elif (tunit == "k"):
        kelvin(a)
    elif (tunit == "f"):
        fahrenheit(a)
    else:
        print("Enter valid unit! (c/k/f)")


if main_choice == 'L':
    lvalue = float(input("Enter current value: "))
    print()
    print("Type,")
    print("m for meter\nk for kilometer\nmi for miles\nf for feet")
    lunit = str(input("Type current unit: "))
    print()
    length(lvalue)

elif main_choice == 'W':
    wvalue = float(input("Enter current value: "))
    print("Type,")
    print("k for Kilogram\ng for Gram\no for Ounce\np for Pound")
    wunit = str(input("Type current unit:"))
    print()
    weight(wvalue)

elif main_choice == 'T':
    tvalue = float(input("Enter current value: "))
    print("Type,")
    print("c for Celsius\nk for Kelvin\nf for Fahrenheit")
    tunit = str(input("Type current unit:"))
    print()
    Temperature(tvalue)
else:
    print("Invalid Choice!")
