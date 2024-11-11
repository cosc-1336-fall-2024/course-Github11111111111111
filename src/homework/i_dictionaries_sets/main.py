#homework 6
from dictionary import add_inventory, remove_inventory_widget

def add_inventory(widgets, widget_name, quantity):
    if widget_name in widgets:
        widgets[widget_name] += quantity
    else:
        widgets[widget_name] = quantity

def remove_inventory_widget(widgets, widget_name):
    if widget_name in widgets:
        del widgets[widget_name]
        return 'Record deleted'
    else:
        return 'Item not found'

def display_menu():
    print("\nInventory Menu")
    print("1 - Add or Update Item")
    print("2 - Delete Item")
    print("3 - Exit")

def main():
    inventory = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            widget_name = input("Enter widget name: ")
            quantity = int(input("Enter quantity: "))
            add_inventory(inventory, widget_name, quantity)
            print(f"{widget_name} updated. Current quantity: {inventory[widget_name]}")
        
        elif choice == '2':
            widget_name = input("Enter widget name to delete: ")
            result = remove_inventory_widget(inventory, widget_name)
            print(result)
        
        elif choice == '3':
            break
        
        else:
            print("Invalid choice.")

main()
