def main ():
    mass = int(input("Enter The mass (in Kg): "))
    result = convert(mass)
    print (result)

def convert(mass):
    energy = (mass * 300000000**2)
    return energy

main()