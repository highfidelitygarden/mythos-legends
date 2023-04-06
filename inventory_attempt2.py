import math


inventory = []
items = ['health potion', 'sword', 'mana potion']
item_limit = [15, 1, 15]
max_slots = 16

free_slots = 16


def add_item(item, quantity, limit, free):
    #check if inventory full
    if free == 0:
        print('not enough space')
        
   
   
   #check if empty inventory
    elif inventory == []:
        if quantity <= limit*free:
            full_stacks = math.floor(quantity/limit)
            print(math.floor(quantity/limit))
            remainder = quantity%limit
            print(quantity%limit)
            
            for i in range(full_stacks):
                inventory.append((item,limit,limit))
                free -= 1
                free_slots = free
            if remainder != 0:
                inventory.append((item,remainder,limit))
                
                free -= 1
                free_slots = free
            print('free slots: ', free_slots)
            
        #if empty and trying to add too many items
        else:
            for i in range(free):
                inventory.append((item,limit,limit))
            print('not enough space to fit everything')
        print(inventory)
        
    #if not empty
    else:
        #check if item in inventory and get index(s)
        index = 0
        index_list = []
        for slot in inventory:
            if item in slot[0]:
                
                index_list.append(index)         
                index += 1
                
        #if item in inventory
        if index_list != []:
            print('item in inventory')
            print(index_list)
            inventory.append((item,quantity,limit))
            print(inventory)
        
        #if item not in inventory
        if index_list ==[]:
            inventory.append((item,quantity,limit))
            print(inventory)
            
#sort the inventory     
def sort_inventory(inventory):
    inventory = sorted(inventory)
    print(inventory)

add_item(items[0],10, item_limit[0], free_slots)
print()

add_item(items[0],10, item_limit[0], free_slots)
print()

add_item(items[1],10, item_limit[1], free_slots)
print()

add_item(items[0],10, item_limit[0], free_slots)
print()

sort_inventory(inventory)


