inventory = []
item = ['health potion', 'sword', 'mana potion']
limit = [15, 1, 15]
max_slots = 16
free_slots = 16


def add_item(item, quantity, limit):
   #inventory.append((item,quantity,limit))
   if inventory == []:
       if quantity <= limit*free_slots:
           inventory.append((item,quantity,limit))
       else:
           print('not enough space!!!')

   else: 
#   else:
#       print('else')
#       for tuple in inventory:
#           #print(tuple)
#           if item not in tuple[0]:
#               inventory.append((item,quantity,limit))
#           elif item in tuple[0]:
#               print(1)
#               inventory.append((item,quantity,limit))
   
print(inventory)      
add_item(item[0],10, limit[0])
print(inventory)
add_item(item[0],10, limit[0])

print(inventory)
