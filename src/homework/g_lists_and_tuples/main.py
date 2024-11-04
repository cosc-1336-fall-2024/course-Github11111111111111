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

def main():
    while True:
        print("\nMenu")
        print("1 - Show the list low/high values")
        print("2 - Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            numbers = []
            while True:
                value = input("Enter a list value: ")
                
                try:
                    numbers.append(float(value))
                except ValueError:
                    continue
                
                if len(numbers) >= 3:
                    another = input("Do you want to enter another value? (yes/no): ").strip().lower()
                    if another != 'yes':
                        break
        
            lowest = get_lowest_list_value(numbers)
            highest = get_highest_list_value(numbers)
            print(f"The lowest value is: {lowest}")
            print(f"The highest value is: {highest}")
        
        elif choice == '2':
            break
        
main()
