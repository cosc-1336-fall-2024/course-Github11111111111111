#Homework 7
def get_lowest_list_value(numbers):
    lowest = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < lowest:
            lowest = numbers[i]
    return lowest

def get_highest_list_value(numbers):
    highest = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > highest:
            highest = numbers[i]
    return highest
