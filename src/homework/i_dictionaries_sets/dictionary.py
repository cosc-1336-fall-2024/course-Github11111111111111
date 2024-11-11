#homework 8
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

inventory = {}
add_inventory(inventory, 'WidgetA', 10)  
add_inventory(inventory, 'WidgetB', 5)   
print(inventory)  

result = remove_inventory_widget(inventory, 'WidgetA')
print(result)  
print(inventory)  

result = remove_inventory_widget(inventory, 'WidgetC')
print(result)  


