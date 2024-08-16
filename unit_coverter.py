print(
    "********************[Welcome to Unit Conversion programme]********************")
print("Enter")
print("L for Length")
print("W for Weight")
print("T for Temperature")
print("E for Exiting the programme anytime")
print()


def get_valid_input_for_main():
    while True:
        valid_input = str(input("Enter option: ")).upper()

        if valid_input in ['L', 'W', 'T', 'E']:
            if valid_input == 'E':
                print("Exiting the programme")
                break
            else:
                return valid_input
        else:
            print("Enter valid Character!")


main_choice = get_valid_input_for_main()

# value = float(input("Enter current value: "))


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

    if (type_of_unit == "mi"):
        miles(a)
    elif (type_of_unit == "m"):
        meters(a)
    elif (type_of_unit == "k"):
        kilometers(a)
    elif (type_of_unit == "f"):
        feet(a)


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

    if (type_of_unit == "k"):
        kilogram(a)
    elif (type_of_unit == "g"):
        grams(a)
    elif (type_of_unit == "o"):
        ounces(a)
    elif (type_of_unit == "p"):
        pounds(a)


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

    if (type_of_unit == "c"):
        celsius(a)
    elif (type_of_unit == "k"):
        kelvin(a)
    elif (type_of_unit == "f"):
        fahrenheit(a)


def get_valid_input_for_unit(unit_type, valid_units, prompt_message):
    while True:
        print(prompt_message)
        unit_type = str(input("Type current unit: "))

        if unit_type in valid_units:
            if unit_type == 'E':
                print("exiting the programme")
                break
            else:
                return unit_type
        else:
            print("Enter valid unit!")


def get_valid_input_value():

    while True:
        valid_value = float(input("Enter current value:"))

        if valid_value > 0:
            if valid_value == 'E':
                print("exiting the programme")
                break
            else:
                return valid_value
        else:
            print("Enter Positive value!")


if main_choice == 'L':
    prompt = "Type,\nm for meter\nk for kilometer\nmi for miles\nf for feet"
    valid_units = ['k', 'mi', 'f', 'm', 'E']
    unit_value = get_valid_input_value()
    type_of_unit = get_valid_input_for_unit('length', valid_units, prompt)

    length(unit_value)


elif main_choice == 'W':
    prompt = "Type,\nk for Kilogram\ng for Gram\no for Ounce\np for Pound"
    valid_units = ['k', 'g', 'o', 'p', 'E']

    unit_value = get_valid_input_value()
    type_of_unit = get_valid_input_for_unit('weight', valid_units, prompt)

    weight(unit_value)


elif main_choice == 'T':
    prompt = "Type,\nc for Celsius\nk for Kelvin\nf for Fahrenheit"
    valid_units = ['c', 'k', 'f', 'E']
    unit_value = get_valid_input_value()
    type_of_unit = get_valid_input_for_unit('temperature', valid_units, prompt)

    Temperature(unit_value)
