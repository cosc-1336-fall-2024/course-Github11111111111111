#create function
def get_factorial(num):
    if num < 0:
        return 
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

def sum_odd_numbers(num):
    total = 0
    current = 1  
    
    while current <= num:
        total += current  
        current += 2  
    
    return total

def display_menu():
    print("1 - Factorial")
    print("2 - Sum odd numbers")
    print("3 - Exit")



