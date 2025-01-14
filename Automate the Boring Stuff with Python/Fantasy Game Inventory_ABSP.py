inventory={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inv):
    tot=0
    print('Inventory:')
    for item in inv:
        print(str(inv[item]),item)
        tot+=inv[item]
    print('Total number of items:',tot)
displayInventory(inventory)