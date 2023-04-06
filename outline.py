#pylint:disable=W0401
#pylint:disable=C0103
#pylint:disable=C0301
'''
        Prototype Outline for Mythos Legends
        
        Classes - Entity, Player(Entity), NPC(Entity), Stats, Reputation, Item, Weapon(Item), Armor(Item), Inventory, Skills, Classes, (Individual Classes), Faction, Dialogue
        
        This module is Mythos Legends without breaking thr class structure into different files to make for easier testing as it is built.
        
'''



# Mythos Legends
from gear_data import *
import math



# Entity
class Entity:
    """
    Entity class - all players, npcs, and enemies will inherit from this class

    Parameters - name, level, speed, position, image

    returns - Entity object never called directly

    Attributes - name, level, stats, speed, position, image
    """

    def __init__(self, name: str, level: int, speed: int, position: tuple, image):
        self.name = name
        self.level = level
        self.stats = Stats(level)
        self.speed = speed
        self.position = position
        self.image = image


# Player


class Player(Entity):
    """
    Player class - this class manages all player characters

    Parameters - name, level, speed

    Returns - Player object with Entity inheritance

    Attributes - name, level, hp, mp, stats, position, image

    """

    def __init__(self, name:str, level:int, speed:int, position:tuple, image):
        super().__init__(name, level, speed, position, image)
        self.xp = 0
        self.xp_to_lvl = (level * 45 ** 2) + 150
        self.playtime = 0
        self.skills = Skills()
        self.inventory = Inventory()
        
    def __str__(self):
        return  f'Name - {self.name}, \nLevel - {self.level}, \nStats - {self.stats}, \nSpeed - {self.speed}, \nPosition - {self.position}, \nImage - {self.image}, \nXP - {self.xp}, \nXP to  Level - {self.xp_to_lvl}, \nPlaytime - {self.playtime}, \nSkills - {self.skills}, \nInventory - {self.inventory}'
    
    def gain_xp(self, xp):
        if xp < self.xp_to_lvl - self.xp:
            self.xp += xp
            self.__str__()
        elif xp == self.xp_to_lvl - self.xp:
            self.level_up()
            self.xp = 0
            self.__str__()
        elif xp > self.xp_to_lvl - self.xp:
            xp = self.xp + xp
            xp_overflow = -1* (self.xp_to_lvl - xp)
            self.level_up()
            self.xp = 0
            self.gain_xp(xp_overflow)


            
    def level_up(self):
        self.level +=1
        self.xp_to_lvl = (self.level * 45 ** 2) + 150
        self.stats = Stats(self.level)
       # print(f'Congrats you made it to level {self.level}. You have {self.xp_to_lvl-self.xp} xp to level {self.level+1}')



class NPC(Entity):
    """
        NPC class - this class manages all non-player characters

        Parameters - name, level, speed, position, image, dialgoue dict

        Returns - Player object with Entity inheritance

        Attributes - name, level, hp, mp, stats, position, image, dialogue

        """

    def __init__(self, name:str, level:int, speed:int, position:tuple, image):
        super().__init__(name, level, speed, position, image)
        #self.dialogue = Dialogue(dialogue)
        self.inventory = Inventory()

    def __str__(self):
        return  f'Name - {self.name}, \nLevel - {self.level}, \nStats - {self.stats}, \nSpeed - {self.speed}, \nPosition - {self.position}, \nImage - {self.image},\nInventory - {self.inventory}'


# NPC
# Entity
# Dialogue

# Enemies
# Stats
# Entity

# Stats

class Stats:
    """
        Stats class - All entities with any battle mechanics will inherit from this class for their base stats
       
         Parameters - level

        Returns - Stats object to be inherited by the Entity object

        Attributes - hp, mp, strength, agility, intellect, charisma, wisdom, vitality

        """

    def __init__(self, level:int):
        self.hp = int(120 * 1.052 ** (1.045 * level))
        self.mp = int(60 * 1.052 ** (1.045 * level))
        self.strength = int(10.93 * 1.06 ** level)
        self.agility = int(10.93 * 1.06 ** level)
        self.intellect = int(10.93 * 1.06 ** level)
        self.charisma = int(10.93 * 1.06 ** level)
        self.wisdom = int(10.93 * 1.06 ** level)
        self.vitality = int(10.93 * 1.06 ** level)
        

    def __str__(self):
        return f'Str:{self.strength}, Agi:{self.agility}, Int:{self.intellect}, Cha:{self.charisma}, Wis:{self.wisdom}, Vit:{self.vitality}'


