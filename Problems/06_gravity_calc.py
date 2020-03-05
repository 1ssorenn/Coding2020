# Universal Gravity Calculator (12pts)
# In physics, the force of gravity between two objects can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters


# Make a calculator that does all of the following
# (3pts) takes the inputs for mass 1, mass 2, and distance between the two objects (m1, m2, and r)
# (4pts) contains exceptions for any potential errors (value and dividebyzero).
# (2pts) keeps asking for inputs until they are valid (see while loop from notes)
# (3pts) calculates the force of gravity in Newtons and print the result to the user in scientific notation to two decimals.
done = False
done2 = False
done3 = False

G = 6.67e-11


while not done:
    try:
        m1 = float(input("\nEnter mass 1(kg): "))
        done = True
        while not done2:
            try:
                m2 = float(input("\nEnter mass 2(kg): "))
                done2 = True
                while not done3:
                    try:
                        r = float(input("\nEnter distance(meters) between objects: "))
                        F = G * (m1 * m2) / r ** 2
                        done3 = True
                    except ValueError as e:
                        print("Invalid,", e)
                        print("Enter a new value.")
                    except ZeroDivisionError as y:
                        print("Error:", y)
                        print("Enter a new value")
            except ValueError as e:
                print("Invalid,", e)
                print("Enter a new value.")
    except ValueError as e:
        print("Invalid,", e)
        print("Enter a new value.")

print("{:.3}".format(F))







