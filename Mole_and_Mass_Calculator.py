import elements
import sys

AVOGADRO_NUMBER = 6.022
AVOGADRO_POWER = 23

#Check mass to number of atoms

def main():
    menu_choice = "0"
    while menu_choice != "7":
        display_menu()
        menu_choice = input("Enter the number matching your selection: ")
        results = handle_choice(menu_choice)
        print(""'\n')
        print (results)
        print("")
    
    
#Option 1
#Calculates the number of moles to the equivalent number of atoms
#Gives user an error for inputting unusable data
def number_of_moles_to_atoms():
    try:
        num_moles = float(input("Number of moles: "))
        answer = num_moles * AVOGADRO_NUMBER
        
        return str(answer) + " * 10^23"
    except ValueError:
        print('\n'"Cannot use that input \nplease use a number")
    except TypeError:
        print('\n'"Cannot use that input \nPlease use the full element name or abbreviation")

#Option 2
#Calculates the number of atoms given by the user into the equivalent number of moles
#Splits up the user's input for separate use in the equation
#Gives the user an error for inputting unusable data
def number_of_atoms_to_moles():
    try:
        input_mass = input("Number of atoms: ")
        input_e = input_mass.split("^")[1]
        input_power = float(input_e)
        
        power = input_power - AVOGADRO_POWER
        atom_numbere = input_mass.split()[0]
        atom_number = float(atom_numbere)
        
        atom_answer = atom_number/AVOGADRO_NUMBER
        return str(atom_answer) + " * 10^" + str(power)
    
    except ValueError:
        print('\n'"Cannot use that input \nplease use a number")
    except TypeError:
        print('\n'"Cannot use that input \nPlease use the full element name or abbreviation")
    except IndexError:
        print('\n'"Please input the number of atoms with a power of ten")

    


#Option 3
#Calculates the mass from the number of moles submitted by the user
#Gives the user an error for inputting unusable data
def mass_from_moles():
    try:
        input_moles = float(input("Number of moles: "))
        answer = elements.elements_choice() * input_moles
        return str(answer) + " mass of element"
    except ValueError:
        print('\n'"Cannot use that input \nplease use a number")
    except TypeError:
        print('\n'"Cannot use that input \nPlease use the full element name or abbreviation")
        

#Option 4
#Calculates the number of moles from the mass input by the user
def moles_from_mass():
    try:
        input_mass = float(input("Mass of sample: "))
        answer = input_mass/elements.elements_choice()
        return str(answer) + " moles of element"
    except ValueError:
        print('\n'"Cannot use that input \nplease use a number")
    except TypeError:
        print('\n'"Cannot use that input \nPlease use the full element name or abbreviation")

#Option 5
#Calculates the number of atoms from a mass input by the user
#Gives the user an error for inputting unusable data
def mass_to_number_of_atoms():
    try:
        input_mass = float(input("Mass of sample (g): "))
        multiply = input_mass * AVOGADRO_NUMBER
        answer = multiply/elements.elements_choice()
        return str(answer) + " * 10^23"
    except ValueError:
        print('\n'"Cannot use that input \nplease use a number")
    except TypeError:
        print('\n'"Cannot use that input \nPlease use the full element name or abbreviation")


#Option 6
#Calculates the mass from a number of atoms input by the user
#Gives the user an error for inputting unusable data
#Splits up the user's input for separate use in the equation
#Returns the answer, one with the ten power, one multiplied by the ten power
def number_of_atoms_from_mass():
    try:
        input_mass = input("Number of atoms: ")
        input_e = input_mass.split("^")[1]
        input_power = float(input_e)
        
        power = input_power - AVOGADRO_POWER
        atom_numbere = input_mass.split()[0]
        atom_number = float(atom_numbere)
        
        multiply = atom_number * elements.elements_choice()
        answer = multiply/AVOGADRO_NUMBER
        
        ten_power = 10 ** power
        answer_without_ten_power = ten_power * answer
        
        return str(answer) + " * 10^" +str(int(power)) + " g" '\n' + str(answer_without_ten_power) + " g"
    except ValueError:
        print('\n'"Cannot use that input \nplease use a number")
    except TypeError:
        print('\n'"Cannot use that input \nPlease use the full element name or abbreviation")
    except IndexError:
        print('\n'"Please input the number of atoms with a power of ten")


#Option 7
def quit_program():
    print("Quitting program...")
    sys.exit()


def handle_choice(menu_choice):
    if menu_choice == "1":
        return number_of_moles_to_atoms()
    elif menu_choice == "2":
        return number_of_atoms_to_moles()
    elif menu_choice == "3":
        return mass_from_moles()
    elif menu_choice == "4":
        return moles_from_mass()
    elif menu_choice == "5":
        return mass_to_number_of_atoms()
    elif menu_choice == "6":
        return number_of_atoms_from_mass()
    elif menu_choice == "7":
        return quit_program()
    else:
        print("Invalid selection.")


def display_menu():
    print("MENU" '\n')    
    print("1) Calculate the number of atoms in a mole")
    print("__")
    print("2) Calculate the number of moles from a number of atoms")
    print("__")
    print("3) Calculate the mass from a number of moles")
    print("__")
    print("4) Calculate the number of moles in a mass")
    print("__")
    print("5) Calculate the number of atoms from the mass")
    print("__")
    print("6) Calculate the mass from a number of atoms")
    print("__")
    print("7) Quit" '\n' '\n') 





main()