# strength (affects damage and crit %)
# agility (affects dodge/hit%)
# intellect (affects spell damage)
# charisma (affects reputation)
# wisdom (affects mana and regen)
# vitality (affects hp and regen)

class Reputation:
    pass


# Items
class Item:
    """
        Item class - All entities with any battle mechanics will inherit from this class for their base stats
       
         Parameters - dictionary of items, item category, item name

        Returns - Item object to be inherited by any class of items in the game (weapons, armor, consumables, etc)

        Attributes - cost, value, stack, rarity, slot. item type, item level, required level, inventory, total space, effects

        """

    def __init__(self, item:dict, category:str, name:str):
        self.name = name
        self.category = category
        self.cost = item[category][name]['cost']
        self.value = int(self.cost / 2)
        self.stack = item[category][name]['stack']
        self.in_inventory = item[category][name]['in_inventory']
        self.rarity = item[category][name]['rarity']
        self.slot = item[category][name]['slot']
        self.item_type = item[category][name]['item_type']
        self.item_level = item[category][name]['item_level']
        self.required_level = item[category][name]['required_level']
        self.effects = list(item[category][name]['effects'].keys())
        self.effects_data = list(item[category][name]['effects'].values())


    def __str__(self):
        return f'Name - {self.name} \nCategory - {self.category}, \nCost - {self.cost}, \nValue - {self.value}, \nStack - {self.stack}, \nRarity - {self.rarity}, \nSlot - {self.slot}, \nType - {self.item_type}, \nItem Level - {self.item_level}, \nRequired Level{self.required_level}, \nEffects - {self.effects}, \nEffects Data - {self.effects_data}'
        
    def __repr__(self):
        return f'{self.name}'

    

# Weapons
class Weapon(Item):
    """
        Weapon class - Class for all weapons in the game. Weapons inherit from the Item class will inherit from this class for their base stats
       
         Parameters - dictionary of weapons, weapon category, weapon name

        Returns - weapon object

        Attributes - cost, value, stack, rarity, slot. item type, item level, required level, inventory, total space, effects

        """

    def __init__(self):
        pass
# dps
# speed

# Stats
# Items

class Armor(Item):
    """
        Armor class - Class for all armor in the game. Armor inherit from the Item class will inherit from this class for their base stats
       
         Parameters - dictionary of armors, armor category, armor name

        Returns - armor object

        Attributes - cost, value, stack, rarity, slot. item type, item level, required level, inventory, total space, effects

        """
    def __init__(self):
        pass
# Armor
# Stats
# Items

class Inventory:
    """
        Inventory class - All entities with any trading ability will have an inventory object
       
         Parameters -

        Returns - Inventory object

        Attributes - inventory list of item objects, total space, free space, money
        
        Methods - add item, use item, delete item

        """

    def __init__(self):
        self.inventory = []
        self.inventory_2 = []
        self.inv_dict = {}
        self.inv_qty = []
        self.total_space = 16
        self.full_slots = 0
        self.free_space = self.total_space - len(self.inventory)
        self.money = {'gold':0, 'silver':0, 'copper':0}
    
    def __str__(self):
        return f'{self.inventory}, \nTotal Space - {self.total_space}, \nFree Space - {self.free_space}, \nMoney - {self.money}'
        
        
        
        
    def item_add(self,item,quantity):
        current_quantity = sum([tup[1] for tup in self.inventory if tup[0] == item])
        print('current quantity ', current_quantity)
        total_quantity = current_quantity+quantity
        print('total quantity ', total_quantity)
        self.inventory.append([item, quantity])
        print('inventory: \n', self.inventory)
        
        for tup in self.inventory:
             if tup[0]==item and tup[1]<item.stack:
                 print(tup[0],'-', tup[1])
               #  print(tup[1])
            
        
        
#    #NOT WORKING
#    def item_add(self, item, quantity):
# 
#        current_quantity = sum([tup[1] for tup in self.inventory if tup[0] == item])
#        print(current_quantity, 'current quantity')
#        total_quantity = current_quantity+quantity
#        print(math.ceil(1))
#        stack_qty = math.ceil(current_quantity/item.stack)
#     #   stack_qty = int(current_quantity/item.stack)
#        remainder = current_quantity%item.stack
#        if remainder != 0:
#            self.full_slots = stack_qty - 1
#        else:
#            self.full_slots = stack_qty
#        #if remainder != 0:
#           # self.full_slots += 1
#        print(stack_qty,'stackqty')
#        print(remainder,'remainder')
#        print(self.inventory)
#        print(self.full_slots, 'full slots')
#        #print(self.inventory)
#        
#        
        
