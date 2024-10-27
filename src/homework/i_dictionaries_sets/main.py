#homework 6
from dictionary import get_p_distance_matrix

def get_p_distance(list1, list2):
    differences = 0
    length = len(list1)
    for i in range(length):
        if list1[i] != list2[i]:
            differences += 1
    return differences / length

def get_p_distance_matrix(lists):
    matrix = []
    for i in range(len(lists)):
        row = []
        for j in range(len(lists)):
            row.append(get_p_distance(lists[i], lists[j]))
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:.5f}", end=" ")
        print()

def main():
    while True:
        print("\n1- Get p distance matrix\n2- Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            n = int(input("Number of DNA sequences: "))
            length = int(input("Length of each sequence: "))
            dna_list = []

            for i in range(n):
                sequence = list(input(f"Sequence {i + 1}: ").strip().upper())
                dna_list.append(sequence)

            matrix = get_p_distance_matrix(dna_list)
            print("\nP-Distance Matrix:")
            display_matrix(matrix)

        elif choice == "2":
            print("Exit")
            break
main()
