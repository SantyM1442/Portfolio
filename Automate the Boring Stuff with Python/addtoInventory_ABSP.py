dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory={}
def addtoInventory(inventory,addedItems):
    item=''
    tot=0
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item]+=1
    print('Inventory:')
    for item in inventory:
        print(str(inventory[item]), item)
        tot += inventory[item]
    print('Total number of items:', tot)
addtoInventory(inventory,dragonLoot)