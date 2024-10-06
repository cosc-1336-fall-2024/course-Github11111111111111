#Homework 5
import strings

def display_menu():
    print("----MENU----\n1-Hamming Distance\n2-Dna Complement\n3-Exit")

def run_menu():

    option = 0
    while option != 3: 
        display_menu()
        option = int(input("Prompt your selection: "))

        if option == 1:
            dna1 = input("Prompt enter DNA1: ")
            dna2 = input("Prompt enter DNA2: ")
            result1 = strings.get_hamming_distance(dna1, dna2)
            print("result: ", result1)

        elif option == 2:
            dna = input("Prompt enter DNA: ")
            result2 = strings.get_dna_complement(dna)
            print("result: ", result2)

        elif option == 3:
            exit()

        else:
            exit()

run_menu()