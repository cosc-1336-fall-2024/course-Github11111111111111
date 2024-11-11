#homework 8
from src.homework.i_dictionaries_sets.dictionary import add_inventory
from src.homework.i_dictionaries_sets.dictionary import remove_inventory_widget

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

def test_add_inventory():
    inventory = {}
    add_inventory(inventory, 'Widget1', 10)
    assert inventory['Widget1'] == 10, "Failed: Widget1 should have quantity 10"
    
    add_inventory(inventory, 'Widget1', 25)
    assert inventory['Widget1'] == 35, "Failed: Widget1 should have quantity 35 after update"
    
    add_inventory(inventory, 'Widget1', -10)
    assert inventory['Widget1'] == 25, "Failed: Widget1 should have quantity 25 after update with -10"

def test_remove_inventory_widget():
    inventory = {}
    add_inventory(inventory, 'Widget1', 15)
    add_inventory(inventory, 'Widget2', 20)
    
    result = remove_inventory_widget(inventory, 'Widget1')
    assert result == 'Record deleted', "Failed: Widget1 should be deleted"
    
    assert len(inventory) == 1, "Failed: Inventory should have 1 item left"
    
    assert 'Widget2' in inventory, "Failed: Widget2 should still exist in inventory"
    assert inventory['Widget2'] == 20, "Failed: Widget2 should have quantity 20"

test_add_inventory()
test_remove_inventory_widget()


