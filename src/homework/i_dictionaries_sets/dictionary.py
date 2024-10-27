#homework 6
def get_p_distance(list1, list2):
    differences = 0
    length = len(list1)  

    for i in range(length):
        if list1[i] != list2[i]:
            differences += 1

    return differences / length

def get_p_distance_matrix(lists):
    n = len(lists)  
    matrix = [] 

    for i in range(n):
        row = []  
        for j in range(n):
            distance = get_p_distance(lists[i], lists[j])
            row.append(distance)  
        matrix.append(row)  

    return matrix

# Sample input
lists = [
    ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A'],  # list1
    ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C'],  # list2
    ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'T'],  # list3
    ['G', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A']   # list4
]

matrix = get_p_distance_matrix(lists)

for row in matrix:
    for value in row:
        print("%.5f" % value, end=" ")  
    print()  