#        partial_stack_index = [tup[0] for tup in self.inventory if tup[1] != item.stack and tup[0] == item]
#        print(partial_stack_index, "index")
 #       print(total_quantity, 'total quantity')
#        
# 

#        
#        for tup in self.inventory:
#            count=1
#            if count < self.full_slots:
#                if tup[1] < tup[0].stack:
#                        tup[1] = tup[0].stack
#                        count += 1
#                else:
#                        print('full stack')
#            elif count == self.full_slots and remainder > 0:
#                tup[1] = remainder
#                print(f'remainder is {remainder}')
#        
#        print(current_quantity)
#        #else:
#        self.inventory.append([item,quantity])
#        #self.inventory.sort(key = item.in_inventory)
#        partial_stack_index = [tup[0] for tup in self.inventory if tup[1] != tup[0].stack and tup[1] == item]
#        #print(partial_stack_index, "index")
#        #print(self.inventory)
#        placeholder = []
#        for item in self.inventory:
#            placeholder.append(item)
#          #  placeholder.sort()
#        print('placeholder',placeholder)
#            
        
        
        
        
        
        
#    def add_item(self,item,quantity):
#        if item in self.inventory:
#            index = self.inventory.index(item)
#            print(f'Index - {index}')
#            if self.inv_qty[index] < item.stack:
#                print(f'Inv Qty - {self.inv_qty[index]}')
#                print(f'Stack - {item.stack}')
#                #print(f'{quantity - self.inv_qty[index]}')
#                add_on = quantity - self.inv_qty[index]
#                if add_on > item.stack:
#                    self.inventory.append(item)
#                    self.inv_qty[self.inventory.index(item)] = item.stack
#                print(add_on)
#                print(self.inventory)
#            #check quantity vs stack!
#        elif self.free_space > 0:
#            self.inventory.append(item)
#            self.inv_qty.append(quantity)
#            self.free_space = self.total_space-len(self.inventory)
#        else:
#            print("You don't have space for this item")


#    def add_item_dict(self, item, quantity):
#       if item.name in self.inv_dict:
#            quantity += self.inv_dict[item.name]
#            self.inv_dict[item.name] = quantity
#            print(f'{item.name}, {self.inv_dict[item.name]}')
#       else:
#           self.inv_dict[item.name] = quantity
#           print(f'{item.name}, {self.inv_dict[item.name]}')

#        
#    def add_item2(self, item, quantity):
#        print(item.stack)
#        print(quantity)
#        print(self.free_space)
#        if item in self.inventory:
#            print('item in inventory')
#            self.inventory_2.append(item)
#            self.inv_qty.append(quantity)
#        elif self.free_space > 0 and quantity/item.stack < self.free_space:
#            print('1')
#            self.inventory_2.append(item)
#        else:
#            print('2')
#            self.inventory_2.append(item)
#        print(self.inventory_2)
#        
        
        
    def use_item(self,item,target):
        if target in item.target:
            for effect in item.effects:
                if effect == 'health':
                    print(item.effects['health'])
                elif effect == 'mana':
                    print(item.effects[effect])
                
    
    def delete_item(self,item):
        '''
        Delete Item - this method manages any action where an item is removed from your inventory
        
        Parameters - item
        
        Returns - nothing
        
        '''
        self.inventory.pop(item)
        self.free_space = self.total_space-len(self.inventory)


    
    def gain_money(self, gold, silver, copper):
        '''
        Gain money - this method manages any action where you will gain money and recalculates your current balance
        
        Parameters - gold, silver and copper gained
        
        Returns - your new balance
        
        '''
        self.money['gold'] += gold
        
        if self.money['silver'] + silver > 99:
            print('madeit')
            self.money['gold'] += 1
            self.money['silver'] = (self.money['silver']+silver)-100
        else:
            self.money['silver'] += silver
        if self.money['copper'] + copper > 99:
            self.money['silver'] += 1
            self.money['copper'] = (self.money['copper']+copper)-100
        else:
            self.money['copper'] += copper
        print(self.money)



    def spend_money(self,gold, silver, copper):
        '''
        Spend money - this method manages any action thay will spend money. It calculates if you have enough money to spend and if you do then it spends the money and calculates your change, if you don't then it tells you you dont have enough money
        
        Parameters - gold, silver and copper price of the purchase
        
        Returns - your new balance and whether you had enough money
        
        '''
        #convert money to copper
        total_money = (self.money['gold']*10000)+(self.money['silver']*100)+self.money['copper']
        #convert cost to copper
        total_cost = (gold*10000)+(silver*100)+copper
        print(total_cost)
        #if enough money then spend it
        if total_money >= total_cost:
            total_money -= total_cost
            self.money['gold'] = int(total_money/10000)
            total_money = total_money%10000
            self.money['silver'] = int(total_money/100)
            total_money = total_money%100
            self.money['copper'] = int(total_money)
        #if not enough money tell player
        else:
            print('You don\'t have enough money')
        print(self.money)
        
        


# Inventory
# slots
# money
# mail

class Skills:
    def __init__(self):
        
        self.skill_class= 'skill_class'
        self.attack_class = 'attack_class'
        self.skill_tree = 'skill tree'
    
    
    def __str__(self):
        return f'Skill Class - {self.skill_class}, \nAttack Class - {self.attack_class}, \nSkill Tree - {self.skill_tree}'
# Skills
# Attacks

# Buffs

# Skill Tree


class Classes:
    def __init__(self):
        self.talent_points = 1
        self.attacks = {}
        self.defenses = {}


# Magic
class Mage(Classes):
    """ int->agi->wis->vit->cha->str"""

    def __init__(self):
        super().__init__()
        self.specialization = {'fire':True, 'frost':False, 'shadow':False}
        self.armor_type = "cloth"
        
        

class Necromancer(Classes):
    """ wis->vit->int->agi->str->cha"""

    def __init__(self):
        super().__init__()
        self.specialization = "summoning"
        self.armor_type = "cloth"


class Priest(Classes):
    """ vit->wis->int->agi->cha->str"""

    def __init__(self):
        super().__init__()
        self.specialization = "dark magic"
        self.armor_type = "cloth"


# Human
class Tank(Classes):
    """ str=vit->agi->cha->int->wis"""

    def __init__(self):
        super().__init__()
        self.specialization = "warrior"


class Samurai(Classes):
    """ agi->str->vit->cha->wis->int"""

    def __init__(self):
        super().__init__()
        self.specialization = "katana"
        self.armor_type = "leather"

class Engineer(Classes):
    """ int->wis->agi->vit->cha->str"""

    def __init__(self):
        super().__init__()
        self.specialization = "engineer"
        self.armor_type = "leather"

class Alchemist(Classes):
    """ vit->wis->agi->int->str->cha"""

    def __init__(self):
        super().__init__()
        self.specialization = "potions"
        self.armor_type = "cloth"

# Classes
# Tank
# Samurai
# DPS 1 ()
# Engineer
# DPS 2 (spells)
# Mage
# Necromancer
# DPS 3 (ranged)

# Healer
# Alchemist
# Priest
# Medic

class Faction:
    """
        Faction  class - this class manages all the factions  in the game

        Parameters -

        Returns - Faction object to be used by all Entities

        Attributes - name, level, hp, mp, stats, position, image

        """    
    def __init__(self, name, description, allies, enemies):
        self.name = name
        self.description = description
        self.allies = allies
        self.enemies = enemies


# Factions
# Magic
# Arcane Order
# Church of the Divine
# Brotherhood of Shadow
# Circle of Elements

# Science
# Guild of the Alchemist

# MagSci
# Artifactors

# Map

# Level
# Tile

# Quests
class Dialogue:
    """
        Dialogue class - this class manages all the dialogue in the game

        Parameters - dialogue dictionary

        Returns - Dialogue object to be used by all Entities

        Attributes - name, level, hp, mp, stats, position, image

        """

    def __init__(self, dialogue: dict):
        self.greetings = dialogue['greetings']
        self.farewells = dialogue['farewells']
        self.questions = dialogue['questions']
        self.responses = dialogue['responses']
        self.quests = dialogue['quests']
        self.storyline = dialogue['storyline']


# Game Loop

if __name__ == '__main__':
    


    pj = Player('PJ',1,5,(20,50),'image')
    health_potion = Item(consumables, 'restore', 'health potion')
    mana_potion = Item(consumables, 'restore', 'mana potion')
  #  print(health_potion)
   #  print(mana_potion)
    
    
    pj.inventory.item_add(health_potion,10)
    pj.inventory.item_add(health_potion,10)
    pj.inventory.item_add(mana_potion,8)
    pj.inventory.item_add(mana_potion,10)
    pj.inventory.item_add(health_potion, 8)
    #print(health_potion.in_inventory)
    #print(consumables['restore']['health potion']['in_inventory'])

#    pj.inventory.gain_money(10,0,0)
#    pj.inventory.spend_money(9,50,30)
